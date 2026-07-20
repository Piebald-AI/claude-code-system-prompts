import { readFileSync as readFileSyncOrig, writeFileSync as writeFileSyncOrig, readdirSync, unlinkSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import {
  assertUniquePromptFilenames,
  decodeSourceEscapes,
  nameToFilename,
  parseYamlString,
  renderPromptFrontmatter,
} from './promptMarkdownUtils.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = join(__dirname, '..');
const SYSTEM_PROMPTS_DIR = join(ROOT_DIR, 'system-prompts');
const README_PATH = join(ROOT_DIR, 'README.md');

// Ensure system-prompts directory exists
if (!existsSync(SYSTEM_PROMPTS_DIR)) {
  mkdirSync(SYSTEM_PROMPTS_DIR, { recursive: true });
}

// Get API key from environment
const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
if (!ANTHROPIC_API_KEY) {
  console.error('Error: ANTHROPIC_API_KEY environment variable is required');
  console.error('Set it with: export ANTHROPIC_API_KEY=your-api-key');
  process.exit(1);
}

const isWindows = process.platform === 'win32';

const readFileSync = (file) => {
  const content = readFileSyncOrig(file, 'utf-8');
  return isWindows ? content.replace(/\r\n/g, "\n") : content;
};

const writeFileSync = (file, content) => {
  const output = isWindows ? content.replace(/\n/g, "\r\n") : content;
  writeFileSyncOrig(file, output);
};

/**
 * Count tokens using Anthropic's token counting API
 */
async function countTokens(text) {
  const response = await fetch('https://api.anthropic.com/v1/messages/count_tokens', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'anthropic-version': '2023-06-01',
      'x-api-key': ANTHROPIC_API_KEY
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5-20250929',
      messages: [
        {
          role: 'user',
          content: text
        }
      ]
    })
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Token counting API error: ${response.status} ${error}`);
  }

  const data = await response.json();
  return data.input_tokens;
}

/**
 * Fetch release date from npm for a specific version
 */
async function getNpmReleaseDate(version) {
  try {
    const response = await fetch('https://registry.npmjs.org/@anthropic-ai/claude-code');
    if (!response.ok) {
      console.warn(`Warning: Could not fetch npm package data`);
      return null;
    }
    const data = await response.json();
    const timestamp = data.time && data.time[version];
    if (!timestamp) {
      console.warn(`Warning: No release date found for v${version}`);
      return null;
    }
    // Parse the date and format it nicely
    const date = new Date(timestamp);
    return date.toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    }).replace(/(\d+)/, (match) => {
      // Add ordinal suffix (1st, 2nd, 3rd, etc.)
      const n = parseInt(match);
      const s = ['th', 'st', 'nd', 'rd'];
      const v = n % 100;
      return n + (s[(v - 20) % 10] || s[v] || s[0]);
    });
  } catch (err) {
    console.warn(`Warning: Error fetching npm release date: ${err.message}`);
    return null;
  }
}

/**
 * Batch count tokens for multiple prompts with rate limiting
 */
async function countTokensBatch(prompts, batchSize = 5, delayMs = 100) {
  const results = new Map();

  for (let i = 0; i < prompts.length; i += batchSize) {
    const batch = prompts.slice(i, i + batchSize);
    const promises = batch.map(async ({ filename, content }) => {
      try {
        const tokens = await countTokens(content);
        return { filename, tokens };
      } catch (err) {
        throw new Error(`Error counting tokens for ${filename}: ${err.message}`, { cause: err });
      }
    });

    const batchResults = await Promise.all(promises);
    batchResults.forEach(({ filename, tokens }) => {
      results.set(filename, tokens);
    });

    // Rate limiting delay between batches
    if (i + batchSize < prompts.length) {
      await new Promise(resolve => setTimeout(resolve, delayMs));
    }
  }

  return results;
}

/**
 * Reconstruct the full prompt content from pieces and identifiers
 */
function reconstructPrompt(prompt) {
  if (prompt.pieces.length === 0) return '';
  if (prompt.pieces.length === 1) return decodeSourceEscapes(prompt.pieces[0]);

  let result = '';
  let identifierIndex = 0;

  for (let i = 0; i < prompt.pieces.length; i++) {
    result += prompt.pieces[i];

    // Add variable name (pieces already contain ${ and } delimiters)
    if (i < prompt.pieces.length - 1 && identifierIndex < prompt.identifiers.length) {
      const identifierId = prompt.identifiers[identifierIndex].toString();
      const variableName = prompt.identifierMap[identifierId];
      if (variableName) {
        result += variableName;
      }
      identifierIndex++;
    }
  }

  return decodeSourceEscapes(result);
}

/**
 * Create markdown file content with HTML comment metadata
 */
function createMarkdownContent(prompt, reconstructedContent) {
  let content = renderPromptFrontmatter(prompt);
  content += reconstructedContent;

  // Ensure file ends with newline
  if (!content.endsWith('\n')) {
    content += '\n';
  }

  return content;
}

/**
 * Parse existing markdown file to extract metadata
 */
function parseMarkdownFile(filepath) {
  try {
    const content = readFileSync(filepath);
    const commentMatch = content.match(/<!--\n([\s\S]*?)\n-->/);
    if (!commentMatch) return null;

    const metadataSection = commentMatch[1];
    const nameMatch = metadataSection.match(/^name:\s*(.+)$/m);
    const descMatch = metadataSection.match(/description: (.+?)(?=\nccVersion:)/s);

    return {
      name: nameMatch ? parseYamlString(nameMatch[1]) : null,
      description: descMatch ? descMatch[1].replace(/>\n\s+/g, '').trim() : null,
      body: content.slice(commentMatch.index + commentMatch[0].length),
      fullContent: content
    };
  } catch (err) {
    return null;
  }
}

/**
 * Categorize prompts based on their name
 */
function categorizePrompt(name) {
  if (name.startsWith('Agent Prompt: ')) {
    const namePart = name.substring('Agent Prompt: '.length);
    // Sub-categorize agent prompts
    if (['Explore', 'Plan mode (enhanced)', 'Task tool'].some(sub => namePart.startsWith(sub))) {
      return { category: 'Agent Prompts', subcategory: 'Sub-agents' };
    } else if (['Agent creation architect', 'CLAUDE.md creation', 'Status line setup'].some(sub => namePart.includes(sub))) {
      return { category: 'Agent Prompts', subcategory: 'Creation Assistants' };
    } else if (namePart.includes('slash command') || namePart.startsWith('/')) {
      return { category: 'Agent Prompts', subcategory: 'Slash commands' };
    } else {
      return { category: 'Agent Prompts', subcategory: 'Utilities' };
    }
  } else if (name.startsWith('System Prompt: ')) {
    return { category: 'System Prompt', subcategory: null };
  } else if (name.startsWith('System Reminder: ')) {
    return { category: 'System Reminders', subcategory: null };
  } else if (name.startsWith('Tool Description: ')) {
    // Check for "additional notes" subcategory
    if (name.includes('(') && name.includes(')')) {
      return { category: 'Builtin Tool Descriptions', subcategory: 'Additional notes for some Tool Descriptions' };
    }
    return { category: 'Builtin Tool Descriptions', subcategory: null };
  } else if (name.startsWith('Data: ')) {
    return { category: 'Data', subcategory: null };
  } else if (name.startsWith('Skill: ')) {
    return { category: 'Skills', subcategory: null };
  } else if (name.startsWith('Tool Parameter: ')) {
    return { category: 'Builtin Tool Descriptions', subcategory: 'Additional notes for some Tool Descriptions' };
  }

  return { category: 'Other', subcategory: null };
}

/**
 * Update or create README entry for a prompt
 */
function createReadmeEntry(prompt, filename, tokens, isBold = false) {
  const link = isBold ? `[**${prompt.name}**]` : `[${prompt.name}]`;
  const path = `./system-prompts/${filename}`;
  const tokenCount = `(**${tokens}** tks)`;
  const description = prompt.description.replace(/\n\s+/g, ' ').trim().replace(/\.$/, '');

  return `- ${link}(${path}) ${tokenCount} - ${description}.`;
}

/**
 * Parse existing token counts from README
 */
function parseReadmeTokenCounts() {
  const tokenCounts = new Map();
  try {
    const readme = readFileSync(README_PATH);
    // Match name, filename, and token count so filename migrations retain counts.
    const regex = /- \[(?:\*\*)?([^\]]+?)(?:\*\*)?\]\(\.\/system-prompts\/([^)]+\.md)\)\s*\(\*\*(\d+)\*\*\s*tks\)/g;
    let match;
    while ((match = regex.exec(readme)) !== null) {
      const entry = { filename: match[2], tokens: parseInt(match[3], 10) };
      tokenCounts.set(match[2], entry);
      tokenCounts.set(match[1], entry);
    }
  } catch (err) {
    // README doesn't exist yet, that's fine
  }
  return tokenCounts;
}

/**
 * Main update function
 */
async function updateFromJSON(jsonPath) {
  console.log(`Reading JSON from: ${jsonPath}`);
  const jsonData = JSON.parse(readFileSync(jsonPath));

  console.log(`Version: ${jsonData.version}`);
  console.log(`Prompts count: ${jsonData.prompts.length}`);
  assertUniquePromptFilenames(jsonData.prompts);

  // Count version files in the same directory as the input JSON
  const jsonDir = dirname(jsonPath);
  const versionFiles = readdirSync(jsonDir).filter(f => f.match(/^prompts-[\d.]+\.json$/));
  const versionCount = versionFiles.length;

  // Get existing token counts from README
  const existingTokenCounts = parseReadmeTokenCounts();

  // Track all prompts by filename
  const promptsByFilename = new Map();
  const changedPrompts = new Set();
  const newPrompts = new Set();
  const promptsToCount = [];
  const unchangedPrompts = [];
  const existingFilesByPromptName = new Map();
  const existingFilesByBody = new Map();
  for (const existingFilename of readdirSync(SYSTEM_PROMPTS_DIR).filter(f => f.endsWith('.md'))) {
    const existingFile = parseMarkdownFile(join(SYSTEM_PROMPTS_DIR, existingFilename));
    if (existingFile?.name) {
      const entry = { filename: existingFilename, ...existingFile };
      existingFilesByPromptName.set(existingFile.name, entry);
      const bodyKey = existingFile.body.trim();
      existingFilesByBody.set(bodyKey, existingFilesByBody.has(bodyKey) ? null : entry);
    }
  }

  // First pass: Process files and identify what needs token counting
  for (const prompt of jsonData.prompts) {
    const filename = nameToFilename(prompt.name);
    const filepath = join(SYSTEM_PROMPTS_DIR, filename);
    const reconstructedContent = reconstructPrompt(prompt);
    const newMarkdownContent = createMarkdownContent(prompt, reconstructedContent);

    // Match by prompt name as well as canonical path so filename migrations can
    // retain token counts and distinguish metadata-only rewrites from body changes.
    const existingFile =
      parseMarkdownFile(filepath) ||
      existingFilesByPromptName.get(prompt.name) ||
      existingFilesByBody.get(reconstructedContent.trim());
    const existingTokenEntry =
      existingTokenCounts.get(filename) ||
      existingTokenCounts.get(prompt.name) ||
      (existingFile && existingTokenCounts.get(existingFile.filename));
    const bodyChanged = existingFile && existingFile.body.trim() !== reconstructedContent.trim();

    if (existingFile) {
      if (existingFile.fullContent.trim() !== newMarkdownContent.trim()) {
        console.log(`\x1b[33mChanged: ${filename}\x1b[0m`);
        writeFileSync(filepath, newMarkdownContent);
        changedPrompts.add(filename);
      }
      if (bodyChanged || !existingTokenEntry) {
        promptsToCount.push({ filename, content: reconstructedContent, prompt });
      } else {
        unchangedPrompts.push({ filename, prompt, tokens: existingTokenEntry.tokens });
      }
    } else {
      console.log(`\x1b[32mNew: ${filename}\x1b[0m`);
      writeFileSync(filepath, newMarkdownContent);
      newPrompts.add(filename);
      promptsToCount.push({ filename, content: reconstructedContent, prompt });
    }
  }

  // Only count tokens for new/changed prompts
  const tokenCounts = new Map();
  if (promptsToCount.length > 0) {
    console.log(`\x1b[34mCounting tokens for ${promptsToCount.length} new/changed prompts...\x1b[0m`);
    const newCounts = await countTokensBatch(promptsToCount);
    newCounts.forEach((tokens, filename) => tokenCounts.set(filename, tokens));
  }

  // Store prompt info for README updates
  for (const { filename, prompt } of promptsToCount) {
    const tokens = tokenCounts.get(filename) || 0;
    promptsByFilename.set(filename, { prompt, tokens });
  }

  // Use existing token counts for unchanged prompts
  for (const { filename, prompt, tokens } of unchangedPrompts) {
    promptsByFilename.set(filename, { prompt, tokens });
  }

  // Find deleted prompts
  const allMdFiles = readdirSync(SYSTEM_PROMPTS_DIR).filter(f => f.endsWith('.md'));
  const deletedFiles = allMdFiles.filter(f => !promptsByFilename.has(f));

  if (deletedFiles.length > 0) {
    console.log('\n🗑️  Deleting removed prompts:');
    deletedFiles.forEach(f => {
      console.log(`   - ${f}`);
      unlinkSync(join(SYSTEM_PROMPTS_DIR, f));
    });
  }

  // Fetch npm release date
  console.log('\x1b[34mFetching npm release date...\x1b[0m');
  const releaseDate = await getNpmReleaseDate(jsonData.version);

  // Update README
  console.log('\x1b[34mUpdating README.md...\x1b[0m');
  updateReadme(promptsByFilename, jsonData.version, releaseDate, versionCount);

  console.log('\x1b[32;1mUpdate complete!\x1b[0m');
  console.log(`   New: \x1b[1m${newPrompts.size}\x1b[0m`);
  console.log(`   Changed: \x1b[1m${changedPrompts.size}\x1b[0m`);
  console.log(`   Deleted: \x1b[1m${deletedFiles.length}\x1b[0m`);
}

/**
 * Update README.md with new prompt information
 */
function updateReadme(promptsByFilename, version, releaseDate, versionCount) {
  let readme = readFileSync(README_PATH);
  const lines = readme.split('\n');

  // Update version in header with npm link and date
  const npmUrl = `https://www.npmjs.com/package/@anthropic-ai/claude-code/v/${version}`;
  const dateStr = releaseDate ? ` (${releaseDate})` : '';

  // Find the intro line dynamically (it starts with "This repository contains")
  const introLineIndex = lines.findIndex(line => line.startsWith('This repository contains'));
  if (introLineIndex !== -1) {
    lines[introLineIndex] = `This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v${version}](${npmUrl})${dateStr}.**  It also contains a [**CHANGELOG.md**](./CHANGELOG.md) for the system prompts across ${versionCount} versions since v2.0.14.  From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)`;
  } else {
    console.warn('Warning: Could not find intro line starting with "This repository contains"');
  }
  // Organize prompts by category
  const categories = {
    'Agent Prompts': {
      'Sub-agents': [],
      'Creation Assistants': [],
      'Slash commands': [],
      'Utilities': []
    },
    'System Prompt': { 'main': [] },
    'System Reminders': { 'main': [] },
    'Builtin Tool Descriptions': {
      'main': [],
      'Additional notes for some Tool Descriptions': []
    },
    'Data': { 'main': [] },
    'Skills': { 'main': [] }
  };

  // Categorize all prompts
  for (const [filename, { prompt, tokens }] of promptsByFilename) {
    const { category, subcategory } = categorizePrompt(prompt.name);

    // Special handling for bold main system prompt
    const isBold = prompt.name === 'System Prompt: Main system prompt';
    const entry = createReadmeEntry(prompt, filename, tokens, isBold);

    if (category === 'Agent Prompts') {
      categories['Agent Prompts'][subcategory].push(entry);
    } else if (category === 'System Prompt') {
      categories['System Prompt']['main'].push(entry);
    } else if (category === 'System Reminders') {
      categories['System Reminders']['main'].push(entry);
    } else if (category === 'Builtin Tool Descriptions') {
      const subcat = subcategory || 'main';
      categories['Builtin Tool Descriptions'][subcat].push(entry);
    } else if (category === 'Data') {
      categories['Data']['main'].push(entry);
    } else if (category === 'Skills') {
      categories['Skills']['main'].push(entry);
    }
  }

  // Sort entries alphabetically within each category
  for (const category of Object.values(categories)) {
    for (const subcategory of Object.values(category)) {
      if (Array.isArray(subcategory)) {
        subcategory.sort();
      }
    }
  }

  // Rebuild README sections
  const newLines = [];
  let i = 0;

  // Copy everything up to "### Agent Prompts"
  while (i < lines.length && !lines[i].startsWith('### Agent Prompts')) {
    newLines.push(lines[i]);
    i++;
  }

  // Agent Prompts section
  newLines.push('### Agent Prompts');
  newLines.push('');
  newLines.push('Sub-agents and utilities.');
  newLines.push('');
  newLines.push('#### Sub-agents');
  newLines.push('');
  newLines.push(...categories['Agent Prompts']['Sub-agents']);
  newLines.push('');
  newLines.push('#### Creation Assistants');
  newLines.push('');
  newLines.push(...categories['Agent Prompts']['Creation Assistants']);
  newLines.push('');
  newLines.push('#### Slash Commands');
  newLines.push('');
  newLines.push(...categories['Agent Prompts']['Slash commands']);
  newLines.push('');
  newLines.push('#### Utilities');
  newLines.push('');
  newLines.push(...categories['Agent Prompts']['Utilities']);
  newLines.push('');

  // Data section (commented out if has entries)
  if (categories['Data']['main'].length > 0) {
    newLines.push('### Data');
    newLines.push('');
    newLines.push('The content of various template files embedded in Claude Code.');
    newLines.push('');
    newLines.push(...categories['Data']['main']);
    newLines.push('');
  }

  // System Prompt section
  newLines.push('### System Prompt');
  newLines.push('');
  newLines.push('Parts of the main system prompt.');
  newLines.push('');
  newLines.push(...categories['System Prompt']['main']);
  newLines.push('');

  // System Reminders section
  newLines.push('### System Reminders');
  newLines.push('');
  newLines.push('Text for large system reminders.');
  newLines.push('');
  newLines.push(...categories['System Reminders']['main']);
  newLines.push('');

  // Builtin Tool Descriptions section
  newLines.push('### Builtin Tool Descriptions');
  newLines.push('');
  newLines.push(...categories['Builtin Tool Descriptions']['main']);
  newLines.push('');
  newLines.push('**Additional notes for some Tool Descriptions**');
  newLines.push('');
  newLines.push(...categories['Builtin Tool Descriptions']['Additional notes for some Tool Descriptions']);
  newLines.push('');

  if (categories['Skills']['main'].length > 0) {
    newLines.push('### Skills');
    newLines.push('');
    newLines.push('Built-in skill prompts for specialized tasks.');
    newLines.push('');
    newLines.push(...categories['Skills']['main']);
    newLines.push('');
  }

  // Write updated README
  writeFileSync(README_PATH, newLines.join('\n'));
}

// Main execution
const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Usage: node updatePrompts.js <path-to-prompts.json>');
  console.error('Example: node updatePrompts.js /path/to/tweakcc/data/prompts/prompts-2.0.44.json');
  process.exit(1);
}

const jsonPath = args[0];
await updateFromJSON(jsonPath);
