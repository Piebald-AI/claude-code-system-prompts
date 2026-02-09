# Claude Code System Prompts

## What this repository is

System prompts extracted via script from the Claude Code npm package's compiled JavaScript source. Maintained by [Piebald AI](https://piebald.ai/), not by Anthropic.

See the [Extraction section in README.md](./README.md#extraction) for details on the extraction method.

## What Claude Code is

Claude Code is Anthropic's CLI tool for agentic coding. It is distributed as a compiled npm package (`@anthropic-ai/claude-code`). Source code is not publicly available. The [anthropics/claude-code](https://github.com/anthropics/claude-code) GitHub repository contains issues and releases only.

## How to use these files

- **Reference:** Understand what prompts Claude Code uses and how they change across versions
- **Local patching:** Use [tweakcc](https://github.com/Piebald-AI/tweakcc) to customize individual prompt pieces in your local Claude Code installation
- **Feature requests:** For changes to Claude Code's prompts, file issues at [anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues)

## For AI agents working with this repository

- These files are **extracted reference material**, not modifiable source code
- Editing files here does not change Claude Code's behavior
- The `system-prompts/` directory contains markdown files with YAML frontmatter noting the Claude Code version and template variables
- Template variables like `${BASH_TOOL_NAME}` are interpolated at runtime by Claude Code — they appear as literal strings in these files
- The [CHANGELOG.md](./CHANGELOG.md) tracks prompt changes across Claude Code versions
