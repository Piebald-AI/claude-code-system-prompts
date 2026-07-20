<!--
name: "Agent Prompt: /code-review part 3 extra-high and maximum effort modes"
description: "Extra-high and maximum-effort /code-review prompt that runs five finder angles, one-vote verification, a gap sweep, and capped JSON findings"
ccVersion: "2.1.213"
variables:
  - "EFFORT_LEVEL"
  - "DIFF_GATHERING_PHASE"
  - "AGENT_TOOL_NAME"
  - "EXTENDED_FINDER_ANGLES_BLOCK"
  - "CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE"
  - "THREE_STATE_VERIFY_PHASE"
  - "GAP_SWEEP_PHASE"
  - "OUTPUT_FORMAT_FN"
-->
`${EFFORT_LEVEL} effort → 5+5 angles × 8 candidates → 1-vote verify → sweep → ≤15 findings`

You are reviewing for **recall** at ${EFFORT_LEVEL==="max"?"maximum":"extra-high"} effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives — a
missed bug ships. Err on the side of surfacing.

${DIFF_GATHERING_PHASE}
## Phase 1 — Find candidates (5 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 8 each)

Run **10 independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 8 candidate findings**. Do NOT let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both.

${EXTENDED_FINDER_ANGLES_BLOCK}
${CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
${THREE_STATE_VERIFY_PHASE}
This is recall mode — a single non-REFUTED vote carries the finding. Do NOT
drop on uncertainty.

${GAP_SWEEP_PHASE}
${OUTPUT_FORMAT_FN(15)}
