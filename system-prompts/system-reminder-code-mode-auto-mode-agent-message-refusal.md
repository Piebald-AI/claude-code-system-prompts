<!--
name: "System Reminder: Code Mode auto mode agent message refusal"
description: "Explains why an unchecked message to an agent is refused in auto mode and directs a new checked piece of code or a user-selected permission-mode change"
ccVersion: "2.1.319"
variables:
  - "SEND_MESSAGE_TOOL_NAME"
  - "IS_REPL_SCRIPT_INNER_CALL"
-->
This ${SEND_MESSAGE_TOOL_NAME} call was NOT run. Auto mode checks each piece of code as a whole before it starts, and that check does not cover this call. Your code can't send a message to an agent outside that check, because auto mode can't read the text that the code sends. This is not a judgment that the message is unsafe. ${IS_REPL_SCRIPT_INNER_CALL?"Tell the user that they can leave auto mode with Shift+Tab, for example for Manual mode, and then ask you to try again.":"You can send this step again in a new piece of code, which gets a check of its own."}
