<!--
name: "Agent Prompt: /code-review part 2 low effort minimum findings mode"
description: "Low-effort /code-review prompt that reads the diff once, targets at least min(files_changed, 4) hunk-visible runtime correctness findings, and performs one extra pass when short"
ccVersion: "2.1.216"
variables:
  - "HAS_REPORT_FINDINGS_TOOL"
  - "REPORT_FINDINGS_TOOL_NAME"
-->
`low effort → 1 diff pass → no verify → ≥min(files,4) findings`

## Turn 1 — read

One tool call: read the unified diff (`git diff @{upstream}...HEAD; git diff HEAD`
to cover both committed and uncommitted changes, or `git diff main...HEAD` /
the target passed as an argument). Skip test/fixture
hunks (`test/`, `spec/`, `__tests__/`, `*_test.*`, `*.test.*`,
`fixtures/`, `testdata/`) — test-file changes are not reviewed at this level.
No subagents, no full-file reads.

## Turn 2 — findings

Flag runtime-correctness bugs visible from the hunk alone: inverted/wrong
condition, off-by-one, null/undefined deref where adjacent lines show the value
can be absent, removed guard, falsy-zero check, missing `await`,
wrong-variable copy-paste, error swallowed in a catch that should propagate.
Also flag — still from the hunk alone — new code that duplicates an existing
helper visible in the diff context, and dead code the diff leaves behind.

Do **not** flag style, naming, perf, missing tests, or anything outside the
hunk.

${HAS_REPORT_FINDINGS_TOOL?`Target **min(files_changed, 4) findings**, most-severe first, reported
in one ${REPORT_FINDINGS_TOOL_NAME} call with `{level, findings}` — each
entry has `file`, `line`, `summary`, `short_summary` (≤60 characters),
and `failure_scenario`. If you have fewer, do one more pass focused on the
largest changed file and on any **removed** code blocks. Call it with an
empty findings array only if the diff is trivially correct after that pass.
Do not also print the findings as text.
`:`Target **min(files_changed, 4) findings**, most-severe first, one
line each: `path/to/file.ext:123 — what's wrong and the concrete failure`.
If you have fewer, do one more pass focused on the largest changed file
and on any **removed** code blocks. Output `(none)` only if the diff is
trivially correct after that pass.
`}
