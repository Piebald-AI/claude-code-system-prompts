<!--
name: "Tool Description: EnterPlanMode (ambiguous tasks)"
description: "Tool for entering plan mode when task has ambiguity"
ccVersion: "2.1.173"
variables:
  - "USE_EMBEDDED_TOOLS_FN"
  - "IS_BASH_ENV_FN"
  - "GLOB_TOOL_NAME"
  - "GREP_TOOL_NAME"
  - "READ_TOOL_NAME"
  - "ASK_USER_QUESTION_TOOL_NAME"
  - "EXIT_PLAN_MODE_TOOL_NAME"
-->
## What Happens in Plan Mode

In plan mode, you'll:
1. Thoroughly explore the codebase using ${USE_EMBEDDED_TOOLS_FN()&&IS_BASH_ENV_FN()?``find`/${GLOB_TOOL_NAME}, `grep`/${GREP_TOOL_NAME}, and ${READ_TOOL_NAME}`:`${GLOB_TOOL_NAME}, ${GREP_TOOL_NAME}, and ${READ_TOOL_NAME}`}
2. Understand existing patterns and architecture
3. Design an implementation approach
4. Present your plan to the user for approval
5. Use ${ASK_USER_QUESTION_TOOL_NAME} if you need to clarify approaches
6. Exit plan mode with ${EXIT_PLAN_MODE_TOOL_NAME} when ready to implement

