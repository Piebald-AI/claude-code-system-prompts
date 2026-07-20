<!--
name: "Skill: Dynamic pacing loop execution"
description: "Step-by-step instructions for executing a dynamic pacing loop that runs tasks, arms persistent monitors for event-gated waits, schedules fallback heartbeat ticks, and handles task notifications"
ccVersion: "2.1.202"
variables:
  - "TASK_RUN_LABEL"
  - "MONITOR_TOOL_NAME"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "TASK_LIST_TOOL_NAME"
  - "CONFIRMATION_MESSAGE"
  - "DYNAMIC_MODE_SENTINEL"
  - "TASK_STOP_TOOL_NAME"
  - "ADDITIONAL_INFO_FN"
-->
1. **Run ${TASK_RUN_LABEL} now**, following the instructions inlined below.
2. **If the next tick is gated on an event** (CI finishing, a PR comment, a log line) and no ${MONITOR_TOOL_NAME} is already running for it: arm one now with `persistent: true`. Its events wake this loop immediately — you do not wait for the ${SCHEDULE_WAKEUP_TOOL_NAME} deadline. Arm once; on later ticks call ${TASK_LIST_TOOL_NAME} first and skip if a monitor is already running.
3. **Briefly confirm**: ${CONFIRMATION_MESSAGE}, whether a ${MONITOR_TOOL_NAME} is the primary wake signal, and what fallback delay you're about to pick. Write this as text *before* calling ${SCHEDULE_WAKEUP_TOOL_NAME} — the turn ends as soon as that tool returns.
4. **Then, as the last action of this turn, decide whether the loop continues.** If the next check is worth running, call ${SCHEDULE_WAKEUP_TOOL_NAME} with:
   - `delaySeconds`: with a ${MONITOR_TOOL_NAME} armed this is the fallback heartbeat (lean 1200–1800s). Without one, pick based on what you observed this turn — quiet branch? wait longer. Lots in flight? wait shorter. Read the tool's own description for cache-aware delay guidance.
   - `reason`: one short sentence on why you picked that delay.
   - `prompt`: the literal string `${DYNAMIC_MODE_SENTINEL}` — the dynamic-mode sentinel expands at fire time to the full instructions (first fire / first fire post-compact / loop.md edited) or a dynamic-pacing-specific short reminder (subsequent fires). Do not pass the full instructions; that is handled automatically.
   If it isn't, stop instead (step 6) — re-arming is a per-turn choice, not a default.
5. **If woken by a `<task-notification>`** rather than this prompt: handle the event, then make the same decision. If the loop should continue, call ${SCHEDULE_WAKEUP_TOOL_NAME} again with `${DYNAMIC_MODE_SENTINEL}` and the same 1200–1800s `delaySeconds` (the ${MONITOR_TOOL_NAME} remains the wake signal; the new wakeup is only the fallback heartbeat). If the event means the work is finished, stop (step 6).
6. **To stop the loop** — the task is complete, further iterations can't make progress, or the user asked you to stop — call ${SCHEDULE_WAKEUP_TOOL_NAME} with `stop: true` (no other fields) and ${TASK_STOP_TOOL_NAME} any ${MONITOR_TOOL_NAME} you armed (use ${TASK_LIST_TOOL_NAME} to find the task ID if it is no longer in context). Stopping is the loop's normal ending — the user can restart it anytime with /loop.${ADDITIONAL_INFO_FN()}
