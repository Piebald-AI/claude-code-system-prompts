<!--
name: "System Reminder: MCP connector name too long for file approval"
description: "Refuses file uploads when the connector's escaped name cannot fit in the approval prompt and tells the user how much to shorten it while leaving file-free calls available"
ccVersion: "2.1.319"
variables:
  - "CLAUDE_AI_CONNECTOR_NAME_PREFIX"
  - "MAX_CONNECTOR_APPROVAL_NAME_CHARACTERS"
  - "ESCAPED_CONNECTOR_NAME_LENGTH"
  - "CONNECTOR_TOOL_NOT_CALLED_NOTE"
-->
No file was sent: this connector's name is too long for Claude Code to show whole in its approval prompt, and Claude Code asks the user to approve sending files only to a connector it can name in full. The prompt writes the name in quotes, as Claude Code holds it: "${CLAUDE_AI_CONNECTOR_NAME_PREFIX}", then the name the connector was given, then a number such as " (2)" where two connectors' names would otherwise clash. It shows at most ${MAX_CONNECTOR_APPROVAL_NAME_CHARACTERS.toLocaleString("en-US")} characters of that, the two quotes included, counting a plain English letter, digit, space or most punctuation as one, a quote or backslash as two, and an angle bracket or an accented or non-Latin letter as six or more. This name comes to ${ESCAPED_CONNECTOR_NAME_LENGTH.toLocaleString("en-US")}, so the name the connector was given has to lose at least ${(ESCAPED_CONNECTOR_NAME_LENGTH-MAX_CONNECTOR_APPROVAL_NAME_CHARACTERS).toLocaleString("en-US")} of those characters. Tell the user, and do not retry with a file: a connector's name is set where the connector was added or published, not in Claude Code. ${CONNECTOR_TOOL_NOT_CALLED_NOTE} A call that sets no file argument is still sent.
