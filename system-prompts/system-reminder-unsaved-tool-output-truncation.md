<!--
name: "System Reminder: Unsaved tool output truncation"
description: "Reports that output too large to save is shown only in part, giving the original and shown sizes and a caller-supplied sentence on how to see more"
ccVersion: "2.1.323"
variables:
  - "ORIGINAL_OUTPUT_SIZE"
  - "SHOWN_OUTPUT_SIZE"
  - "SEE_MORE_GUIDANCE"
-->
Output too large (${ORIGINAL_OUTPUT_SIZE}). It could not be saved, so only the first ${SHOWN_OUTPUT_SIZE} are shown; the rest was dropped. ${SEE_MORE_GUIDANCE}
