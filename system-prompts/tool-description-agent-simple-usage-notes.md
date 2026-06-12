<!--
name: 'Tool Description: Agent (simple usage notes)'
description: Simplified usage notes for the Agent tool, including when to delegate, fork behavior, resumption, worktree isolation, background execution, parallel launches, and context restrictions
ccVersion: 2.1.176
variables:
  - TOOL_BASE_DESCRIPTION
  - HAS_PRO_RESTRICTION_NOTE
  - CAN_FORK_CONTEXT
  - SEND_MESSAGE_TOOL_NAME
  - AGENT_TOOL_NAME
  - RUN_IN_BACKGROUND_NOTE
  - PARALLEL_AGENTS_NOTE
  - CONTEXT_RESTRICTION_NOTE
-->
${TOOL_BASE_DESCRIPTION}${HAS_PRO_RESTRICTION_NOTE?"":`

## When to use

Reach for this when the task matches an available agent type, when you have independent work to run in parallel, or when answering would mean reading across several files — delegate it and you keep the conclusion, not the file dumps. For a single-fact lookup where you already know the file, symbol, or value, search directly. Once you've delegated a search, don't also run it yourself — wait for the result.`}${CAN_FORK_CONTEXT?`

A fork runs in the background and keeps its tool output out of your context. If you are the fork, execute directly — don't re-delegate.`:""}

- The agent's final message is returned to you as the tool result; it is not shown to the user — relay what matters.
- Use ${SEND_MESSAGE_TOOL_NAME} with the agent's ID or name to continue a previously spawned agent with its context intact; a new ${AGENT_TOOL_NAME} call starts fresh${CAN_FORK_CONTEXT?' (except subagent_type: "fork", which inherits your context)':""}.
- `isolation: "worktree"` gives the agent its own git worktree (auto-cleaned if unchanged).${RUN_IN_BACKGROUND_NOTE}${PARALLEL_AGENTS_NOTE}${CONTEXT_RESTRICTION_NOTE}
