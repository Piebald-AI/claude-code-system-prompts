<!--
name: "Agent Prompt: /code-review workflow routing"
description: "Routes eligible /code-review runs through the background code-review workflow and conditionally adds findings reporting, GitHub commenting, fix application, and artifact publishing"
ccVersion: "2.1.212"
variables:
  - "CODE_REVIEW_ROUTING_NOTICE"
  - "CODE_REVIEW_EFFORT_LEVEL"
  - "WORKFLOW_TOOL_NAME"
  - "JSON_STRINGIFY_FN"
  - "CODE_REVIEW_WORKFLOW_NAME"
  - "CODE_REVIEW_WORKFLOW_ARGS"
  - "HAS_REPORT_FINDINGS_TOOL"
  - "REPORT_FINDINGS_TOOL_NAME"
  - "HAS_COMMENT_FLAG"
  - "GITHUB_COMMENT_INSTRUCTIONS_BLOCK"
  - "HAS_FIX_FLAG"
  - "FIX_APPLICATION_INSTRUCTIONS_FN"
  - "FINDINGS_REREPORT_INSTRUCTIONS_BLOCK"
  - "ARTIFACT_PUBLISHING_INSTRUCTIONS_BLOCK"
  - "EMPTY_STRING"
-->
${CODE_REVIEW_ROUTING_NOTICE}Run the workflow-backed code review at ${CODE_REVIEW_EFFORT_LEVEL} effort instead of reviewing inline.

Invoke: ${WORKFLOW_TOOL_NAME}({ name: ${JSON_STRINGIFY_FN(CODE_REVIEW_WORKFLOW_NAME)}, args: ${JSON_STRINGIFY_FN(CODE_REVIEW_WORKFLOW_ARGS)} })

Everything after the level in the args string is passed to the workflow as the review target / instructions. If the user gave additional instructions for this review elsewhere in the conversation (a scope restriction, files to focus on, things to skip), append them to the args string so the workflow honors them.

The workflow runs the same finder angles and verify pass as the inline review, in the background; the verified findings arrive as a task notification. When they arrive, ${HAS_REPORT_FINDINGS_TOOL?`call ${REPORT_FINDINGS_TOOL_NAME} once with {level, findings} from the result payload (most-severe first; empty array if nothing survived). Give each finding a `short_summary`: the claim compressed to ≤60 characters, no rationale or consequence clause. Do not also print the findings as text.`:"present the findings ranked most-severe first (or note that nothing survived verification)."}${HAS_COMMENT_FLAG?GITHUB_COMMENT_INSTRUCTIONS_BLOCK:""}${HAS_FIX_FLAG?FIX_APPLICATION_INSTRUCTIONS_FN(HAS_REPORT_FINDINGS_TOOL):""}${HAS_REPORT_FINDINGS_TOOL?FINDINGS_REREPORT_INSTRUCTIONS_BLOCK:""}${ARTIFACT_PUBLISHING_INSTRUCTIONS_BLOCK}${EMPTY_STRING}
