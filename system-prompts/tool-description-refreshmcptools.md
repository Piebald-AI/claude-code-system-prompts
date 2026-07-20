<!--
name: "Tool Description: RefreshMcpTools"
description: "Describes when and how to refresh connected MCP servers tool lists to recover missing or stale tools"
ccVersion: "2.1.211"
-->
Re-queries the tool list of connected MCP servers and updates the set of available tools, reporting which tools were added or removed.

MCP servers normally push a notification when their tool list changes, but that notification can be missed (connection hiccups, a device announcing while the notification stream was down). Use this tool to re-sync when the available tools may be out of date. Good triggers:
- The user says a device or app is now open or connected (e.g. "my desktop IS open", "I just started the app") after a tool call failed with device-not-connected or the expected tools are missing.
- A tool you expect an MCP server to provide is absent from your available tools.
- A server's tools look stale after its connection recovered.

The refreshed tools are available immediately — you can call them on your next step.

Usage:
- Refresh all connected servers: `RefreshMcpTools` with no arguments
- Refresh one server: `RefreshMcpTools({ server: "myserver" })`
