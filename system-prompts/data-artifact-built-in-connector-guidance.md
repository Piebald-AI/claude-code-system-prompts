<!--
name: "Data: Artifact built-in connector guidance"
description: "Explains how an Artifact declares the built-in claude.ai connector and makes viewer features optional when session-only tools or policy-blocked tools are unavailable"
ccVersion: "2.1.319"
variables:
  - "BUILT_IN_META_CONNECTOR"
-->
 A page can call the `mcp__${BUILT_IN_META_CONNECTOR.toolPrefix}__*` tools in your tool list through the built-in claude.ai connector `${BUILT_IN_META_CONNECTOR.server}`: declare that exact name as `server` with those tools' upstream names. A published page calls them as the viewer, with no calling session, so tools that act on the calling session (e.g. `send_later`, `watch_url`) do not apply there. A viewer may have fewer of the connector's tools than you (often only a core set for managing routines), so keep each feature optional: only after the viewer has allowed the connector, have the page call `listTools()`. When a tool a feature needs is not listed, or a call to it rejects with code `blocked_by_policy`, show that feature as unavailable and do not call that tool.
