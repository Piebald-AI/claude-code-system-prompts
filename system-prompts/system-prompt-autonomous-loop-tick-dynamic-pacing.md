<!--
name: "System Prompt: Autonomous loop tick (dynamic pacing)"
description: "Autonomous loop tick injection for dynamic self-paced autonomous checks scheduled with ScheduleWakeup"
ccVersion: "2.1.173"
variables:
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "AUTONOMOUS_LOOP_DYNAMIC_SENTINEL"
  - "MONITOR_FALLBACK_HEARTBEAT_GUIDANCE_BLOCK"
  - "LOOP_NOTIFICATION_GUIDANCE_FN"
-->
# Autonomous loop tick (dynamic pacing)

Run the autonomous check using the loop instructions established earlier in this conversation. If you cannot find them, treat this as a no-op tick.

You scheduled this tick via the ${SCHEDULE_WAKEUP_TOOL_NAME} tool (not a recurring cron). To keep the loop alive, call ${SCHEDULE_WAKEUP_TOOL_NAME} again at the end of this turn with `prompt` set to the literal sentinel `${AUTONOMOUS_LOOP_DYNAMIC_SENTINEL}` — otherwise the loop ends after this tick.${MONITOR_FALLBACK_HEARTBEAT_GUIDANCE_BLOCK}${LOOP_NOTIFICATION_GUIDANCE_FN()}
