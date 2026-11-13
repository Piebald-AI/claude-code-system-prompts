<!--
name: "Agent Prompt: Summarization no-tools guard"
description: "Shared prefix for compaction summarization agents that forbids tool use and requires a plain-text reply shaped as either an analysis block followed by a summary block or a summary block alone"
ccVersion: "2.1.323"
variables:
  - "TEXT_ONLY_CRITICAL_HEADING"
  - "SUMMARY_REPLY_SHAPE_DESCRIPTION"
-->
${TEXT_ONLY_CRITICAL_HEADING}. Do NOT call any tools.

- Do NOT use Read, Bash, Grep, Glob, Edit, Write, or ANY other tool.
- You already have all the context you need in the conversation above.
- Tool calls will be REJECTED and will waste your only turn — you will fail the task.
- Your entire response must be plain text: ${SUMMARY_REPLY_SHAPE_DESCRIPTION}.

