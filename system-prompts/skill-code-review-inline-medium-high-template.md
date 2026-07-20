<!--
name: "Skill: Code Review inline medium/high template"
description: "Template for medium and high inline code-review prompts that run eight finder angles, deduplicate without verification, and enforce a minimum findings target"
ccVersion: "2.1.206"
variables:
  - "REVIEW_EFFORT_SUMMARY"
  - "REVIEW_EFFORT_INTRO"
  - "REVIEW_ANGLE_SHARED_INTRO"
  - "REVIEW_CORRECTNESS_ANGLES"
  - "REVIEW_REUSE_ANGLE"
  - "REVIEW_SIMPLIFICATION_ANGLE"
  - "REVIEW_EFFICIENCY_ANGLE"
  - "REVIEW_ALTITUDE_ANGLE"
  - "REVIEW_CONVENTIONS_ANGLE"
  - "REVIEW_CANDIDATE_PRECEDENCE_NOTE"
  - "FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN"
  - "REVIEW_OUTPUT_FORMATTER_FN"
  - "MAX_FINDINGS"
-->
`${REVIEW_EFFORT_SUMMARY}`

${REVIEW_EFFORT_INTRO}

${REVIEW_ANGLE_SHARED_INTRO}
## Phase 1 — Find candidates (3 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 6 each)

Run **8 independent finder angles** in sequence yourself, in THIS context — do NOT spawn subagents for them. Each
surfaces **up to 6 candidate findings** with `file`, `line`, a one-line
`summary`, and a concrete `failure_scenario`.

${REVIEW_CORRECTNESS_ANGLES}
${REVIEW_REUSE_ANGLE}
${REVIEW_SIMPLIFICATION_ANGLE}
${REVIEW_EFFICIENCY_ANGLE}
${REVIEW_ALTITUDE_ANGLE}
${REVIEW_CONVENTIONS_ANGLE}
${REVIEW_CANDIDATE_PRECEDENCE_NOTE}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates are the dominant cause of misses.

## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Do NOT run verifiers; do NOT re-judge. Sort by severity.

${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(REVIEW_OUTPUT_FORMATTER_FN)(MAX_FINDINGS)}
