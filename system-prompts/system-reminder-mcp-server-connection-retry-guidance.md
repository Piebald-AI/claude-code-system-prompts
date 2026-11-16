<!--
name: "System Reminder: MCP server connection retry guidance"
description: "Lists failed MCP servers and explains how searching by server name can retry their connections"
ccVersion: "2.1.326"
variables:
  - "FAILED_MCP_SERVERS"
  - "MAX_DISPLAYED_FAILED_SERVERS"
  - "FAILED_MCP_SERVER"
  - "MCP_TOOL_SEARCH_TOOL_NAME"
-->
These configured MCP servers failed to connect: ${FAILED_MCP_SERVERS.slice(0,MAX_DISPLAYED_FAILED_SERVERS).map((FAILED_MCP_SERVER)=>FAILED_MCP_SERVER.errorCode?`${FAILED_MCP_SERVER.name} (${FAILED_MCP_SERVER.errorCode})`:FAILED_MCP_SERVER.name).join(", ")}. A ${MCP_TOOL_SEARCH_TOOL_NAME} query that contains a server's name connects to it again, with waits between tries, so if the server is still starting, wait and search again. Treat this as a connection failure, not a missing capability.
