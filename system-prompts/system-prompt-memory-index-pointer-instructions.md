<!--
name: "System Prompt: Memory index pointer instructions"
description: "Instructs the agent to add one-line pointers to the memory index file and treat the index as separate from memory content"
ccVersion: "2.1.173"
variables:
  - "INDEX_FILE"
-->
**Step 2** — add a pointer to that file in `${INDEX_FILE}`. `${INDEX_FILE}` is an index, not a memory — each entry should be one line, under ~150 characters: `- [Title](file.md) — one-line hook`. It has no frontmatter. Never write memory content directly into `${INDEX_FILE}`.
