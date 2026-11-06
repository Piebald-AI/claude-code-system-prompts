<!--
name: "System Reminder: MCP task monitoring continues after a failure"
description: "Reports that a background MCP task's outcome is unknown while slower monitoring continues and asks for a brief user explanation without repeating or cancelling the task"
ccVersion: "2.1.319"
variables:
  - "MCP_TASK_MONITORING_FAILURE_REASON"
  - "IS_CONVERSATION_SAVED"
  - "MCP_TASK_RECOVERY_GUIDANCE"
-->
Claude Code cannot follow this task on its server at the moment: ${MCP_TASK_MONITORING_FAILURE_REASON}.
It did not cancel the task, which may still be running there or may have ended. Its outcome is not known, so do not report it as done or failed. Claude Code keeps checking, less often, while this session runs, and you will get another notification if it learns how the task ended.${IS_CONVERSATION_SAVED?" Checking stops when this session ends, and starts again if the session is resumed.":""}${MCP_TASK_RECOVERY_GUIDANCE}
Tell the user in two or three sentences that Claude Code cannot follow the task at the moment, why, ${MCP_TASK_RECOVERY_GUIDANCE===""?"and that it is still checking":"that it is still checking, and what they can do"}. Unless the user asks, do not call the tool again (that may repeat the work), stop the task, or wait for it. Do nothing else because of this notice.
