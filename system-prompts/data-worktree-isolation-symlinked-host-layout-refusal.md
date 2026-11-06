<!--
name: "Data: Worktree isolation symlinked host layout refusal"
description: "Error text refusing an isolation worktree whose host layout is symlinked or unresolved, with real-path recovery and tampering precautions"
ccVersion: "2.1.319"
variables:
  - "WORKTREE_PATH"
  - "WORKTREE_PARENT_PATH"
  - "PATH_DIRNAME_FN"
  - "HOST_CHECKOUT_PATH"
  - "HOST_CHECKOUT_DISPLAY_PATH"
-->
Refusing to use ${WORKTREE_PATH} as an isolation worktree: ${WORKTREE_PARENT_PATH} or ${PATH_DIRNAME_FN(WORKTREE_PARENT_PATH)} is a symbolic link or junction (or ${HOST_CHECKOUT_PATH}'s own path could not be resolved), so the worktree is not really inside ${HOST_CHECKOUT_PATH} and cannot be checked against ${HOST_CHECKOUT_PATH}'s own records. Claude Code never creates such a link. If you made it yourself, open the worktree by its real path instead, or replace the link with a real directory and recreate the worktree from ${HOST_CHECKOUT_DISPLAY_PATH}. If you did not, treat the worktree as tampered with: run no git in it, copy out what you need, delete it, and recreate it from ${HOST_CHECKOUT_DISPLAY_PATH}.
