<!--
name: "System Reminder: Subagent write blocked pending worktree isolation"
description: "Tells a subagent that its write to the shared checkout was blocked because its parent background session has not isolated into a worktree yet, and lists how to proceed (re-spawn with worktree isolation, have the parent enter a worktree, or edit inside a linked worktree) plus how to disable the guard"
ccVersion: "2.1.323"
variables:
  - "HAS_RESOLVED_PARENT_CWD"
  - "ENTER_WORKTREE_TOOL_NAME"
-->
This subagent's parent bg session hasn't isolated yet, so writes to the shared checkout are blocked. Re-spawn this agent with `isolation: "worktree"`${HAS_RESOLVED_PARENT_CWD?`, have the parent call ${ENTER_WORKTREE_TOOL_NAME} before spawning, or make the edit inside a linked git worktree made for this task — paths inside a worktree are accepted`:`, or have the parent call ${ENTER_WORKTREE_TOOL_NAME} before spawning`}. (To disable this guard for this repo, set `"worktree": {"bgIsolation": "none"}` in .claude/settings.json.)
