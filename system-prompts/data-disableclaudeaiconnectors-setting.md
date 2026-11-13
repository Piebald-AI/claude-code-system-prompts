<!--
name: "Data: disableClaudeAiConnectors setting"
description: "Describes how disableClaudeAiConnectors blocks cloud-connector connections and how true values across settings sources take precedence"
ccVersion: "2.1.324"
-->
When true in any settings source, claude.ai MCP cloud connectors are not auto-fetched or connected, and a claudeai-proxy server passed explicitly (e.g. via --mcp-config or the SDK mcpServers option) does not connect either. Where a managed or served source sets it, the connectors that the desktop app's Code tab hands to a session do not connect either, from the app version that shows them as turned off. Any-source-true wins: a project can opt out, but a project-level false cannot override a user-level true.
