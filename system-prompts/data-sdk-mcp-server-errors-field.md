<!--
name: "Data: SDK MCP server errors field"
description: "Schema description for the optional internal mcp_server_errors list on SDK system init frames, including skipped configuration categories, affected-server omission, and CI handling"
ccVersion: "2.1.326"
-->
@internal MCP server config entries from --mcp-config (or initialize.mcpServers) that failed validation and were skipped (e.g. a `url` entry with no `type`). Affected servers are absent from `mcp_servers[]`. `type` is a stable category from an open set — currently unknown_type, url_missing_type, invalid_config, reserved_name, or (Remote Control child only) bridge_carrier_foreign_entry, bridge_carrier_not_http, bridge_carrier_url_mismatch, bridge_carrier_no_ingress_origin, bridge_carrier_no_session_id; treat values you do not recognize as a generic skip. The key is omitted when there are no errors; CI can fail on `(mcp_server_errors?.length ?? 0) > 0`. On connections that persist frames server-side (the local bridge-worker lane) this key is always omitted — the skipped-entry detail stays in the local log, so an omitted key there does NOT assert every entry validated.
