<!--
name: "Data: Worktree isolation redirected git directory refusal"
description: "Error text refusing a registered worktree whose .git points somewhere else, warning against git worktree repair and appending manual registry cleanup guidance"
ccVersion: "2.1.319"
variables:
  - "WORKTREE_PATH"
  - "HOST_WORKTREE_REGISTRATION"
  - "FORMAT_WORKTREE_REGISTRY_ENTRY_FN"
  - "REGISTERED_WORKTREE_ADMIN_DIR_PATH"
  - "SAFE_DISPLAY_PATH_FN"
  - "WORKTREE_GIT_IDENTITY"
  - "WORKTREE_REGISTRY_CLEANUP_GUIDANCE"
-->
Refusing to use ${WORKTREE_PATH} as an isolation worktree: ${HOST_WORKTREE_REGISTRATION.host} registers it (${FORMAT_WORKTREE_REGISTRY_ENTRY_FN(REGISTERED_WORKTREE_ADMIN_DIR_PATH)}), but its .git now leads to ${SAFE_DISPLAY_PATH_FN(WORKTREE_GIT_IDENTITY.gitDir,"another directory (its path is not repeated here)")} instead of that entry. Unless you re-pointed it yourself, treat the worktree as tampered with: run no git in it, and do not re-link it with git worktree repair, which points each of that checkout's worktrees, this one included, at whichever entry names it — code running in a worktree can add such an entry. Copy out what you need and delete it. ${WORKTREE_REGISTRY_CLEANUP_GUIDANCE}
