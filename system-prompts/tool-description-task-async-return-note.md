<!--
name: 'Tool Description: Task (async return note)'
description: Message returned to the model when a subagent launched successfully
ccVersion: 2.0.14
variables:
  - LAUNCHED_AGENT_INFO
  - AgentOutputTool
-->
Async agent launched successfully.
agentId: ${LAUNCHED_AGENT_INFO.agentId} (This is an internal ID for your use, do not mention it to the user. Use this ID to retrieve results with ${AgentOutputTool} when the agent finishes). 
The agent is currently working in the background. If you have other tasks you you should continue working on them now. Wait to call ${AgentOutputTool} until either:
- If you want to check on the agent's progress - call ${AgentOutputTool} with block=false to get an immediate update on the agent's status
- If you run out of things to do and the agent is still running - call ${AgentOutputTool} with block=true to idle and wait for the agent's result (do not use block=true unless you completely run out of things to do as it will waste time).
