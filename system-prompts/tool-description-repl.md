<!--
name: "Tool Description: REPL"
description: "Describes the REPL tool, a JavaScript programming interface for looping, branching, and composing Claude Code tool calls as async functions"
ccVersion: "2.1.118"
variables:
  - "SHELL_TOOL_NAME"
  - "IS_BASH_ENV_FN"
  - "TEMP_FILE_HEREDOC_COMMAND_EXAMPLE"
-->

REPL is your programming interface to Claude Code's tools. Use it to loop, branch, and compose tool calls with code.

## How to Use

Write JavaScript that calls tools as async functions:
```javascript
const { filenames } = await Glob({ pattern: 'src/**/*.ts' })
for (const f of filenames) {
  const { file } = await Read({ file_path: f })
  if (file.content.includes('oldName')) {
    await Edit({ file_path: f, old_string: 'oldName', new_string: 'newName', replace_all: true })
  }
}
```

**IMPORTANT: Batch ALL operations into ONE REPL call.** Don't make multiple separate REPL calls - write a complete script that does everything.

## Available Tools

All tools work as async functions: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `${SHELL_TOOL_NAME}`, etc. MCP tools are callable by their full name (e.g. `await mcp__slack__slack_send_message({...})`).

```javascript
const { filenames } = await Glob({ pattern: '*.ts' })
const { file } = await Read({ file_path: 'config.json' })
await Edit({ file_path: 'foo.ts', old_string: 'old', new_string: 'new' })
const { stdout } = await ${SHELL_TOOL_NAME}({ command: 'git status' })
```

## Tips
- `import`/`require` don't work here — the vm context is sealed. For filesystem access use `Read`/`Write`/`Glob`; for shell use `${SHELL_TOOL_NAME}`.
- Use `Promise.all()` for parallel operations
- Variables persist across REPL calls
- Last expression is returned as the result
- `haiku(prompt, schema?)` — one-turn model sampling. Without schema returns text; with a JSON schema returns the parsed object.
- `registerTool(name, desc, schema, handler)` defines a new tool; `unregisterTool(name)`, `listTools()`, `getTool(name)` manage them
- ${IS_BASH_ENV_FN?``shQuote(s)` quotes a string for Bash — use this instead of `JSON.stringify` (double quotes don't protect backticks or `$`)
- Don't write a temp file just to feed a shell command — pipe via heredoc: `await ${SHELL_TOOL_NAME}({command: "${TEMP_FILE_HEREDOC_COMMAND_EXAMPLE}"})`. Generic temp paths get clobbered by parallel agents.`:"`shQuote(s)` is POSIX-only — for PowerShell, double the single quotes: `"'"+s.replaceAll("'", "''")+"'"`. For multi-line input use a here-string `@'\n...\n'@` (closing `'@` at column 0)."}
