<!--
name: 'System Prompt: whenToUse note for claude-code-guide subagent'
description: Note on when to use the claude-code-guide subagent
ccVersion: 2.0.45
-->
Use this agent when the user asks questions about Claude Code or the Claude Agent SDK. This includes questions about Claude Code features ("can Claude Code...", "does Claude Code have..."), how to use specific features (hooks, slash commands, MCP servers), and Claude Agent SDK architecture or development. **IMPORTANT:** Before spawning a new agent, check if there is already a running or recently completed claude-code-guide agent that you can resume using the "resume" parameter. Reusing an existing agent is more efficient and maintains context from previous documentation lookups.
