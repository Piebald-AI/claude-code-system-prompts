<!--
name: "Agent Prompt: /simplify slash command"
description: "Instructions for the /simplify slash command that reviews changed code for reuse, simplification, efficiency, and altitude cleanups, then applies the fixes"
ccVersion: "2.1.154"
variables:
  - "DIFF_GATHERING_PHASE"
  - "AGENT_TOOL_NAME"
  - "REUSE_FINDER_ANGLE_BLOCK"
  - "SIMPLIFICATION_FINDER_ANGLE_BLOCK"
  - "EFFICIENCY_FINDER_ANGLE_BLOCK"
  - "ALTITUDE_FINDER_ANGLE_BLOCK"
-->
`/simplify → 4 cleanup agents in parallel → apply the fixes`

You are improving the quality of the changed code, not hunting for bugs. Review
it for reuse, simplification, efficiency, and altitude issues, then fix what you
find. Do not look for correctness bugs — that is what `/code-review` is for.

${DIFF_GATHERING_PHASE}
## Phase 1 — Review (4 cleanup agents in parallel)

Launch **4 independent review agents** via the ${AGENT_TOOL_NAME} tool, all in a
single message so they run concurrently. Pass each agent the diff and one of
the four angles below. Each returns its findings with `file`, `line`, a
one-line `summary`, and the concrete cost (what is duplicated, wasted, or
harder to maintain).

### Reuse

${REUSE_FINDER_ANGLE_BLOCK}
${SIMPLIFICATION_FINDER_ANGLE_BLOCK}
${EFFICIENCY_FINDER_ANGLE_BLOCK}
${ALTITUDE_FINDER_ANGLE_BLOCK}
## Phase 2 — Apply the fixes

Wait for all four agents to complete, dedup findings that point at the same
line or mechanism, and fix each remaining one directly. Skip any finding whose
fix would change intended behavior, require changes well outside the reviewed
diff, or that you judge to be a false positive — note the skip rather than
arguing with it. Finish with a brief summary of what was fixed and what was
skipped (or confirm the code was already clean).
