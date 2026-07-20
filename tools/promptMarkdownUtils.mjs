const PROMPT_NAME_PREFIXES = [
  ['Agent Prompt: ', 'agent-prompt-'],
  ['System Prompt: ', 'system-prompt-'],
  ['System Reminder: ', 'system-reminder-'],
  ['Tool Description: ', 'tool-description-'],
  ['Tool Parameter: ', 'tool-parameter-'],
  ['Data: ', 'data-'],
  ['Skill: ', 'skill-'],
];

/**
 * Convert a prompt name to its canonical generated Markdown filename.
 */
export function nameToFilename(name) {
  const stringName = String(name);
  const category = PROMPT_NAME_PREFIXES.find(([namePrefix]) =>
    stringName.startsWith(namePrefix)
  );
  const [namePrefix, filenamePrefix] = category || ['', ''];
  const slug = stringName
    .slice(namePrefix.length)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-+|-+$/g, '');

  return `${filenamePrefix}${slug}.md`;
}

/**
 * Serialize a string as a deterministic YAML-compatible double-quoted scalar.
 */
export function yamlString(value) {
  const stringValue = String(value);
  if (stringValue.includes('-->')) {
    throw new Error('Frontmatter strings cannot contain the HTML comment terminator "-->"');
  }
  return JSON.stringify(stringValue);
}

/**
 * Parse string scalars emitted by this generator, including its legacy single quotes.
 */
export function parseYamlString(value) {
  const scalar = String(value).trim();
  if (scalar.startsWith('"')) {
    return JSON.parse(scalar);
  }
  if (scalar.startsWith("'") && scalar.endsWith("'")) {
    return scalar.slice(1, -1).replace(/''/g, "'");
  }
  return scalar;
}

/**
 * Decode JavaScript source escapes preserved by the prompt extractor.
 */
export function decodeSourceEscapes(value) {
  const text = String(value);
  let result = '';

  for (let i = 0; i < text.length; i++) {
    if (text[i] === '\\' && i + 1 < text.length) {
      const next = text[i + 1];
      if (next === '`' || next === '"' || next === "'" || next === '$') {
        result += next;
        i++;
      } else if (next === '\\') {
        result += '\\';
        i++;
      } else {
        result += text[i];
      }
    } else {
      result += text[i];
    }
  }

  return result;
}

/**
 * Reject filename collisions before generation can overwrite one prompt with another.
 */
export function assertUniquePromptFilenames(prompts) {
  const promptNamesByFilename = new Map();

  for (const prompt of prompts) {
    const filename = nameToFilename(prompt.name);
    const existingName = promptNamesByFilename.get(filename);
    if (existingName) {
      throw new Error(
        `Canonical filename collision for ${filename}: ${existingName} and ${prompt.name}`
      );
    }
    promptNamesByFilename.set(filename, prompt.name);
  }
}

/**
 * Render the HTML-comment frontmatter used by generated prompt Markdown files.
 */
export function renderPromptFrontmatter(prompt) {
  const lines = [
    '<!--',
    `name: ${yamlString(prompt.name)}`,
    `description: ${yamlString(prompt.description)}`,
    `ccVersion: ${yamlString(prompt.version)}`,
  ];
  const variables = Object.values(prompt.identifierMap || {});

  if (variables.length > 0) {
    lines.push('variables:');
    for (const variable of variables) {
      lines.push(`  - ${yamlString(variable)}`);
    }
  }

  if (prompt.agentMetadata) {
    const metadata = prompt.agentMetadata;
    lines.push('agentMetadata:');

    for (const key of ['agentType', 'model', 'color', 'permissionMode']) {
      if (metadata[key] != null) {
        lines.push(`  ${key}: ${yamlString(metadata[key])}`);
      }
    }
    if (metadata.maxTurns != null) {
      lines.push(`  maxTurns: ${metadata.maxTurns}`);
    }
    if (metadata.whenToUseDynamic) {
      lines.push('  whenToUseDynamic: true');
    }
    if (Array.isArray(metadata.tools)) {
      lines.push('  tools:');
      for (const tool of metadata.tools) {
        lines.push(`    - ${yamlString(tool)}`);
      }
    } else if (metadata.tools != null) {
      lines.push(`  tools: ${yamlString(metadata.tools)}`);
    }
    if (metadata.toolsNote != null) {
      lines.push(`  toolsNote: ${yamlString(metadata.toolsNote)}`);
    }
    if (Array.isArray(metadata.disallowedTools)) {
      lines.push('  disallowedTools:');
      for (const tool of metadata.disallowedTools) {
        lines.push(`    - ${yamlString(tool)}`);
      }
    } else if (metadata.disallowedTools != null) {
      lines.push(`  disallowedTools: ${yamlString(metadata.disallowedTools)}`);
    }
    if (metadata.whenToUse != null) {
      lines.push(`  whenToUse: ${yamlString(metadata.whenToUse)}`);
    }
    if (metadata.criticalSystemReminder != null) {
      lines.push(
        `  criticalSystemReminder: ${yamlString(metadata.criticalSystemReminder)}`
      );
    }
  }

  lines.push('-->');
  return `${lines.join('\n')}\n`;
}
