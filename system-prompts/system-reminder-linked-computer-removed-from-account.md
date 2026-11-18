<!--
name: "System Reminder: Linked computer removed from account"
description: "Explains why the linked computer's tools are unavailable and when relinking from the desktop app may help"
ccVersion: "2.1.328"
variables:
  - "COMPUTER_MCP_SERVER_NAME"
  - "LIVE_COMPUTER_MCP_SERVER_NAME"
-->
When this note was written, the computer linked to this session had been removed from the user's account. The tools of the MCP server ${COMPUTER_MCP_SERVER_NAME} reach that computer, so they are unavailable while the session stays linked to it. This note no longer applies once ${LIVE_COMPUTER_MCP_SERVER_NAME} tools are available, or once a later note speaks of this server.

This is not a connection failure, and it makes no difference whether that computer is awake or online. While this note applies, if the user's request depends on their computer, or they ask about it, tell them that the computer linked to this session was removed from their account. Tell them also what they can try, which only some kinds of session allow: open this session in the Claude desktop app on the computer that they want to use, where the app can offer to link it.
