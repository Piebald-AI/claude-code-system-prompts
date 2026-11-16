<!--
name: "System Reminder: Deferred tools available (shortened list)"
description: "Lists deferred tools with MCP servers collapsed into wildcard rows, and explains how to load a server's tools through ToolSearch with a +server query or select: by name"
ccVersion: "2.1.326"
variables:
  - "TOOL_SEARCH_TOOL_NAME"
-->
The following deferred tools are available via ${TOOL_SEARCH_TOOL_NAME}. Their schemas are NOT loaded. This list is shortened to save room: a row such as mcp__claude_ai_Slack__* (42) stands for 42 tools of that server. To load one of them, use ${TOOL_SEARCH_TOOL_NAME} with a word of the server's name that other servers do not share, after a +, and then words for what you need, such as query "+slack send message". Query "mcp__claude_ai_Slack__" alone gives that server's first tools. A query cannot hold the *. For a tool whose full name you know, use query "select:<name>[,<name>...]". Load a tool's schema before you call it. The tools are:
