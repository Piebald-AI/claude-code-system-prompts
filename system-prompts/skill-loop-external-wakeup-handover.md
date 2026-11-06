<!--
name: "Skill: /loop external wakeup handover"
description: "Offers an explicitly requested cloud-session loop using one pending send_later wakeup, replacing local timers only after acceptance and cancelling or rearming the wakeup until the work ends or the time limit is reached"
ccVersion: "2.1.319"
variables:
  - "SEND_LATER_TOOL_NAME"
  - "CLAUDE_CODE_REMOTE_MCP_SERVER_NAME"
  - "TOOL_SEARCH_TOOL_NAME"
  - "DELETE_TRIGGER_TOOL_NAME"
  - "CRON_DELETE_TOOL_NAME"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "CANCEL_TIMEFRAME_DAYS"
-->

If a `${SEND_LATER_TOOL_NAME}` tool from the `${CLAUDE_CODE_REMOTE_MCP_SERVER_NAME}` server is available (load it with ${TOOL_SEARCH_TOOL_NAME} if it is deferred), also say they can ask for a loop that survives this. Build that loop only when they ask for it: in place of a timer, keep exactly one pending `${SEND_LATER_TOOL_NAME}` call, with a message that says what to run next, the cadence and the date to stop, in plain words and never as a `/loop` command. It is held outside the container and wakes the session on a new one. If anything wakes you while one is pending, cancel it with `${DELETE_TRIGGER_TOOL_NAME}` before you arm another. Once the first one is accepted, cancel any timer you set for this loop (${CRON_DELETE_TOOL_NAME}, or ${SCHEDULE_WAKEUP_TOOL_NAME} with `stop: true`). That only hands the loop over, so report the hand-over and skip the steps for a finished loop, whatever the tool's result says. Re-arm it only while the work is unfinished, stop after at most ${CANCEL_TIMEFRAME_DAYS} days, and if the user says stop, cancel the pending one with `${DELETE_TRIGGER_TOOL_NAME}`. If `${SEND_LATER_TOOL_NAME}` is refused, tell the user why and keep a timer running.
