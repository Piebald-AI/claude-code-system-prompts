<!--
name: "Tool Description: Agent (usage notes)"
description: "Usage notes and instructions for the Task/Agent tool, including guidance on launching subagents, background execution, resumption, and worktree isolation"
ccVersion: "2.1.215"
variables:
  - "TOOL_BASE_DESCRIPTION"
  - "WHEN_NOT_TO_USE_NOTE"
  - "CAN_RUN_BACKGROUND_AGENTS"
  - "IS_FORK_SUBAGENT_FEATURE_ENABLED"
  - "CAN_FORK_CONTEXT"
  - "SEND_MESSAGE_TOOL_NAME"
  - "AGENT_TOOL_NAME"
  - "IS_DEFAULT_SUBAGENT_STEERING_MODE"
  - "IS_REMOTE_ISOLATION_AVAILABLE_FN"
  - "IS_IN_PROCESS_TEAMMATE_CONTEXT_FN"
  - "IS_TEAMMATE_CONTEXT_FN"
  - "FORK_USAGE_GUIDELINES"
  - "WRITING_SUBAGENT_PROMPTS_GUIDANCE"
  - "FORK_CAPABLE_SUBAGENT_DELEGATION_EXAMPLES"
  - "NON_FORK_SUBAGENT_DELEGATION_EXAMPLES"
-->
${TOOL_BASE_DESCRIPTION}
${WHEN_NOT_TO_USE_NOTE}
## Usage notes

- Always include a short description summarizing what the agent will do
- ${CAN_RUN_BACKGROUND_AGENTS?"When the agent is done, its final report is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.":"When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result."}
- Trust but verify: an agent's summary describes what it intended to do, not necessarily what it did. When an agent writes or edits code, check the actual changes before reporting the work as done.${CAN_RUN_BACKGROUND_AGENTS&&!IS_FORK_SUBAGENT_FEATURE_ENABLED?"\n- Agents run in the background by default. When an agent runs in the background, you will be automatically notified when it completes — do NOT sleep, poll, or proactively check on its progress. Continue with other work or respond to the user instead.\n- **Foreground vs background**: Pass `run_in_background: false` to run an agent in the foreground when you need its results before you can proceed — e.g., research agents whose findings inform your next steps. Otherwise let it run in the background (the default) so you can keep working in parallel.":""}${CAN_RUN_BACKGROUND_AGENTS&&!CAN_FORK_CONTEXT?`
- **Don't race**: after launching a background agent, you know nothing about its results. Never fabricate or predict them in any format — not as prose, summary, or structured output. The completion notification arrives in a later turn; it is never something you write yourself. If the user asks before it lands, say the agent is still running — give status, not a guess.`:""}
- To continue a previously spawned agent, use ${SEND_MESSAGE_TOOL_NAME} with the agent's ID or name as the `to` field — that resumes it with full context. A new ${AGENT_TOOL_NAME} call starts a fresh agent with no memory of prior runs${CAN_FORK_CONTEXT?' (except subagent_type: "fork")':""}, so the prompt must be self-contained.
- Each agent type's model, reasoning effort, and tool access are set in its definition (`.claude/agents/*.md` frontmatter, or the SDK `agents` option); the `model` parameter here overrides the definition for this one call.
- Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since a fresh agent is not aware of the user's intent${IS_DEFAULT_SUBAGENT_STEERING_MODE?`
- If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first.
- If the user specifies that they want you to run agents "in parallel", you MUST send a single message with multiple ${AGENT_TOOL_NAME} tool use content blocks. For example, if you need to launch both a build-validator agent and a test-runner agent in parallel, send a single message with both tool calls.`:""}
- With `isolation: "worktree"`, the worktree is automatically cleaned up if the agent makes no changes; otherwise the path and branch are returned in the result.${IS_REMOTE_ISOLATION_AVAILABLE_FN()?'\n- You can set `isolation: "remote"` to run the agent in a remote CCR environment. This is always a background task; you'll be notified when it completes. Use for long-running tasks that need a fresh sandbox.':""}${IS_IN_PROCESS_TEAMMATE_CONTEXT_FN()?`
- The run_in_background and name parameters are not available in this context. Only synchronous subagents are supported.`:IS_TEAMMATE_CONTEXT_FN()?`
- The name parameter is not available in this context — teammates cannot spawn other teammates. Omit it to spawn a subagent.`:""}${FORK_USAGE_GUIDELINES}${WRITING_SUBAGENT_PROMPTS_GUIDANCE}

${CAN_FORK_CONTEXT?FORK_CAPABLE_SUBAGENT_DELEGATION_EXAMPLES:NON_FORK_SUBAGENT_DELEGATION_EXAMPLES}
