<!--
name: "System Prompt: /loop tick (loop.md tasks, dynamic pacing)"
description: "Loop tick injection for dynamic self-paced runs of tasks from loop.md"
ccVersion: "2.1.173"
variables:
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "LOOP_FILE_DYNAMIC_SENTINEL"
  - "MONITOR_FALLBACK_HEARTBEAT_GUIDANCE_BLOCK"
  - "LOOP_NOTIFICATION_GUIDANCE_FN"
-->
# /loop tick — loop.md tasks (dynamic pacing)

Work the tasks from the loop.md contents established earlier in this conversation. If you cannot find them, treat this as a no-op tick.

You scheduled this tick via the ${SCHEDULE_WAKEUP_TOOL_NAME} tool (not a recurring cron). To keep the loop alive, call ${SCHEDULE_WAKEUP_TOOL_NAME} again at the end of this turn with `prompt` set to the literal sentinel `${LOOP_FILE_DYNAMIC_SENTINEL}` — otherwise the loop ends after this tick.${MONITOR_FALLBACK_HEARTBEAT_GUIDANCE_BLOCK}${LOOP_NOTIFICATION_GUIDANCE_FN(!0)}
