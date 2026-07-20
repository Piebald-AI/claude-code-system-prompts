import assert from 'node:assert/strict';
import test from 'node:test';

import {
  assertUniquePromptFilenames,
  decodeSourceEscapes,
  nameToFilename,
  parseYamlString,
  renderPromptFrontmatter,
  yamlString,
} from './promptMarkdownUtils.mjs';

test('nameToFilename applies the documented canonical slug algorithm', () => {
  const cases = [
    ['Agent Prompt: CLAUDE.md creation', 'agent-prompt-claude-md-creation.md'],
    ['Skill: Code Review angle E wrapper/proxy correctness', 'skill-code-review-angle-e-wrapper-proxy-correctness.md'],
    ['Tool Parameter: Bash run_in_background guidance', 'tool-parameter-bash-run-in-background-guidance.md'],
    ['System Prompt: PowerShell edition for 5.1', 'system-prompt-powershell-edition-for-5-1.md'],
    ['Tool Description: Claude.ai project', 'tool-description-claude-ai-project.md'],
    ['Data: --- repeated... punctuation ___', 'data-repeated-punctuation.md'],
  ];

  for (const [name, expected] of cases) {
    assert.equal(nameToFilename(name), expected);
  }
});

test('parseYamlString reads current and legacy generated name scalars', () => {
  assert.equal(parseYamlString('"Agent Prompt: Example"'), 'Agent Prompt: Example');
  assert.equal(parseYamlString("'Agent Prompt: Example'"), 'Agent Prompt: Example');
  assert.equal(parseYamlString("'Agent Prompt: It''s quoted'"), "Agent Prompt: It's quoted");
});

test('decodeSourceEscapes restores escaped source punctuation', () => {
  assert.equal(decodeSourceEscapes('Reply \\`go\\`'), 'Reply `go`');
  assert.equal(decodeSourceEscapes('say \\"yes\\"'), 'say "yes"');
  assert.equal(decodeSourceEscapes('keep \\n and \\t escapes'), 'keep \\n and \\t escapes');
  assert.equal(decodeSourceEscapes('escaped \\\\ slash'), 'escaped \\ slash');
});

test('assertUniquePromptFilenames rejects canonical slug collisions', () => {
  assert.throws(
    () =>
      assertUniquePromptFilenames([
        { name: 'Data: wrapper/proxy' },
        { name: 'Data: wrapper proxy' },
      ]),
    /Canonical filename collision for data-wrapper-proxy\.md/
  );
});

test('yamlString safely quotes YAML-significant and multiline values', () => {
  const values = [
    'Code-review dimension: check whether...',
    '*',
    'contains # a comment marker',
    'true',
    'null',
    'single and "double" quotes',
    ' leading and trailing ',
    'first line\nsecond line',
  ];

  for (const value of values) {
    assert.equal(JSON.parse(yamlString(value)), value);
  }
  assert.throws(
    () => yamlString('closes --> the metadata comment'),
    /HTML comment terminator/
  );
});

test('renderPromptFrontmatter quotes every string field and list item', () => {
  const frontmatter = renderPromptFrontmatter({
    name: 'Agent Prompt: Example',
    description: 'Description: with # YAML syntax\nand a second line',
    version: '2.1.215',
    identifierMap: { 0: 'TRUE', 1: 'NULL_VALUE' },
    agentMetadata: {
      agentType: 'example',
      model: 'inherit',
      color: 'violet',
      permissionMode: 'bubble',
      maxTurns: 200,
      whenToUseDynamic: true,
      tools: ['*', 'Read'],
      toolsNote: 'Tools: all inherited',
      disallowedTools: ['Agent'],
      whenToUse: 'Use when: needed\nAcross lines',
      criticalSystemReminder: 'Do not treat # as a comment',
    },
  });

  assert.match(frontmatter, /^<!--\n/);
  assert.match(frontmatter, /description: "Description: with # YAML syntax\\nand a second line"/);
  assert.match(frontmatter, /ccVersion: "2\.1\.215"/);
  assert.match(frontmatter, /    - "\*"/);
  assert.match(frontmatter, /  whenToUse: "Use when: needed\\nAcross lines"/);
  assert.match(frontmatter, /\n-->\n$/);
});

test('renderPromptFrontmatter preserves scalar tool metadata', () => {
  const frontmatter = renderPromptFrontmatter({
    name: 'Agent Prompt: Legacy example',
    description: 'Legacy scalar metadata',
    version: '2.1.216',
    agentMetadata: {
      tools: '*',
      disallowedTools: 'Agent',
    },
  });

  assert.match(frontmatter, /\n  tools: "\*"\n/);
  assert.match(frontmatter, /\n  disallowedTools: "Agent"\n/);
});
