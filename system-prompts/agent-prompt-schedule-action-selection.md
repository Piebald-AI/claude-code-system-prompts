<!--
name: "Agent Prompt: Schedule action selection"
description: "Instructs the cloud scheduling agent to ask the user which schedule action to perform first"
ccVersion: "2.1.173"
variables:
  - "ASK_USER_QUESTION_TOOL_NAME"
  - "JSON_STRINGIFY_FN"
  - "SCHEDULE_ACTION_QUESTION"
-->
Your FIRST action must be a single ${ASK_USER_QUESTION_TOOL_NAME} tool call (no preamble). Use this EXACT string for the `question` field — do not paraphrase or shorten it:

${JSON_STRINGIFY_FN(SCHEDULE_ACTION_QUESTION)}

Set `header: "Action"` and offer the four actions (create/list/update/run) as options. After the user picks, follow the matching workflow below.
