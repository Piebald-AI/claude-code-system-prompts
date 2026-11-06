<!--
name: "System Reminder: MCP task monitoring stopped"
description: "Reports that monitoring a background MCP task has stopped without knowing its outcome and explains possible resumed checks and sign-in recovery without repeating the original work"
ccVersion: "2.1.319"
variables:
  - "MCP_TASK_MONITORING_FAILURE_REASON"
  - "IS_CONVERSATION_SAVED"
  - "MCP_TASK_ERROR_CODE"
  - "GET_MCP_SIGN_IN_LOCATION_FN"
-->
Claude Code has stopped checking on this task: ${MCP_TASK_MONITORING_FAILURE_REASON}.
Claude Code did not cancel the task: it may still be running on the server, or it may have ended there, so do not report it as done or as failed. ${IS_CONVERSATION_SAVED?"No result will arrive unless this session is resumed later; Claude Code may then be able to follow the task again, and you will be told the result if it does.":"No result will arrive."} Tell the user that Claude Code has stopped checking on this task, why, and that its outcome is not known. Do not call the tool again unless the user asks: a second call may repeat the work. Do nothing else because of this notice.${MCP_TASK_ERROR_CODE==="needs_sign_in"&&IS_CONVERSATION_SAVED?`
Where the user can sign in: ${GET_MCP_SIGN_IN_LOCATION_FN()}. After a sign-in, Claude Code checks on the task again only when this session is resumed.`:""}
