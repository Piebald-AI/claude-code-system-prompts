import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';

import { parseYamlString } from './promptMarkdownUtils.mjs';

const README_TOKEN_ENTRY =
  /- \[(?:\*\*)?([^\]]+?)(?:\*\*)?\]\(\.\/system-prompts\/([^)]+\.md)\)\s*\(\*\*(\d+)\*\*\s*tks\)/g;

const PROMPT_CATEGORIES = [
  ['Agent Prompt: ', 'agent'],
  ['System Prompt: ', 'system'],
  ['System Reminder: ', 'reminder'],
  ['Tool Description: ', 'tool'],
  ['Tool Parameter: ', 'tool'],
  ['Data: ', 'data'],
  ['Skill: ', 'skill'],
];

const IMPERATIVE_PATTERNS = [
  /\bmust\b/gi,
  /\bnever\b/gi,
  /\balways\b/gi,
  /\bdo not\b/gi,
  /\bdon't\b/gi,
  /\brequired\b/gi,
  /\bshould\b/gi,
];

const EXAMPLE_PATTERNS = [
  /\bfor example\b/gi,
  /\bexamples?:\b/gi,
  /```/g,
  /\be\.g\.\b/gi,
];

export function parseReadmeTokenCounts(readmeContent) {
  const counts = new Map();
  let match;
  while ((match = README_TOKEN_ENTRY.exec(readmeContent)) !== null) {
    counts.set(match[2], {
      name: match[1],
      filename: match[2],
      tokens: Number.parseInt(match[3], 10),
    });
  }
  README_TOKEN_ENTRY.lastIndex = 0;
  return counts;
}

export function parsePromptMarkdown(content) {
  const commentMatch = content.match(/^<!--\n([\s\S]*?)\n-->\n?/);
  if (!commentMatch) {
    return {
      name: null,
      description: null,
      body: content,
    };
  }

  const metadata = commentMatch[1];
  const nameMatch = metadata.match(/^name:\s*(.+)$/m);
  const descriptionMatch = metadata.match(/^description:\s*(.+)$/m);

  return {
    name: nameMatch ? parseYamlString(nameMatch[1]) : null,
    description: descriptionMatch ? parseYamlString(descriptionMatch[1]) : null,
    body: content.slice(commentMatch[0].length),
  };
}

export function promptCategory(name) {
  const prefix = PROMPT_CATEGORIES.find(([candidate]) =>
    String(name || '').startsWith(candidate)
  );
  return prefix ? prefix[1] : 'other';
}

function countMatches(patterns, text) {
  return patterns.reduce((total, pattern) => {
    const matches = text.match(pattern);
    return total + (matches ? matches.length : 0);
  }, 0);
}

function bodyMetrics(body) {
  const lines = body.split('\n');
  const nonEmptyLines = lines.filter((line) => line.trim().length > 0);
  const bulletLines = lines.filter((line) => /^\s*(?:[-*]|\d+\.)\s+/.test(line));

  return {
    chars: body.length,
    lines: nonEmptyLines.length,
    bulletLines: bulletLines.length,
    imperativeCount: countMatches(IMPERATIVE_PATTERNS, body),
    exampleCount: countMatches(EXAMPLE_PATTERNS, body),
  };
}

export function classifyPrompt(prompt) {
  const category = promptCategory(prompt.name);
  const metrics = bodyMetrics(prompt.body);
  const tokens = prompt.tokens || 0;
  const reasons = [];
  const actions = [];
  let priority = 0;

  if (tokens >= 10_000) {
    priority += 5;
    reasons.push('very large token footprint');
  } else if (tokens >= 4_000) {
    priority += 4;
    reasons.push('large token footprint');
  } else if (tokens >= 1_000) {
    priority += 2;
    reasons.push('moderate token footprint');
  }

  if (metrics.imperativeCount >= 40) {
    priority += 2;
    reasons.push('many imperative rules');
  } else if (metrics.imperativeCount >= 15) {
    priority += 1;
    reasons.push('rule-heavy wording');
  }

  if (metrics.exampleCount >= 8) {
    priority += 1;
    reasons.push('example-heavy content');
  }

  if (metrics.bulletLines >= 40) {
    priority += 1;
    reasons.push('long checklist shape');
  }

  if (category === 'data') {
    priority += tokens >= 1_000 ? 2 : 0;
    actions.push('move reference material behind retrieval or an explicit help/docs command');
  } else if (category === 'skill' || category === 'agent') {
    actions.push('keep a short trigger and load step-specific guidance only after invocation');
  } else if (category === 'tool') {
    actions.push('replace prose rules with clearer tool schema, validation, and concise errors');
  } else if (category === 'system' || category === 'reminder') {
    actions.push('keep only global invariants in the prompt and move situational policy to runtime state');
  }

  if (metrics.exampleCount > 0) {
    actions.push('collapse examples into one canonical positive case plus one failure case');
  }
  if (metrics.imperativeCount > 0) {
    actions.push('deduplicate repeated must/never/always rules into a smaller contract');
  }

  return {
    ...prompt,
    category,
    metrics,
    priority,
    reasons,
    actions: [...new Set(actions)],
  };
}

export function analyzePrompts({ promptsDir, readmePath, limit = 30 }) {
  const readme = readFileSync(readmePath, 'utf8');
  const tokenCounts = parseReadmeTokenCounts(readme);
  const prompts = [];

  for (const filename of readdirSync(promptsDir).filter((file) => file.endsWith('.md'))) {
    const content = readFileSync(join(promptsDir, filename), 'utf8');
    const parsed = parsePromptMarkdown(content);
    const tokenEntry = tokenCounts.get(filename);
    prompts.push(
      classifyPrompt({
        filename,
        name: parsed.name || tokenEntry?.name || filename,
        description: parsed.description || '',
        body: parsed.body,
        tokens: tokenEntry?.tokens || 0,
      })
    );
  }

  const candidates = prompts
    .filter((prompt) => prompt.priority > 0)
    .sort((left, right) => right.priority - left.priority || right.tokens - left.tokens)
    .slice(0, limit);

  return {
    promptCount: prompts.length,
    totalTokens: prompts.reduce((sum, prompt) => sum + prompt.tokens, 0),
    categoryTotals: categoryTotals(prompts),
    candidates,
  };
}

function categoryTotals(prompts) {
  const totals = new Map();
  for (const prompt of prompts) {
    const current = totals.get(prompt.category) || { count: 0, tokens: 0 };
    current.count += 1;
    current.tokens += prompt.tokens;
    totals.set(prompt.category, current);
  }
  return [...totals.entries()]
    .map(([category, value]) => ({ category, ...value }))
    .sort((left, right) => right.tokens - left.tokens);
}

export function renderSlimmingReport(analysis) {
  const lines = [
    '# Prompt Slimming Candidates',
    '',
    `Prompts analyzed: ${analysis.promptCount}`,
    `README token total: ${analysis.totalTokens.toLocaleString()} tokens`,
    '',
    '## Token Totals By Category',
    '',
    '| Category | Prompts | Tokens |',
    '| --- | ---: | ---: |',
  ];

  for (const total of analysis.categoryTotals) {
    lines.push(
      `| ${total.category} | ${total.count} | ${total.tokens.toLocaleString()} |`
    );
  }

  lines.push('', '## Highest Priority Candidates', '');

  for (const [index, prompt] of analysis.candidates.entries()) {
    lines.push(
      `${index + 1}. ${prompt.name} (${prompt.tokens.toLocaleString()} tokens, ${prompt.filename})`
    );
    lines.push(`   - Category: ${prompt.category}`);
    lines.push(`   - Why: ${prompt.reasons.join('; ') || 'low structural signal'}`);
    lines.push(`   - Suggested cut: ${prompt.actions.join('; ')}`);
  }

  lines.push('');
  return `${lines.join('\n')}\n`;
}
