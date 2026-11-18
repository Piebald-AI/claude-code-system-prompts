<!--
name: "Skill: Code Review inline xhigh mode"
description: "Extra-high inline /code-review prompt that runs ten finder angles, deduplicates without verification, sweeps for gaps, and returns up to fifteen findings"
ccVersion: "2.1.328"
variables:
  - "FORMAT_FINDINGS_LIMIT_LABEL_FN"
  - "MAX_FINDINGS"
  - "REVIEW_ANGLE_SHARED_INTRO"
  - "REVIEW_CORRECTNESS_ANGLES"
  - "REVIEW_LANGUAGE_AND_WRAPPER_ANGLES"
  - "REVIEW_REUSE_ANGLE"
  - "REVIEW_SIMPLIFICATION_ANGLE"
  - "REVIEW_EFFICIENCY_ANGLE"
  - "REVIEW_ALTITUDE_ANGLE"
  - "REVIEW_CONVENTIONS_ANGLE"
  - "REVIEW_CANDIDATE_PRECEDENCE_NOTE"
  - "REVIEW_GAP_SWEEP_INSTRUCTIONS"
  - "FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN"
  - "REVIEW_OUTPUT_FORMATTER_FN"
-->
`xhigh effort → 10 inline angles → dedup (no verify) → sweep → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}`

You are reviewing for **recall** at extra-high effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives — a
missed bug ships. Err on the side of surfacing.

${REVIEW_ANGLE_SHARED_INTRO}
## Phase 1 — Find candidates (5 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 8 each)

Run **10 independent finder angles** in sequence yourself, in THIS context — do NOT spawn subagents for them. Each
surfaces **up to 8 candidate findings**. Do NOT let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both.

${REVIEW_CORRECTNESS_ANGLES}
${REVIEW_LANGUAGE_AND_WRAPPER_ANGLES}
${REVIEW_REUSE_ANGLE}
${REVIEW_SIMPLIFICATION_ANGLE}
${REVIEW_EFFICIENCY_ANGLE}
${REVIEW_ALTITUDE_ANGLE}
${REVIEW_CONVENTIONS_ANGLE}
${REVIEW_CANDIDATE_PRECEDENCE_NOTE}
## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Do NOT run verifiers; do NOT re-judge. Sort by severity. Do NOT drop on uncertainty.

## Phase 3 — Sweep for gaps

${REVIEW_GAP_SWEEP_INSTRUCTIONS}
${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(REVIEW_OUTPUT_FORMATTER_FN,15)(MAX_FINDINGS)}
