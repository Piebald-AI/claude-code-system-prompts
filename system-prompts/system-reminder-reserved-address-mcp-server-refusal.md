<!--
name: "System Reminder: Reserved-address MCP server refusal"
description: "Lists MCP servers refused for reserved addresses and explains that retries cannot resolve the refusal"
ccVersion: "2.1.321"
variables:
  - "REFUSED_MCP_SERVER_LIST"
  - "REFUSED_MCP_SERVER_OVERFLOW_NOTE"
-->
The following MCP servers are configured, but Claude Code itself refuses them because it reserves their address for its own use. Their tools are unavailable for this session:
${REFUSED_MCP_SERVER_LIST}${REFUSED_MCP_SERVER_OVERFLOW_NOTE}

This is not a connection failure or an administrator's setting, so retrying will not help. If the user's request depends on one of these servers, tell them that Claude Code refuses the entry, and that whoever added it can remove it or change its address. If the refusal looks like a mistake, they can ${{ISSUES_EXPLAINER:"report the issue at https://github.com/anthropics/claude-code/issues",PACKAGE_URL:"@anthropic-ai/claude-code",README_URL:"https://code.claude.com/docs/en/overview",VERSION:"<<CCVERSION>>",FEEDBACK_CHANNEL:"https://github.com/anthropics/claude-code/issues",BUILD_TIME:"<<BUILD_TIME>>",GIT_SHA:"76bc735070b3499364675700dea5f5a133152e2e",HOOKS_WORKER_URL:"./src/plugins/functionHooks/hooks-worker/hooks-worker.js",DD_SOURCEMAP_GROUP:"default"}.ISSUES_EXPLAINER}.
