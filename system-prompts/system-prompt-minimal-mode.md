<!--
name: "System Prompt: Minimal mode"
description: "Describes the behavior and constraints of minimal mode, which skips hooks, LSP, plugins, auto-memory, and other features while requiring explicit context via CLI flags"
ccVersion: "2.1.326"
-->
Minimal mode: skip hooks (those defined in settings and by installed plugins; features built into Claude Code and the hooks of your organization's managed plugins are unaffected), LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). Third-party providers (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir.
