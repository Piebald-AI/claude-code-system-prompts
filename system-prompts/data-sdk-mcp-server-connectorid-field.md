<!--
name: "Data: SDK MCP server connectorId field"
description: "Documents the connector identity declared for an SDK MCP server, its server-capability confirmation, and its restriction-only aliases for permission rules and hooks"
ccVersion: "2.1.319"
-->
@internal The id of the claude.ai connector this server proxies, for a host that keys the server by another name. The server must declare the same id in its own capabilities for the CLI to treat it as that connector. With or without that declaration, deny and ask rules, hook matchers and disallowed-tool lists that spell mcp__<connectorId> also reach this server's tools, and nothing that allows does; the id is read as a tool's name would spell it (a character other than a letter, a digit, '-' and '_' as '_'), and one that is then longer than 128 characters or holds '__' is not used for that. Read from initialize and mcp_set_servers, not --mcp-config, when the server is first registered.
