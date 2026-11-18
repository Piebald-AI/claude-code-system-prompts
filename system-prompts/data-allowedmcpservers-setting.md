<!--
name: "Data: allowedMcpServers setting"
description: "Describes how the enterprise allowedMcpServers setting governs user-added versus organization-delivered MCP servers, including ${VAR} expansion, undefined and empty-array behavior, and denylist precedence"
ccVersion: "2.1.328"
-->
Enterprise allowlist of the MCP servers users may use. Governs servers users add (user, project and local config, --mcp-config, agent frontmatter, plugins, claude.ai connectors); servers the organization itself delivers (managedMcpServers, and managed-mcp.json entries with no ${VAR} in their command, args, url or header values) are allowed without being listed; a managed-mcp.json entry with ${VAR} in any of those must match this list. An entry found only in a project's .claude/settings.json or .claude/settings.local.json can admit a server the organization provides (managed-mcp.json, managedMcpServers, or a plugin that managed settings list in enabledPlugins) but can't keep one out. If undefined, all servers are allowed. If empty array, users can use no servers of their own. Denylist takes precedence - if a server is on both lists, it is denied.
