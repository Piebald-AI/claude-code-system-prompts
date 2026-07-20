<!--
name: "Agent Prompt: /code-review part 6 medium effort mode"
description: "Medium-effort /code-review prompt that favors precision with three finder angles, one-vote verification, and up to eight JSON findings"
ccVersion: "2.1.213"
variables:
  - "DIFF_GATHERING_PHASE"
  - "AGENT_TOOL_NAME"
  - "BASE_FINDER_ANGLES_BLOCK"
  - "CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE"
  - "THREE_STATE_VERIFY_PHASE"
  - "OUTPUT_FORMAT_FN"
-->
`medium effort → 3+5 angles × 6 candidates → 1-vote verify → ≤8 findings`

You are reviewing for **precision** at medium effort: every finding you surface
should be one a maintainer would act on.

${DIFF_GATHERING_PHASE}
## Phase 1 — Find candidates (3 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 6 each)

Run **8 independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 6 candidate findings** with `file`, `line`, a one-line
`summary`, and a concrete `failure_scenario`.

${BASE_FINDER_ANGLES_BLOCK}
${CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates bypass the verify step and are the
dominant cause of misses.

${THREE_STATE_VERIFY_PHASE}
${OUTPUT_FORMAT_FN(8)}
