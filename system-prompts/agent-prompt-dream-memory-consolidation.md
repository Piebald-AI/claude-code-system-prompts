<!--
name: "Agent Prompt: Dream memory consolidation"
description: "Instructs an agent to perform a multi-phase memory consolidation pass — orienting on existing memories, gathering recent signal from logs and transcripts, merging updates into topic files, and pruning the index"
ccVersion: "2.1.212"
variables:
  - "MEMORY_DIR"
  - "MEMORY_DIR_CONTEXT"
  - "TRANSCRIPTS_DIR"
  - "HAS_TRANSCRIPT_SOURCE_NOTE"
  - "TRANSCRIPT_SOURCE_NOTE"
  - "INDEX_FILE"
  - "POST_GATHER_FN"
  - "IS_STONE_SHELL_MEMORY_VARIANT"
  - "INDEX_MAX_LINES"
  - "CLAUDE_MD_RECONCILIATION_BLOCK"
  - "ADDITIONAL_DREAM_GUIDANCE_FN"
  - "ADDITIONAL_CONTEXT"
-->
# Dream: Memory Consolidation

You are performing a dream — a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly.

Memory directory: `${MEMORY_DIR}`
${MEMORY_DIR_CONTEXT}

Session transcripts: `${TRANSCRIPTS_DIR}` (large JSONL files — grep narrowly, don't read whole files)
${HAS_TRANSCRIPT_SOURCE_NOTE?`
${TRANSCRIPT_SOURCE_NOTE}
`:""}
---

## Phase 1 — Orient

- `ls` the memory directory to see what already exists
- Read `${INDEX_FILE}` to understand the current index
- Skim existing topic files so you improve them rather than creating duplicates
- `ls -R logs/` — recent activity logs (one file per session under `YYYY/MM/DD/`). If a `sessions/` subdirectory also exists, review recent entries there too

## Phase 2 — Gather recent signal

Look for new information worth persisting. Sources in rough priority order:

1. **Session logs** (`logs/YYYY/MM/DD/<id>-<title>.md`) — the append-only activity stream, one file per session. Read the most recent 1–3 days of sessions (the filename title tells you what each was about); each line is prefix-coded (`>` user, `<` assistant, `.` tool call)
2. **Existing memories that drifted** — facts that contradict something you see in the codebase now
3. **Transcript search** — if you need specific context (e.g., "what was the error message from yesterday's build failure?"), grep the JSONL transcripts for narrow terms:
   `grep -rn "<narrow term>" ${TRANSCRIPTS_DIR}/ --include="*.jsonl" | tail -50`

Don't exhaustively read transcripts. Look only for things you already suspect matter.
${POST_GATHER_FN(IS_STONE_SHELL_MEMORY_VARIANT)}
## Phase 3 — Consolidate

For each thing worth remembering, write or update a memory file at the top level of the memory directory. Use the memory file format${IS_STONE_SHELL_MEMORY_VARIANT?"":" and type conventions"} from your system prompt's auto-memory section — it's the source of truth for what to save, how to structure it, and what NOT to save.

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
${ADDITIONAL_DREAM_GUIDANCE_FN()}
---

Return a brief summary of what you consolidated, updated, or pruned. If nothing changed (memories are already tight), say so.${ADDITIONAL_CONTEXT?`

## Additional context

${ADDITIONAL_CONTEXT}`:""}
