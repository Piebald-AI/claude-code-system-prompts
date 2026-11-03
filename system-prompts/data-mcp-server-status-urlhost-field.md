<!--
name: "Data: MCP server status urlHost field"
description: "Documents the settings-file host and port exposed for an HTTP or SSE MCP server when its configuration is withheld, including cloud-hosting and privacy restrictions"
ccVersion: "2.1.317"
-->
@internal Host and port of an http or sse server's URL as its settings file wrote it, for display where `config` is withheld. Absent for other transports, for a server with no settings file (dynamic, plugin, sdk, agent, claudeai), for a server the session proxies (its host would be the session's own), outside a worker known to be Anthropic-hosted, where `config` is withheld (on a self-hosted runner, for one, it can name a machine in the customer's own network), when the file's host holds an environment-variable placeholder or the file can't be re-read, and on CLIs that predate the field.
