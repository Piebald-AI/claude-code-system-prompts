<!--
name: "Data: SDK initialize mcpServers parameter"
description: "SDK initialize parameter that passes MCP server configs over stdin instead of the command line, read only at launch under --await-initialize and handled like an --mcp-config item"
ccVersion: "2.1.326"
-->
MCP servers for Claude Code to run or connect to, keyed by server name: the serializable entries of the SDK `mcpServers` option (host-resident servers go in sdkMcpServers), as the stdin form of one --mcp-config item, which keeps server credentials (stdio `env`, http and sse `headers`) off the command line. Read only at launch under --await-initialize, and then handled as --mcp-config: an invalid entry is skipped and reported in system/init, not fatal; one difference is that a Claude Code process this one starts is not handed them. Without that flag, on a repeated initialize, or over a remote session transport it loads nothing; use mcp_set_servers in a running session. mcp_servers_applied in the response says whether these are the set read at launch.
