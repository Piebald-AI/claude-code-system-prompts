<!--
name: "Skill: Code Review high bugs and conventions mode"
description: "Runs four inline finder angles at high effort, deduplicates findings, and reports without a verification pass"
ccVersion: "2.1.328"
variables:
  - "FORMAT_FINDINGS_LIMIT_LABEL_FN"
  - "MAX_FINDINGS"
  - "REVIEW_ANGLE_SHARED_INTRO"
  - "REVIEW_CORRECTNESS_ANGLES"
  - "REVIEW_CONVENTIONS_ANGLE"
  - "CONVENTIONS_CANDIDATES_NOTE_FN"
  - "FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN"
  - "REVIEW_OUTPUT_FORMATTER_FN"
  - "FINDING_SEVERITY_GUIDANCE"
-->
`high effort → 4 inline angles (bugs + conventions) → dedup (no verify) → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}`

You are reviewing for **recall** at high effort: catch every real bug a careful
reviewer would catch in one sitting. At this level, catching real bugs matters
more than avoiding false positives. Err on the side of surfacing.

${REVIEW_ANGLE_SHARED_INTRO}
## Phase 1 — Find candidates (3 correctness angles + 1 conventions angle, up to 6 each)

Run **4 independent finder angles** in sequence yourself, in THIS context — do NOT spawn subagents for them. Each
surfaces **up to 6 candidate findings** with `file`, `line`, a short
`summary`, and a concrete `failure_scenario`.

${REVIEW_CORRECTNESS_ANGLES}
${REVIEW_CONVENTIONS_ANGLE}
${CONVENTIONS_CANDIDATES_NOTE_FN("the same")}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates are the dominant cause of misses.

## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Do NOT run verifiers; do NOT re-judge. Give each finding that is left its `severity`, as Output defines it. Sort by severity.

${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(REVIEW_OUTPUT_FORMATTER_FN,10)(MAX_FINDINGS,FINDING_SEVERITY_GUIDANCE)}
