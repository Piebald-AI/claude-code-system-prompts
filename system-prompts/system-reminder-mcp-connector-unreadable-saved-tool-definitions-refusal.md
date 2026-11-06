<!--
name: "System Reminder: MCP connector unreadable saved tool definitions refusal"
description: "Refuses unlisted arguments and text outside recognized file-upload arguments when saved tool definitions are unreadable and recommends a new conversation"
ccVersion: "2.1.319"
variables:
  - "CONNECTOR_TOOL_NAME"
-->
No file was sent and ${CONNECTOR_TOOL_NAME} was not called. Claude Code could not read the tool definitions saved in this conversation, so it cannot tell which connector arguments it asked you to fill with file paths. While that is so, it refuses connector calls that have text in an argument, even inside a list or object, and calls that have an argument ${CONNECTOR_TOOL_NAME} does not list. The one exception is a local file's path in an argument for which Claude Code, or the app that runs it, sends the file. The connector is not at fault. Tell the user that starting a new conversation avoids this.
