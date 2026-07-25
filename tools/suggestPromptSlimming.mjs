#!/usr/bin/env node

import { writeFileSync } from 'fs';
import { dirname, join, resolve } from 'path';
import { fileURLToPath } from 'url';

import { analyzePrompts, renderSlimmingReport } from './promptSlimmingAnalysis.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = join(__dirname, '..');

function parseArgs(args) {
  const options = {
    limit: 30,
    outputPath: null,
  };

  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === '--limit') {
      options.limit = Number.parseInt(args[++index], 10);
    } else if (arg === '--out') {
      options.outputPath = resolve(args[++index]);
    } else if (arg === '--help' || arg === '-h') {
      options.help = true;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (!Number.isInteger(options.limit) || options.limit <= 0) {
    throw new Error('--limit must be a positive integer');
  }

  return options;
}

function usage() {
  return [
    'Usage: node tools/suggestPromptSlimming.mjs [--limit N] [--out path]',
    '',
    'Ranks extracted Claude Code prompt files by token footprint and structural',
    'signals that suggest the content should move from always-on prompt prose',
    'into tool schemas, runtime state, skills, or retrieval-backed references.',
    '',
  ].join('\n');
}

try {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    process.stdout.write(usage());
    process.exit(0);
  }

  const analysis = analyzePrompts({
    promptsDir: join(ROOT_DIR, 'system-prompts'),
    readmePath: join(ROOT_DIR, 'README.md'),
    limit: options.limit,
  });
  const report = renderSlimmingReport(analysis);

  if (options.outputPath) {
    writeFileSync(options.outputPath, report);
  } else {
    process.stdout.write(report);
  }
} catch (error) {
  console.error(error.message);
  console.error('');
  console.error(usage());
  process.exit(1);
}
