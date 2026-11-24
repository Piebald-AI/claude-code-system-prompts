<!--
name: "Data: SDK MCP call soft error result field"
description: "Documents how a caller can receive an MCP tool's own error result with structured content"
ccVersion: "2.1.331"
-->
Asks for the tool's own error result (CallToolResult.isError) and not its text alone. The reply then has the success subtype and isError: true, with the server's content (text and resource_link blocks only, without icons), structuredContent and _meta. A staged call still carries staging.error_code tool_error and its detail. These answer as they do without the member: any other failure, a cancel or a timeout, a result with no such block and no structuredContent, a result whose kept members come to over 64000 characters of JSON and, with check_permissions, a call whose result a PostToolUse hook or a plugin reviews. A sender that takes the success subtype for the tool's success must not set it. Honoured on the lanes that honour result_not_for_model, with or without that member. Feature-detected as `mcp_call_soft_error_result_v1`; where it is not said, and by a CLI without it, the member is ignored.
