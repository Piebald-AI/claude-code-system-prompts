<!--
name: "Data: SDK MCP server dataFlowServer field"
description: "Describes the internal MCP server field that tells Claude Code where the host got a server (Anthropic's registry, a claude.ai connector, or user configuration) for the data flow records of calls to it, and when it is read"
ccVersion: "2.1.323"
-->
@internal Where the host got this server, for the data flow records of calls to it: one of Anthropic's, by its registry id; a claude.ai connector, by its id (tagged or a bare UUID) and its directory id or null; or one the user configured, by the transport the host reaches it over. The first two are taken only in a session a desktop host started. Without it, or with a value of another shape, the records say unknown (docs/desktop-host-contract.md, D139). Read from initialize, mcp_set_servers and the Agent SDK's server config, not --mcp-config, when the server is first registered.
