<!--
name: "System Reminder: Parent must enter worktree before spawning"
description: "Blocks writes to the shared checkout and tells the parent to enter a worktree before spawning the agent"
ccVersion: "2.1.330"
variables:
  - "ENTER_WORKTREE_TOOL_NAME"
  - "HAS_RESOLVED_PARENT_CWD"
-->
This subagent's parent bg session hasn't isolated yet, so writes to the shared checkout are blocked. Have the parent call ${ENTER_WORKTREE_TOOL_NAME} before spawning${HAS_RESOLVED_PARENT_CWD?", or make the edit inside a linked git worktree made for this task — paths inside a worktree are accepted":""}. (To disable this guard for this repo, set `"worktree": {"bgIsolation": "none"}` in .claude/settings.json.)
