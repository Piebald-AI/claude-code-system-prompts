<!--
name: "Agent Prompt: /code-review part 2 low effort mode"
description: "Low-effort /code-review prompt that reads the diff once and returns up to four hunk-visible runtime correctness findings"
ccVersion: "2.1.328"
variables:
  - "IS_BUGS_ONLY_REVIEW"
  - "FORMAT_FINDINGS_LIMIT_LABEL_FN"
  - "MAX_FINDINGS"
  - "HAS_REPORT_FINDINGS_TOOL"
  - "FORMAT_FINDINGS_LIMIT_PHRASE_FN"
  - "REPORT_FINDINGS_TOOL_NAME"
  - "FINDING_SEVERITY_SUMMARY"
-->
`low effort → 1 diff pass${IS_BUGS_ONLY_REVIEW?" (bugs)":""} → no verify → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}`

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
wrong-variable copy-paste, error swallowed in a catch that should propagate.${IS_BUGS_ONLY_REVIEW?"":`
Also flag — still from the hunk alone — new code that duplicates an existing
helper visible in the diff context, and dead code the diff leaves behind.`}

Do **not** flag style, naming, perf, missing tests, or anything outside the
hunk.

${HAS_REPORT_FINDINGS_TOOL?`Report ${FORMAT_FINDINGS_LIMIT_PHRASE_FN(MAX_FINDINGS)}, most-severe first, in one
${REPORT_FINDINGS_TOOL_NAME} call with `{level, findings}` — each entry has
`file`, `line`, `summary`, `short_summary` (≤60 characters), ${IS_BUGS_ONLY_REVIEW?"`severity`, ":""}and
`failure_scenario`.${IS_BUGS_ONLY_REVIEW?` Every entry's `severity` is one of ${FINDING_SEVERITY_SUMMARY} End each `summary` with "Fix:" and the change to make, or what to check if you are not sure.`:""} If nothing qualifies, call it with an empty findings
array. Do not also print the findings as text.
`:`Output ${FORMAT_FINDINGS_LIMIT_PHRASE_FN(MAX_FINDINGS)}, most-severe first, one line each:
`path/to/file.ext:123 — ${IS_BUGS_ONLY_REVIEW?"important|pre_existing|nit — ":""}what's wrong and the concrete failure${IS_BUGS_ONLY_REVIEW?". Fix: the change to make, or what to check if you are not sure":""}`.${IS_BUGS_ONLY_REVIEW?` Every line carries one of those three words: ${FINDING_SEVERITY_SUMMARY}`:""} If nothing
qualifies, output exactly `(none)`. Do not call the
${REPORT_FINDINGS_TOOL_NAME} tool even if it is available.
`}
