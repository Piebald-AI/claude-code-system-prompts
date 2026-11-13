<!--
name: "Tool Description: SearchMcpRegistry"
description: "Describes the SearchMcpRegistry tool for discovering MCP connectors by keyword, including named-product and intent-based examples and install-state guidance"
ccVersion: "2.1.323"
variables:
  - "SUGGEST_CONNECTORS_TOOL_NAME"
  - "SEARCH_MCP_REGISTRY_TOOL_NAME"
-->
Search the MCP connector registry by keyword. Call this when connecting to an MCP server might help complete the task — whether or not the user named a specific product.

Named-product examples:
- "check my Asana tasks" → keywords ["asana", "tasks", "todo"]
- "find issues in Jira" → keywords ["jira", "issues"]

Intent-based examples (no product named):
- "help me manage my tasks" → keywords ["tasks", "todo", "project management"]
- "pull up the design mockups" → keywords ["design", "figma", "mockup"]

Returns a ranked list with directoryUuid, name, description, sample tool names, installState (org-level), and enabledInChat (this session). Results include the org's custom connectors (ones the org configured that are not in the public directory) when they match the keywords. enabledInChat: false means the connector's tools are not loaded in this session; the field does not say why. ${SUGGEST_CONNECTORS_TOOL_NAME} takes a result's directoryUuid whatever its installState is, not only that of a connector that is not installed. The user can also check a connector, and its tool permissions, in their claude.ai connector settings. Do not name a setting for this chat alone; there may be none. ${SEARCH_MCP_REGISTRY_TOOL_NAME} does not itself connect anything.
