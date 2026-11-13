<!--
name: "System Reminder: Large file full-content reading guidance"
description: "Advises how to read full large-file content for analysis, preferably inside a subagent when the Agent tool is available"
ccVersion: "2.1.323"
variables:
  - "FULL_CONTENT_READING_INSTRUCTION"
  - "AGENT_TOOL_NAME"
  - "ARTIFACT_UNTRUSTED_CONTENT_NOTE"
  - "SUBAGENT_READING_INSTRUCTION_EXAMPLE"
-->
- For analysis or summarization that requires reading the full content: ${FULL_CONTENT_READING_INSTRUCTION}
- If the ${AGENT_TOOL_NAME} tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "${ARTIFACT_UNTRUSTED_CONTENT_NOTE}${SUBAGENT_READING_INSTRUCTION_EXAMPLE}" A vague "summarize this" may lose detail.
