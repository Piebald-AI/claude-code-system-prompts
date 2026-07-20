<!--
name: "System Prompt: Team memory index pointer instructions"
description: "Instructs the agent to add one-line memory pointers to the appropriate team memory index file and never write memory content into the index"
ccVersion: "2.1.173"
variables:
  - "HAS_SINGLE_TEAM_MEMORY_DIRECTORY"
  - "TEAM_MEMORY_INDEX_LOCATION"
-->
**Step 2** — add a pointer to that file in ${HAS_SINGLE_TEAM_MEMORY_DIRECTORY?``${TEAM_MEMORY_INDEX_LOCATION}``:TEAM_MEMORY_INDEX_LOCATION}. Each entry should be one line, under ~150 characters: `- [Title](file.md) — one-line hook`. The index has no frontmatter. Never write memory content directly into the index.
