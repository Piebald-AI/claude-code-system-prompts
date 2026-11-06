<!--
name: "System Reminder: MCP connector call outside session refusal"
description: "Refuses a connector call made outside the session when its file-path argument record cannot be reached and tells Claude to identify the host program rather than the connector as the fault"
ccVersion: "2.1.319"
variables:
  - "CONNECTOR_TOOL_NAME"
-->
No file was sent and ${CONNECTOR_TOOL_NAME} was not called. The program that runs Claude Code made this call outside this session, so Claude Code could not reach the session's note of the connector arguments it asked you to fill with file paths. That note may be the only record of them, so rather than risk sending a file's path to a connector as plain text, Claude Code refuses every connector call made this way, whatever its arguments. The connector is not at fault, and neither is this call: changing it makes no difference. Calling again may or may not work; that depends on the program. Tell the user that the fault is in that program.
