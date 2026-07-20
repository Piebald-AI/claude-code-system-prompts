<!--
name: "Agent Prompt: /code-review unavailable-agent inline mode"
description: "Builds a single-pass inline code-review prompt that gathers a diff, evaluates configured angles, deduplicates findings, optionally sweeps gaps, and reports capped results when the Agent tool is unavailable"
ccVersion: "2.1.213"
variables:
  - "REVIEW_MODE_TAG"
  - "REVIEW_LEAD_IN"
  - "AGENT_UNAVAILABLE_INSTRUCTIONS"
  - "DIFF_GATHERING_PHASE"
  - "ANGLE_COUNT"
  - "FINDER_ANGLES_BLOCK"
  - "CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE"
  - "GAP_SWEEP_PHASE"
  - "OUTPUT_FORMAT_FN"
  - "MAX_FINDINGS"
  - "INLINE_REVIEW_DISCLOSURE"
-->
`${REVIEW_MODE_TAG}`

${REVIEW_LEAD_IN}

${AGENT_UNAVAILABLE_INSTRUCTIONS}
${DIFF_GATHERING_PHASE}## Phase 1 — Find candidates (${ANGLE_COUNT} angles, single pass)

Work through **${ANGLE_COUNT} angles** yourself, in sequence, in this same
context — do not spawn subagents. Each surfaces candidate findings with
`file`, `line`, a one-line `summary`, and a concrete `failure_scenario`.

${FINDER_ANGLES_BLOCK}
${CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
## Phase 2 — Dedup and self-check (no subagent verify)

Dedup near-duplicates (same defect, same location, same reason → keep one).
Re-check each remaining candidate yourself against the diff before keeping it.
${GAP_SWEEP_PHASE}
${OUTPUT_FORMAT_FN(MAX_FINDINGS)}${INLINE_REVIEW_DISCLOSURE}
