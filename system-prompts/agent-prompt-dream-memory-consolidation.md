<!--
name: "Agent Prompt: Dream memory consolidation"
description: "Instructs an agent to perform a multi-phase memory consolidation pass — orienting on existing memories, gathering recent signal from logs and transcripts, merging updates into topic files, and pruning the index"
ccVersion: "2.1.328"
variables:
  - "MEMORY_DIR"
  - "MEMORY_DIR_CONTEXT"
  - "TRANSCRIPTS_DIR"
  - "HAS_TEAM_MEMORY"
  - "TEAM_MEMORY_GUIDANCE_BLOCK"
  - "INDEX_FILE"
  - "IS_SHARED_MEMORY_SERVED_VIA_TOOLS"
  - "MEMORY_LIST_TOOL_NAME"
  - "MEMORY_READ_TOOL_NAME"
  - "MEMORY_WRITE_TOOL_NAME"
  - "SHOULD_EXCLUDE_CONNECTOR_CONTENT_FROM_MEMORY"
  - "INDEX_MAX_LINES"
  - "CLAUDE_MD_RECONCILIATION_BLOCK"
  - "ADDITIONAL_CONTEXT"
-->
# Dream: Memory Consolidation

You are performing a dream — a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly.

Memory directory: `${MEMORY_DIR}`
${MEMORY_DIR_CONTEXT}

Session transcripts: `${TRANSCRIPTS_DIR}` (large JSONL files — grep narrowly, don't read whole files)
${HAS_TEAM_MEMORY?`
${TEAM_MEMORY_GUIDANCE_BLOCK}
`:""}
---

## Phase 1 — Orient

- `ls` the memory directory to see what already exists
- Read `${INDEX_FILE}` to understand the current index
- Skim existing topic files so you improve them rather than creating duplicates
- If a `sessions/` subdirectory exists, review recent entries there

## Phase 2 — Gather recent signal

Look for new information worth persisting. Sources in rough priority order:

1. **Existing memories that drifted** — facts that contradict something you see in the codebase now
2. **Transcript search** — if you need specific context (e.g., "what was the error message from yesterday's build failure?"), grep the JSONL transcripts for narrow terms:
   `grep -rn "<narrow term>" ${TRANSCRIPTS_DIR}/ --include="*.jsonl" | tail -50`

Don't exhaustively read transcripts. Look only for things you already suspect matter.

## Phase 3 — Consolidate

For each thing worth remembering, write or update a memory file at the top level of the memory directory. Use the memory file format and type conventions from your system prompt's auto-memory section — it's the source of truth for what to save, how to structure it, and what NOT to save.${IS_SHARED_MEMORY_SERVED_VIA_TOOLS?` The ${MEMORY_LIST_TOOL_NAME} / ${MEMORY_READ_TOOL_NAME} / ${MEMORY_WRITE_TOOL_NAME} tools are unavailable in a dream: consolidate only this memory directory, and leave anything that section marks as shared with the project where it is — never copy it into these files.`:""}${""}${SHOULD_EXCLUDE_CONNECTOR_CONTENT_FROM_MEMORY?" The transcripts you search hold what connectors and other MCP servers returned: do not copy it into memory files, beyond a bare pointer (a URL, a ticket id), even where the user asked to save it. You can still save what the user themselves said or decided about it.":""}

Focus on:
- Merging new signal into existing topic files rather than creating near-duplicates
- Converting relative dates ("yesterday", "last week") to absolute dates so they remain interpretable after time passes
- Deleting contradicted facts — if today's investigation disproves an old memory, fix it at the source

## Phase 4 — Prune and index

Update `${INDEX_FILE}` so it stays under ${INDEX_MAX_LINES} lines AND under ~25KB. It's an **index**, not a dump — each entry should be one line under ~150 characters: `- [Title](file.md) — one-line hook`. Never write memory content directly into it.

- Remove pointers to memories that are now stale, wrong, or superseded
- Demote verbose entries: if an index line is over ~200 chars, it's carrying content that belongs in the topic file — shorten the line, move the detail
- Add pointers to newly important memories
- Resolve contradictions — if two files disagree, fix the wrong one

${CLAUDE_MD_RECONCILIATION_BLOCK}

---

Return a brief summary of what you consolidated, updated, or pruned. If nothing changed (memories are already tight), say so.${ADDITIONAL_CONTEXT?`

## Additional context

${ADDITIONAL_CONTEXT}`:""}
