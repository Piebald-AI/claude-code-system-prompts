<!--
name: "Skill: Code Review low effort expanded-findings mode"
description: "Low-effort /code-review prompt that reads the diff once, returns up to eight hunk-visible findings, and targets at least min(files_changed, 4) genuine findings"
ccVersion: "2.1.216"
variables:
  - "HAS_REPORT_FINDINGS_TOOL"
  - "REPORT_FINDINGS_TOOL_NAME"
-->
`low effort → 1 diff pass → no verify → ≤8 findings`

## Turn 1 — read

One tool call: read the unified diff (`git diff @{upstream}...HEAD; git diff HEAD`
to cover both committed and uncommitted changes, or `git diff main...HEAD` /
the target passed as an argument). No subagents, no full-file reads.

## Turn 2 — findings

Flag runtime-correctness bugs visible from the hunk alone: inverted/wrong
condition, off-by-one, null/undefined deref where adjacent lines show the value
can be absent, removed guard, falsy-zero check, missing `await`,
wrong-variable copy-paste, error swallowed in a catch that should propagate.
Also flag — still from the hunk alone — new code that duplicates an existing
helper visible in the diff context, and dead code the diff leaves behind.

Do **not** flag style, naming, perf, missing tests, or anything outside the
hunk.

${HAS_REPORT_FINDINGS_TOOL?`Report at most **8 findings**, most-severe first, in one
${REPORT_FINDINGS_TOOL_NAME} call with `{level, findings}` — each entry has
`file`, `line`, `summary`, `short_summary` (≤60 characters), and
`failure_scenario`.
Target at least min(files_changed, 4) findings — if you see fewer, widen to other hunks in the same diff before stopping. If fewer than 4 genuine findings exist, report what you have. Do not also print the findings as text.
`:`Output at most **8 findings**, most-severe first, one line each:
`path/to/file.ext:123 — what's wrong and the concrete failure`.
Target at least min(files_changed, 4) findings — if you see fewer, widen to other hunks in the same diff before stopping. If fewer than 4 genuine findings exist, emit what you have.
`}
