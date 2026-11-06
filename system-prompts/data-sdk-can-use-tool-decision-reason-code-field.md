<!--
name: "Data: SDK can_use_tool decision_reason_code field"
description: "Documents host-actionable reason codes on can_use_tool permission requests, including the MCP organization ask ceiling and exclusion of denial-only auto-mode codes"
ccVersion: "2.1.319"
-->
@internal A closed-set code for a reason a host can act on, beside decision_reason_type (whose values are unchanged, so type-keyed host policy decides as before): 'outside_reads_blocked', 'memory_paused', 'classifier_transcript_too_long', 'org_ask_ceiling' (the MCP tool's ceiling, toolPermissions, is 'ask', and an ask rule or the ceiling itself raised the ask: type 'rule' or 'other'). The type also lists auto_mode_ values, which are sent on system/permission_denied only, never on this request. Absent for every other reason; new values are additive.
