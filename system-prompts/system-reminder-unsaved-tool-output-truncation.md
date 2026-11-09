<!--
name: "System Reminder: Unsaved tool output truncation"
description: "Reports output that could not be saved, shows only a preview and explains paging or retrying when several results share the output limit"
ccVersion: "2.1.321"
variables:
  - "TRUNCATED_OUTPUT_START_TAG"
  - "ORIGINAL_OUTPUT_SIZE"
  - "SHOWN_OUTPUT_SIZE"
  - "SHARES_OUTPUT_LIMIT"
  - "OUTPUT_PREVIEW"
  - "TRUNCATED_OUTPUT_END_TAG"
-->
${TRUNCATED_OUTPUT_START_TAG}
Output too large (${ORIGINAL_OUTPUT_SIZE}). It could not be saved, so only the first ${SHOWN_OUTPUT_SIZE} are shown; the rest was dropped. ${SHARES_OUTPUT_LIMIT?"This part is short because other tool calls in the same reply also gave results that were too large and could not be saved, and such results share one limit. To see more: if the tool can page or filter, ask for the part you need; or, if this call is safe to repeat, run it again with fewer calls in the same reply.":"If the tool can page or filter its results, call it again for the part you need."}

${OUTPUT_PREVIEW}
${TRUNCATED_OUTPUT_END_TAG}
