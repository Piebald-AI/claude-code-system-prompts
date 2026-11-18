<!--
name: "Skill: Code Review extra-high bugs and conventions mode"
description: "Runs six inline finder angles at extra-high effort, deduplicates without verification, and sweeps for missed findings"
ccVersion: "2.1.328"
variables:
  - "FORMAT_FINDINGS_LIMIT_LABEL_FN"
  - "MAX_FINDINGS"
  - "REVIEW_ANGLE_SHARED_INTRO"
  - "REVIEW_CORRECTNESS_ANGLES"
  - "REVIEW_EXTRA_CORRECTNESS_ANGLES"
  - "REVIEW_CONVENTIONS_ANGLE"
  - "CONVENTIONS_CANDIDATES_NOTE_FN"
  - "REVIEW_GAP_SWEEP_INSTRUCTIONS"
  - "FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN"
  - "REVIEW_OUTPUT_FORMATTER_FN"
  - "FINDING_SEVERITY_GUIDANCE"
-->
`xhigh effort → 6 inline angles (bugs + conventions) → dedup (no verify) → sweep → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}`

You are reviewing for **recall** at extra-high effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives — a
missed bug ships. Err on the side of surfacing.

${REVIEW_ANGLE_SHARED_INTRO}
## Phase 1 — Find candidates (5 correctness angles + 1 conventions angle, up to 8 each)

Run **6 independent finder angles** in sequence yourself, in THIS context — do NOT spawn subagents for them. Each
surfaces **up to 8 candidate findings**. Do NOT let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both.

${REVIEW_CORRECTNESS_ANGLES}
${REVIEW_EXTRA_CORRECTNESS_ANGLES}
${REVIEW_CONVENTIONS_ANGLE}
${CONVENTIONS_CANDIDATES_NOTE_FN("the output's")}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates are the dominant cause of misses.

## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Do NOT run verifiers; do NOT re-judge. Sort by severity. Do NOT drop on uncertainty.

## Phase 3 — Sweep for gaps

${REVIEW_GAP_SWEEP_INSTRUCTIONS}
Then give each finding, the sweep's too, its `severity`, as Output defines it.

${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(REVIEW_OUTPUT_FORMATTER_FN,15)(MAX_FINDINGS,FINDING_SEVERITY_GUIDANCE)}
