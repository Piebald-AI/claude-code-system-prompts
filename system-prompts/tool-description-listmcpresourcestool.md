<!--
name: "Tool Description: ListMcpResourcesTool"
description: "Tool description for listing available MCP resources from all configured servers or a specific server"
ccVersion: "2.1.173"
-->

Lists available resources from configured MCP servers.
Each resource object includes a 'server' field indicating which server it's from.

Usage examples:
- List all resources from all servers: `listMcpResources`
- List resources from a specific server: `listMcpResources({ server: "myserver" })`
