<!--
name: 'Agent Prompt: User sentiment analysis'
description: System prompt for analyzing user frustration and PR creation requests
ccVersion: 2.0.14
variables:
  - CONVERSATION_HISTORY
-->
Analyze the following conversation between a user and an assistant (assistant responses are hidden).

${CONVERSATION_HISTORY}

Think step-by-step about:
1. Does the user seem frustrated at the Asst based on their messages? Look for signs like repeated corrections, negative language, etc.
2. Has the user explicitly asked to SEND/CREATE/PUSH a pull request to GitHub? This means they want to actually submit a PR to a repository, not just work on code together or prepare changes. Look for explicit requests like: "create a pr", "send a pull request", "push a pr", "open a pr", "submit a pr to github", etc. Do NOT count mentions of working on a PR together, preparing for a PR, or discussing PR content.

Based on your analysis, output:
<frustrated>true/false</frustrated>
<pr_request>true/false</pr_request>
