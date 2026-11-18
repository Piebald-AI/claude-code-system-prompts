<!--
name: "Data: Self-hosted runner disableAllHooks warning"
description: "Explains how the runner reports repo hook settings and warns when a wrapper can drop server-supplied hooks"
ccVersion: "2.1.328"
variables:
  - "HAS_RUNNER_MANAGED_HOOKS"
-->
[runner:session] A repo's .claude/settings.json or settings.local.json sets disableAllHooks:true. ${HAS_RUNNER_MANAGED_HOOKS?"It turns off the repo's own hooks, not the server-supplied ones or those of your settings.json, where managed settings can be read.":"This session's Claude Code is started by your --exec-path wrapper or 'command' lifecycle hook: if it is older than this runner, or lacks CLAUDE_CODE_REMOTE, it drops the server-supplied hooks, and Claude Tag may not post its reply. Update it, and let the wrapper or hook pass CLAUDE_CODE_REMOTE."}
