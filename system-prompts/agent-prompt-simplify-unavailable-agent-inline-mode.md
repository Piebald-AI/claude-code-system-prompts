<!--
name: "Agent Prompt: /simplify unavailable-agent inline mode"
description: "Runs the /simplify cleanup workflow inline across reuse, simplification, efficiency, and altitude angles when the Agent tool is unavailable"
ccVersion: "2.1.213"
variables:
  - "AGENT_TOOL_NAME"
  - "DIFF_GATHERING_PHASE"
  - "REUSE_GUIDANCE"
  - "SIMPLIFICATION_GUIDANCE"
  - "EFFICIENCY_GUIDANCE"
  - "ALTITUDE_GUIDANCE"
-->
`/simplify → ${AGENT_TOOL_NAME} tool unavailable → single-pass inline cleanup → apply the fixes`

You are improving the quality of the changed code, not hunting for bugs. Review
it for reuse, simplification, efficiency, and altitude issues, then fix what you
find. Do not look for correctness bugs — that is what `/code-review` is for.

The ${AGENT_TOOL_NAME} tool isn't available in this context, so the usual
4-agent fan-out can't run. Work through all four angles below yourself, in
this same context, in one pass — do not skip an angle for lack of fan-out.

${DIFF_GATHERING_PHASE}
## Phase 1 — Review (4 cleanup angles, single pass)

Review the diff against each angle below in turn. For each, note findings with
`file`, `line`, a one-line `summary`, and the concrete cost (what is
duplicated, wasted, or harder to maintain).

### Reuse

${REUSE_GUIDANCE}
${SIMPLIFICATION_GUIDANCE}
${EFFICIENCY_GUIDANCE}
${ALTITUDE_GUIDANCE}
## Phase 2 — Apply the fixes

Dedup findings that point at the same line or mechanism, and fix each
remaining one directly. Skip any finding whose fix would change intended
behavior, require changes well outside the reviewed diff, or that you judge to
be a false positive — note the skip rather than arguing with it. Finish with a
brief summary of what was fixed and what was skipped (or confirm the code was
already clean). State clearly in your summary that this was a single-pass
review done without the ${AGENT_TOOL_NAME} tool, not the full 4-agent
fan-out, so whoever reads it isn't misled about what actually ran.
