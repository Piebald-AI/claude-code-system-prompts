<!--
name: "Tool Description: Agent (usage notes)"
description: "Usage notes and instructions for the Task/Agent tool, including guidance on launching subagents, background execution, resumption, and worktree isolation"
ccVersion: "2.1.323"
variables:
  - "TOOL_BASE_DESCRIPTION"
  - "WHEN_NOT_TO_USE_NOTE"
  - "CAN_RUN_BACKGROUND_AGENTS"
  - "IS_BACKGROUND_AGENTS_OPT_IN"
  - "IS_BACKGROUND_FORK_ENABLED"
  - "WAIT_ON_BACKGROUND_WORK_NOTE"
  - "CAN_FORK_CONTEXT"
  - "BACKGROUND_SESSION_KEEPALIVE_GUIDANCE"
  - "CAN_CONTINUE_AGENT"
  - "SEND_MESSAGE_TOOL_NAME"
  - "AGENT_TOOL_NAME"
  - "PROCESS_ENV"
  - "SUBAGENT_EFFORT_GUIDANCE_NOTE"
  - "IS_DEFAULT_SUBAGENT_STEERING_MODE"
  - "PARALLEL_WORKTREE_ISOLATION_NOTE"
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
- ${CAN_RUN_BACKGROUND_AGENTS||IS_BACKGROUND_AGENTS_OPT_IN?"When the agent is done, its final report is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.":"When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result."}
- Trust but verify: an agent's summary describes what it intended to do, not necessarily what it did. When an agent writes or edits code, check the actual changes before reporting the work as done.${CAN_RUN_BACKGROUND_AGENTS&&!IS_BACKGROUND_FORK_ENABLED?`
- Agents run in the background by default. When an agent runs in the background, you will be automatically notified when it completes — do NOT sleep, poll, or proactively check on its progress. Continue with other work or respond to the user instead.${WAIT_ON_BACKGROUND_WORK_NOTE}
- **Foreground vs background**: Pass `run_in_background: false` only when your very next action depends on the agent's result and nothing else could usefully happen while it runs — e.g., a research agent whose finding gates the edit you're about to make. Otherwise let it run in the background (the default) — this includes fire-and-forget work, independent investigations, and anything where the user might hand you something else in the meantime. Wanting the result "next" is not enough on its own.`:""}${CAN_RUN_BACKGROUND_AGENTS&&!(CAN_FORK_CONTEXT&&IS_BACKGROUND_FORK_ENABLED)?`
- **Don't race**: after launching a background agent, you know nothing about its results. Never fabricate or predict them in any format — not as prose, summary, or structured output. The completion notification arrives in a later turn; it is never something you write yourself. If the user asks before it lands, say the agent is still running — give status, not a guess.`:""}${IS_BACKGROUND_AGENTS_OPT_IN?`
- **Background agents**: an agent runs in the background only if you pass `run_in_background: true`, and a call that passes it may still run in the foreground or be refused. When an agent does run in the background, the call returns at once without its report, and you will be automatically notified when it completes — do NOT sleep, poll, or proactively check on its progress. Continue with other work or respond to the user instead.${WAIT_ON_BACKGROUND_WORK_NOTE} After launching a background agent, you know nothing about its results. Never fabricate or predict them in any format — not as prose, summary, or structured output. The completion notification arrives in a later turn; it is never something you write yourself. If the user asks before it lands, say the agent is still running — give status, not a guess.`:""}${BACKGROUND_SESSION_KEEPALIVE_GUIDANCE}
- ${CAN_CONTINUE_AGENT?`To continue a previously spawned agent, use ${SEND_MESSAGE_TOOL_NAME} with the agent's ID or name as the `to` field — that resumes it with full context. A new ${AGENT_TOOL_NAME} call`:`A previously spawned agent cannot be continued from here. Every ${AGENT_TOOL_NAME} call`} starts a fresh agent with no memory of prior runs${CAN_FORK_CONTEXT?' (except subagent_type: "fork")':""}, so the prompt must be self-contained.
- Each agent type's model, reasoning effort, and tool access are set in its definition (`.claude/agents/*.md` frontmatter, or the SDK `agents` option)${PROCESS_ENV.CLAUDE_CODE_SUBAGENT_MODEL_FORCE?"":"; the `model` parameter here overrides the definition for this one call"}.${SUBAGENT_EFFORT_GUIDANCE_NOTE}
- Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since a fresh agent is not aware of the user's intent${IS_DEFAULT_SUBAGENT_STEERING_MODE?`
- If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first.
- If the user specifies that they want you to run agents "in parallel", you MUST send a single message with multiple ${AGENT_TOOL_NAME} tool use content blocks. For example, if you need to launch both a build-validator agent and a test-runner agent in parallel, send a single message with both tool calls.`:""}
- With `isolation: "worktree"`, the worktree is automatically cleaned up if the agent makes no changes; otherwise the path and branch are returned in the result.${PARALLEL_WORKTREE_ISOLATION_NOTE?`
- ${PARALLEL_WORKTREE_ISOLATION_NOTE}`:""}${IS_REMOTE_ISOLATION_AVAILABLE_FN()?'\n- You can set `isolation: "remote"` to run the agent in a remote CCR environment. This is always a background task; you'll be notified when it completes. Use for long-running tasks that need a fresh sandbox.':""}${IS_IN_PROCESS_TEAMMATE_CONTEXT_FN()?`
- The run_in_background and name parameters are not available in this context. Only synchronous subagents are supported.`:IS_TEAMMATE_CONTEXT_FN()?`
- The name parameter is not available in this context — teammates cannot spawn other teammates. Omit it to spawn a subagent.`:""}${FORK_USAGE_GUIDELINES}${WRITING_SUBAGENT_PROMPTS_GUIDANCE}

${CAN_FORK_CONTEXT?FORK_CAPABLE_SUBAGENT_DELEGATION_EXAMPLES:NON_FORK_SUBAGENT_DELEGATION_EXAMPLES}
