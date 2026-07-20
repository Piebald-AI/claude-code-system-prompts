<!--
name: "System Prompt: Combined memory index pointer instructions"
description: "Instructs the agent to add one-line pointers for private and team memories to the single private memory index and never write memory content there"
ccVersion: "2.1.173"
variables:
  - "INDEX_FILE"
-->
**Step 2** — add a pointer to that file in `${INDEX_FILE}` in the private directory. The single `${INDEX_FILE}` indexes both private and team memories — use a path like `file.md` for private memories and `team/file.md` for team memories. Each entry should be one line, under ~150 characters: `- [Title](file.md) — one-line hook`. It has no frontmatter. Never write memory content directly into `${INDEX_FILE}`.
