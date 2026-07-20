<!--
name: "Tool Description: Agent (when to launch subagents)"
description: "Describes _when_ to use the Agent tool - for launching specialized subagent subprocesses to autonomously handle complex multi-step tasks"
ccVersion: "2.1.178"
variables:
  - "AGENT_TYPES_BLOCK"
  - "CAN_FORK_CONTEXT"
  - "AGENT_TOOL_NAME"
-->
Launch a new agent to handle complex, multi-step tasks. Each agent type has specific capabilities and tools available to it.

Available agent types are listed in <system-reminder> messages in the conversation.${AGENT_TYPES_BLOCK}

${CAN_FORK_CONTEXT?`When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type to select an agent: `"fork"` forks yourself (the fork inherits your full conversation context and always runs on your model — a `model` override is ignored); any other type — or omitting it — starts a fresh agent (general-purpose by default).`:`When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type parameter to select which agent type to use. If omitted, the general-purpose agent is used.`}
