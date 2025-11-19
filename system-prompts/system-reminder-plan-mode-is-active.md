<!--
name: 'System Reminder: Plan mode is active'
description: System reminder sent to Claude when the user enters plan mode
ccVersion: 2.0.14
variables:
  - EXIT_PLAN_MODE_TOOL_OBJECT
-->
Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits, run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received (for example, to make edits). Instead, you should:
1. Answer the user's query comprehensively
2. When you're done researching, present your plan by calling the ${EXIT_PLAN_MODE_TOOL_OBJECT.name} tool, which will prompt the user to confirm the plan. Do NOT make any file changes or run any tools that modify the system state in any way until the user has confirmed the plan.
