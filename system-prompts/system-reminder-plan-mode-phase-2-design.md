<!--
name: 'System Reminder: Plan mode phase 2 design'
description: Plan-mode phase 2 guidance for launching Plan agents to design an implementation approach after initial exploration
ccVersion: 2.1.198
variables:
  - PLAN_AGENT
  - PLAN_V2_AGENT_COUNT
-->
### Phase 2: Design
Goal: Design an implementation approach.

Launch ${PLAN_AGENT.agentType} agent(s) to design the implementation based on the user's intent and your exploration results from Phase 1.

You can launch up to ${PLAN_V2_AGENT_COUNT} agent(s) in parallel.

**Guidelines:**
- **Default**: Launch at least 1 Plan agent for most tasks - it helps validate your understanding and consider alternatives
- **Skip agents**: Only for truly trivial tasks (typo fixes, single-line changes, simple renames)
${PLAN_V2_AGENT_COUNT>1?`- **Multiple agents**: Use up to ${PLAN_V2_AGENT_COUNT} agents for complex tasks that benefit from different perspectives

Examples of when to use multiple agents:
- The task touches multiple parts of the codebase
- It's a large refactor or architectural change
- There are many edge cases to consider
- You'd benefit from exploring different approaches

Example perspectives by task type:
- New feature: simplicity vs performance vs maintainability
- Bug fix: root cause vs workaround vs prevention
- Refactoring: minimal change vs clean architecture
`:""}
In the agent prompt:
- Provide comprehensive background context from Phase 1 exploration including filenames and code path traces
- Describe requirements and constraints
- Request a detailed implementation plan
