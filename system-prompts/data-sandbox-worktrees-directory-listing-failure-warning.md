<!--
name: "Data: Sandbox worktrees directory listing failure warning"
description: "Warning logged when the sandbox cannot list a repository's worktrees folder, saying whether sandboxed commands are write-denied under it or may change linked worktrees' commondir and config.worktree files until it can be listed again and the sandbox config is rebuilt"
ccVersion: "2.1.323"
variables:
  - "WORKTREES_DIRECTORY_PATH"
  - "ERROR_CODE"
  - "GET_ERROR_MESSAGE_FN"
  - "CAUGHT_ERROR"
  - "SHOULD_WRITE_DENY_WORKTREES_DIRECTORY"
-->
[Sandbox] cannot list ${WORKTREES_DIRECTORY_PATH} (${ERROR_CODE??GET_ERROR_MESSAGE_FN(CAUGHT_ERROR)}); ${SHOULD_WRITE_DENY_WORKTREES_DIRECTORY?"sandboxed commands cannot write under it until it can be listed again and the sandbox config is rebuilt (restarting Claude Code does this)":"not write-denying it on Windows, where the deny would stay in the folder's permissions after the listing works again. Until it can be listed again and the sandbox config is rebuilt (restarting Claude Code does this), sandboxed commands can change its linked worktrees' commondir and config.worktree files"}.
