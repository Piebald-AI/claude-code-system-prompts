<!--
name: "Tool Description: SendMessage"
description: "Describes the SendMessage tool for communicating with other agents and handling legacy team protocol responses"
ccVersion: "2.1.331"
variables:
  - "IS_MESSAGING_BEYOND_OWN_AGENTS_DISABLED"
  - "CROSS_SESSION_RECIPIENT_TABLE_ROWS"
  - "CLOUD_SESSION_RECIPIENT_TABLE_ROWS"
  - "OTHER_CLOUD_SESSIONS_GUIDANCE_BLOCK"
  - "CROSS_SESSION_GUIDANCE_BLOCK"
  - "SHOULD_INCLUDE_LEGACY_PROTOCOL_RESPONSES"
-->

# SendMessage

Send a message to another agent.

```json
{"to": "researcher", "summary": "assign task 1", "message": "start on task #1"}
```

| `to` | |
|---|---|
${IS_MESSAGING_BEYOND_OWN_AGENTS_DISABLED?'| `"researcher"` | An agent of this session, by its name |\n| `"main"` | The main conversation (background subagents only) |\n\nNo one outside this session can be reached.':`| `"researcher"` | Teammate by name |
| `"main"` | The main conversation (background subagents only) |${CROSS_SESSION_RECIPIENT_TABLE_ROWS}${CLOUD_SESSION_RECIPIENT_TABLE_ROWS}`}

Your plain text output is NOT visible to other agents — to communicate, you MUST call this tool.${IS_MESSAGING_BEYOND_OWN_AGENTS_DISABLED?"":" Messages from teammates are delivered automatically; you don't check an inbox."} Refer to agents by name — names keep working after an agent completes (a send resumes it from its transcript). Use the raw `agentId` (format `a...-...`) from its spawn result only when the agent has no name, or when a newer agent took the name (latest wins). When relaying, don't quote the original — it's already rendered to the user.${OTHER_CLOUD_SESSIONS_GUIDANCE_BLOCK}${CROSS_SESSION_GUIDANCE_BLOCK}${SHOULD_INCLUDE_LEGACY_PROTOCOL_RESPONSES&&!IS_MESSAGING_BEYOND_OWN_AGENTS_DISABLED?'\n\n## Protocol responses (legacy)\n\nIf you receive a JSON message with `type: "shutdown_request"` or `type: "plan_approval_request"`, respond with the matching `_response` type — echo the `request_id`, set `approve` true/false:\n\n```json\n{"to": "team-lead", "message": {"type": "shutdown_response", "request_id": "...", "approve": true}}\n{"to": "researcher", "message": {"type": "plan_approval_response", "request_id": "...", "approve": false, "feedback": "add error handling"}}\n```\n\nApproving shutdown terminates your process. Rejecting plan sends the teammate back to revise. Don't originate `shutdown_request` unless asked. Don't send structured JSON status messages — report progress through your task tools if you have them, otherwise in plain prose.':""}
