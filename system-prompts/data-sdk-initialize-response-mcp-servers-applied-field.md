<!--
name: "Data: SDK initialize response mcp_servers_applied field"
description: "SDK initialize response field saying whether the mcpServers sent in initialize are the set read at launch, and telling hosts to treat an absent field as not applied"
ccVersion: "2.1.326"
-->
Whether the `mcpServers` in this initialize are the set the process read at launch under --await-initialize, so a re-sent initialize naming the same set also reads true; false otherwise. True says they were taken as an --mcp-config item, not that each one connected: a server missing from system/init mcp_servers was not loaded. The field loads nothing after launch. Absent when the request named none, and on CLIs that predate the field, which never read `mcpServers`: a host that sent servers must treat absence as not applied.
