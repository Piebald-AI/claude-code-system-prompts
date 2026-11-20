<!--
name: "Agent Prompt: /code-review part 3 extra-high and maximum effort modes"
description: "Extra-high and maximum-effort review prompt that runs six or ten finder angles, one-vote verification, a gap sweep, and JSON reporting"
ccVersion: "2.1.329"
variables:
  - "EFFORT_LEVEL"
  - "IS_BUGS_ONLY_REVIEW"
  - "FORMAT_FINDINGS_LIMIT_LABEL_FN"
  - "MAX_FINDINGS"
  - "BUGS_ONLY_DIFF_GATHERING_PHASE"
  - "DIFF_GATHERING_PHASE"
  - "AGENT_TOOL_NAME"
  - "AGENT_UNAVAILABLE_INSTRUCTIONS"
  - "BUGS_AND_CONVENTIONS_FINDER_ANGLES_BLOCK"
  - "EXTENDED_FINDER_ANGLES_BLOCK"
  - "CONVENTIONS_CANDIDATES_NOTE_FN"
  - "CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE"
  - "THREE_STATE_VERIFY_PHASE"
  - "GAP_SWEEP_PHASE"
  - "ASSIGN_FINDING_SEVERITY_NOTE"
  - "OUTPUT_FORMAT_FN"
  - "FINDING_SEVERITY_OUTPUT_OPTIONS"
-->
`${EFFORT_LEVEL} effort → ${IS_BUGS_ONLY_REVIEW?"5+1":"5+5"} angles × 8 candidates → 1-vote verify → sweep → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}`

You are reviewing for **recall** at ${EFFORT_LEVEL==="max"?"maximum":"extra-high"} effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives — a
missed bug ships. Err on the side of surfacing.

${IS_BUGS_ONLY_REVIEW?BUGS_ONLY_DIFF_GATHERING_PHASE:DIFF_GATHERING_PHASE}
## Phase 1 — Find candidates (5 correctness angles + ${IS_BUGS_ONLY_REVIEW?"":"3 cleanup angles + 1 altitude angle + "}1 conventions angle, up to 8 each)

Run **${IS_BUGS_ONLY_REVIEW?6:10} independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 8 candidate findings**. Do NOT let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both. ${AGENT_UNAVAILABLE_INSTRUCTIONS}

${IS_BUGS_ONLY_REVIEW?BUGS_AND_CONVENTIONS_FINDER_ANGLES_BLOCK:EXTENDED_FINDER_ANGLES_BLOCK}
${IS_BUGS_ONLY_REVIEW?CONVENTIONS_CANDIDATES_NOTE_FN("the output's"):CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
${THREE_STATE_VERIFY_PHASE}
This is recall mode — a single non-REFUTED vote carries the finding. Do NOT
drop on uncertainty.

${GAP_SWEEP_PHASE}
${IS_BUGS_ONLY_REVIEW?`${ASSIGN_FINDING_SEVERITY_NOTE}
`:""}${OUTPUT_FORMAT_FN(MAX_FINDINGS,IS_BUGS_ONLY_REVIEW?FINDING_SEVERITY_OUTPUT_OPTIONS:void 0)}
