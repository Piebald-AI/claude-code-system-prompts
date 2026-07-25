import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import test from 'node:test';

import {
  analyzePrompts,
  classifyPrompt,
  parsePromptMarkdown,
  parseReadmeTokenCounts,
  promptCategory,
  renderSlimmingReport,
} from './promptSlimmingAnalysis.mjs';

test('parseReadmeTokenCounts extracts filenames and token counts', () => {
  const counts = parseReadmeTokenCounts(`
- [Data: Big reference](./system-prompts/data-big-reference.md) (**1234** tks) - Reference.
- [**System Prompt: Main**](./system-prompts/system-prompt-main.md) (**42** tks) - Main.
`);

  assert.equal(counts.get('data-big-reference.md').tokens, 1234);
  assert.equal(counts.get('system-prompt-main.md').name, 'System Prompt: Main');
});

test('parsePromptMarkdown reads generated metadata and body', () => {
  const parsed = parsePromptMarkdown(`<!--
name: "Skill: Example"
description: "A quoted description"
ccVersion: "2.1.220"
-->
Body text.
`);

  assert.equal(parsed.name, 'Skill: Example');
  assert.equal(parsed.description, 'A quoted description');
  assert.equal(parsed.body, 'Body text.\n');
});

test('promptCategory maps generated prompt prefixes', () => {
  assert.equal(promptCategory('Data: Claude API reference'), 'data');
  assert.equal(promptCategory('Tool Description: Bash'), 'tool');
  assert.equal(promptCategory('System Reminder: Plan mode'), 'reminder');
  assert.equal(promptCategory('Other prompt'), 'other');
});

test('classifyPrompt prefers retrieval for large data prompts', () => {
  const classified = classifyPrompt({
    filename: 'data-api-reference.md',
    name: 'Data: API reference',
    body: 'You must follow this.\nFor example:\n```js\ncall();\n```\n'.repeat(50),
    tokens: 12_000,
  });

  assert.equal(classified.category, 'data');
  assert.ok(classified.priority >= 8);
  assert.ok(classified.reasons.includes('very large token footprint'));
  assert.ok(
    classified.actions.includes(
      'move reference material behind retrieval or an explicit help/docs command'
    )
  );
});

test('analyzePrompts ranks candidates from prompt files and README counts', () => {
  const root = mkdtempSync(join(tmpdir(), 'prompt-slimming-'));
  const promptsDir = join(root, 'system-prompts');
  mkdirSync(promptsDir);

  try {
    writeFileSync(
      join(root, 'README.md'),
      [
        '- [Data: Big reference](./system-prompts/data-big-reference.md) (**9000** tks) - Reference.',
        '- [Tool Description: Bash details](./system-prompts/tool-description-bash-details.md) (**1200** tks) - Tool.',
      ].join('\n')
    );
    writeFileSync(
      join(promptsDir, 'data-big-reference.md'),
      `<!--
name: "Data: Big reference"
description: "Reference docs"
ccVersion: "2.1.220"
-->
For example, this reference has many details.
`
    );
    writeFileSync(
      join(promptsDir, 'tool-description-bash-details.md'),
      `<!--
name: "Tool Description: Bash details"
description: "Tool docs"
ccVersion: "2.1.220"
-->
You must validate input. Never hide errors.
`
    );

    const analysis = analyzePrompts({
      promptsDir,
      readmePath: join(root, 'README.md'),
      limit: 1,
    });

    assert.equal(analysis.promptCount, 2);
    assert.equal(analysis.totalTokens, 10_200);
    assert.equal(analysis.candidates.length, 1);
    assert.equal(analysis.candidates[0].name, 'Data: Big reference');

    const report = renderSlimmingReport(analysis);
    assert.match(report, /Prompt Slimming Candidates/);
    assert.match(report, /Data: Big reference/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
