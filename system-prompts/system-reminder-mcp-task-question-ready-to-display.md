<!--
name: "System Reminder: MCP task question ready to display"
description: "Notifies the user that an MCP task has a question and directs Claude to show it with McpTaskShowQuestion after finishing work that doesn't need the answer"
ccVersion: "2.1.331"
variables:
  - "MCP_TASK_SHOW_QUESTION_TOOL_NAME"
  - "TASK_ID"
-->

<result>
This task's server is waiting for the user to answer a question. Only the user can see and answer it. Tell the user in one sentence that the task has a question, then call the ${MCP_TASK_SHOW_QUESTION_TOOL_NAME} tool (task_id: ${TASK_ID}) to show it to them. The call can wait until the user is back, so unless they have just written, first finish the work that does not need the answer. If you cannot call the tool now, ask the user to reply here, and call it after their reply. Name the task by what they asked for, and leave out its id.
</result>
