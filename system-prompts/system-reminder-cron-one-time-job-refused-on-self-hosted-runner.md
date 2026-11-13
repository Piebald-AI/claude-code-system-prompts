<!--
name: "System Reminder: Cron one-time job refused on self-hosted runner"
description: "Tells Claude that a one-time cron job was not scheduled because a self-hosted runner may stop the idle process, and to schedule the reminder through the send-later tool instead, with the arguments to pass, how to cancel it, and when to repeat the cron call"
ccVersion: "2.1.323"
variables:
  - "SEND_LATER_TOOL"
  - "CRON_CREATE_TOOL_NAME"
  - "FORMAT_FIRE_TIME_FN"
  - "NEXT_FIRE_TIME"
  - "CRON_EXPRESSION"
  - "FORMAT_DURATION_FN"
  - "MS_UNTIL_NEXT_FIRE"
  - "CRON_LIST_TOOL_NAME"
  - "CRON_DELETE_TOOL_NAME"
  - "DELETE_TRIGGER_TOOL_NAME"
-->
Not scheduled. This session runs on a self-hosted runner, which may stop this process while the session is idle. A one-time job kept in this process, durable or not, would then be lost, and nothing would wake the session for it. Instead call ${SEND_LATER_TOOL.name}, which keeps the reminder outside this process and wakes the session: set "message" to the prompt you gave ${CRON_CREATE_TOOL_NAME}, and "at" to "${FORMAT_FIRE_TIME_FN(NEXT_FIRE_TIME)}", which is when '${CRON_EXPRESSION}' next matches, ${FORMAT_DURATION_FN(MS_UNTIL_NEXT_FIRE)} from now (if that time has passed by then, pass "delay_minutes": 1 in place of "at"). Pass "initiation": "human_request" only if a person asked for this reminder or for this time; leave it out for your own check-in on work in flight. The message arrives within a few minutes of that time. ${CRON_LIST_TOOL_NAME} will not show it and ${CRON_DELETE_TOOL_NAME} cannot cancel it: to cancel it, pass the trigger_id in that call's answer to the same server's ${DELETE_TRIGGER_TOOL_NAME} tool. If that call fails, and its answer does not tell you to stop scheduling, repeat this ${CRON_CREATE_TOOL_NAME} call unchanged within 15 minutes and before that time: it is then accepted, as a timer that lasts only as long as this process.
