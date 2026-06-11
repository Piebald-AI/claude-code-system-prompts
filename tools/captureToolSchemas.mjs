#!/usr/bin/env node
// Capture Claude Code's tool `input_schema` values into tool-schemas/<slug>.json
// by running a tiny intercepting HTTP server, pointing `claude -p` at it via
// ANTHROPIC_BASE_URL, and pulling `tools[]` out of the POST /v1/messages
// request body Claude Code sends.
//
// The server captures the request body and then replies with a stub auth
// error — so it never forwards anywhere and doesn't need a valid upstream
// session. Claude exits immediately on the error, the script collects the
// captured tools, moves on to the next run, and finally writes one JSON
// Schema document per tool name to tool-schemas/<slug>.json.
//
// Usage:
//   node tools/captureToolSchemas.mjs
//
// Requires:
//   - `claude` CLI on PATH (Claude Code v2.1.168+).
//   - Claude Code does not need to actually succeed in talking to Anthropic;
//     the script just needs Claude Code to *send* its request. So no API key,
//     no valid OAuth, no network access to Anthropic — anything that lets
//     `claude -p` get as far as the first POST is enough.
//
// What this script produces:
//   - One file per tool name under tool-schemas/, e.g. `bash.json`,
//     `ask-user-question.json`, `lsp.json`.
//   - Four runs cover the four surface conditions the existing PR captures:
//     default (29), --agent-teams (+3), local-agent entrypoint (+2),
//     brief / KAIROS (+1).
//   - StructuredOutput is intentionally skipped — its `input_schema` is
//     supplied per-call by the workflow that spawned the sub-agent, so
//     there is no stable shape to record (see tool-schemas/README.md).
//   - KAIROS-family build-time-gated tools (SendUserFile, WebBrowser, Snip)
//     and the computer-use MCP tools simply don't appear in `tools[]` on
//     this binary; the script writes whatever it sees and skips the rest.

import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = join(__dirname, '..');
const OUT_DIR = join(ROOT_DIR, 'tool-schemas');

const PORT = Number(process.env.CAPTURE_PORT ?? 4099);

// Inverse of updatePrompts.js's SCHEMA_DISPLAY_NAME_OVERRIDES — when the
// wire-level tool name doesn't kebab-case mechanically. Add entries here
// (and the matching override in updatePrompts.js) as future tools appear.
const NAME_TO_KEBAB_OVERRIDES = {
  LSP: 'lsp',
};

function toKebab(name) {
  if (NAME_TO_KEBAB_OVERRIDES[name]) return NAME_TO_KEBAB_OVERRIDES[name];
  return name
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1-$2')
    .toLowerCase();
}

// Sort all object keys lexically so two runs (or two captures) produce
// byte-stable output. The wire-level payload's emit order is not stable
// across Claude Code processes — only the content is.
function sortKeysDeep(value) {
  if (Array.isArray(value)) return value.map(sortKeysDeep);
  if (value === null || typeof value !== 'object') return value;
  return Object.keys(value)
    .sort()
    .reduce((acc, k) => {
      acc[k] = sortKeysDeep(value[k]);
      return acc;
    }, {});
}

// In-flight capture state for the current run.
let capturedTools = null;

function startStubServer() {
  return new Promise((resolve) => {
    const server = createServer((req, res) => {
      const chunks = [];
      req.on('data', (c) => chunks.push(c));
      req.on('end', () => {
        // Pull tools[] out of the first POST /v1/messages we see this run.
        if (
          capturedTools === null &&
          req.method === 'POST' &&
          req.url.includes('/v1/messages')
        ) {
          try {
            const parsed = JSON.parse(Buffer.concat(chunks).toString('utf8'));
            if (Array.isArray(parsed.tools)) capturedTools = parsed.tools;
          } catch {
            // not JSON, or no tools — leave capturedTools null
          }
        }

        // Stub a 403 so `claude -p` exits immediately. 401 triggers up to
        // four internal retries; 403 surfaces straight through as
        // "Failed to authenticate" and the process exits. We don't care
        // what claude prints — we already have the tools[] in memory.
        res.writeHead(403, { 'content-type': 'application/json' });
        res.end(
          JSON.stringify({
            type: 'error',
            error: {
              type: 'forbidden',
              message: 'capture stub — tools[] already collected',
            },
          }),
        );
      });
    });
    server.listen(PORT, '127.0.0.1', () => resolve(server));
  });
}

function runClaude(extraEnv) {
  return new Promise((resolve) => {
    const child = spawn('claude', ['-p', 'ok'], {
      env: {
        ...process.env,
        ANTHROPIC_BASE_URL: `http://127.0.0.1:${PORT}`,
        ...extraEnv,
      },
      stdio: ['ignore', 'ignore', 'ignore'],
    });
    // We expect claude to exit non-zero (we stubbed an auth error). Resolve
    // either way; the capture happened during the request body.
    child.on('exit', () => resolve());
    child.on('error', () => resolve());
  });
}

async function captureRun(label, extraEnv) {
  capturedTools = null;
  process.stdout.write(`  ${label.padEnd(16)} `);
  await runClaude(extraEnv);
  if (!capturedTools) {
    console.log('no tools[] seen');
    return [];
  }
  console.log(`captured ${capturedTools.length}`);
  return capturedTools;
}

function writeSchemas(tools) {
  if (!existsSync(OUT_DIR)) mkdirSync(OUT_DIR, { recursive: true });
  const written = [];
  for (const t of tools) {
    if (!t.name || !t.input_schema) continue;
    const file = `${toKebab(t.name)}.json`;
    writeFileSync(
      join(OUT_DIR, file),
      JSON.stringify(sortKeysDeep(t.input_schema), null, 2) + '\n',
    );
    written.push(file);
  }
  return written;
}

async function main() {
  console.log(`Listening on http://127.0.0.1:${PORT} (intercept, no upstream)`);
  const server = await startStubServer();

  const runs = [
    { label: 'default', env: {} },
    { label: 'agent-teams', env: { CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: '1' } },
    { label: 'local-agent', env: { CLAUDE_CODE_ENTRYPOINT: 'local-agent' } },
    { label: 'brief', env: { CLAUDE_CODE_BRIEF: '1' } },
  ];

  try {
    const merged = new Map();
    for (const run of runs) {
      const tools = await captureRun(run.label, run.env);
      for (const t of tools) {
        if (!merged.has(t.name)) merged.set(t.name, t);
      }
    }

    merged.delete('StructuredOutput');

    const written = writeSchemas([...merged.values()]);
    console.log(`\nWrote ${written.length} files under ${OUT_DIR}/`);
  } finally {
    server.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
