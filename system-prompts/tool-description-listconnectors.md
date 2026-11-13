<!--
name: "Tool Description: ListConnectors"
description: "Describes the ListConnectors tool for listing installed claude.ai MCP connectors, filtering by keyword, and interpreting org-level connection and chat-enabled status"
ccVersion: "2.1.323"
variables:
  - "SEARCH_MCP_REGISTRY_TOOL_NAME"
  - "SUGGEST_CONNECTORS_TOOL_NAME"
-->
List the MCP connectors installed for the user's claude.ai org. Call this when the user asks what connectors they have. Pass keywords to filter to a topic; omit to list all.

Returns name, description, whether each connector is connected at org level (connected may be null when the status check was unavailable — treat that as unknown, not disconnected), and enabledInChat (whether its tools are loaded in this session). enabledInChat: false means the connector's tools are not loaded in this session; the field does not say why. The user can check a connector, and its tool permissions, in their claude.ai connector settings. Do not name a setting for this chat alone; there may be none. To recommend connectors the user does NOT have yet, use ${SEARCH_MCP_REGISTRY_TOOL_NAME} → ${SUGGEST_CONNECTORS_TOOL_NAME} instead; this tool does not itself connect anything.
