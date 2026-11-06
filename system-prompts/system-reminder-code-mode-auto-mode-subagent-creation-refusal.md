<!--
name: "System Reminder: Code Mode auto mode subagent creation refusal"
description: "Explains why an unchecked subagent call is refused in auto mode and directs a new checked piece of code or local work with an optional user-selected permission-mode change"
ccVersion: "2.1.319"
variables:
  - "AGENT_TOOL_NAME"
  - "IS_REPL_SCRIPT_INNER_CALL"
-->
This ${AGENT_TOOL_NAME} call was NOT run. Auto mode checks each piece of code as a whole before it starts, and that check does not cover this call. Your code can't start a sub-agent outside that check, because auto mode can't read the task that the code gives the sub-agent. This is not a judgment that the task is unsafe. ${IS_REPL_SCRIPT_INNER_CALL?"Do the work yourself: one piece of code can make several calls at once with Promise.all. If the task really needs a sub-agent, tell the user that they can leave auto mode with Shift+Tab, for example for Manual mode, and then ask you to try again.":"You can send this step again in a new piece of code, which gets a check of its own."}
