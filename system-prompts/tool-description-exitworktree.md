<!--
name: "Tool Description: ExitWorktree"
description: "Describes ExitWorktree, which returns the session to its original working directory and either keeps or removes the session-created worktree"
ccVersion: "2.1.330"
variables:
  - "IS_WORKING_COPY_BACKEND"
-->
Exit a worktree session created by EnterWorktree and return the session to the original working directory.

## Scope

This tool ONLY operates on worktrees created by EnterWorktree in this session. It will NOT touch:
- Worktrees you created manually${IS_WORKING_COPY_BACKEND?"":" with `git worktree add`"}
- Worktrees from a previous session (even if created by EnterWorktree then)
- The directory you're in if EnterWorktree was never called

If called outside an EnterWorktree session, the tool is a **no-op**: it reports that no worktree session is active and takes no action. Filesystem state is unchanged.

## When to Use

- The user explicitly asks to "exit the worktree", "leave the worktree", "go back", or otherwise end the worktree session
- Do NOT call this proactively — only when the user asks

## Parameters

- `action` (required): `"keep"` or `"remove"`
  - `"keep"` — leave the worktree directory ${IS_WORKING_COPY_BACKEND?"":"and branch "}intact on disk. Use this if the user wants to come back to the work later, or if there are changes to preserve.
  - `"remove"` — delete the worktree directory${IS_WORKING_COPY_BACKEND?", and its branch too where Claude Code made one":", and its branch too unless a hook made the worktree or git refuses the delete"}. Use this for a clean exit when the work is done or abandoned.
- `discard_changes` (optional, default false): only meaningful with `action: "remove"`. If the worktree has uncommitted files or ${IS_WORKING_COPY_BACKEND?"unpublished work, or its state is unknown":"commits not on the original branch"}, the tool will REFUSE to remove it unless this is set to `true`. If the tool returns an error listing changes, confirm with the user before re-invoking with `discard_changes: true`. The tool also refuses while a task may be running in the worktree: wait for the task, or ask the user before stopping it, then call the tool again, or use `keep`.

## Behavior

- Restores the session's working directory to where it was before EnterWorktree
- Clears CWD-dependent caches (system prompt sections, memory files, plans directory) so the session state reflects the original directory
- If a tmux session was attached to the worktree: killed on `remove`, left running on `keep` (its name is returned so the user can reattach)
- Once exited, EnterWorktree can be called again to create a fresh worktree
