<!--
name: "Tool Parameter: matched ask rule"
description: "Describes metadata identifying a user-configured permissions.ask rule that forced a tool approval prompt while preserving the tool-authored decision reason"
ccVersion: "2.1.319"
-->
Set when a user-configured ask RULE (permissions.ask) forced this prompt but the ask carries the tool's own decision_reason — the ask-rule substitution keeps the richer tool-minted ask, so the rule rides here instead of decision_reason_type 'rule'. May also be set, whatever the decision_reason, when an ask rule reaches an MCP tool only under another name of its server (such as a connector's id or its claude.ai name), not under the name in tool_name: a host that looks for the rule by that name does not find it. Hosts making policy on decision_reason_type (e.g. auto-deny safetyCheck) or running host-side auto-approval should treat asks carrying this field as rule-forced: the user's stated intent is a human prompt. Values are producer-authored but render-unsafe like decision_reason; sanitize before display.
