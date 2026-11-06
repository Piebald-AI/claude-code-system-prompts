<!--
name: "Data: Worktree isolation unverified host repository refusal"
description: "Error text refusing an isolation worktree when its enclosing checkout cannot be verified, listing broken git metadata causes and ways to repair or avoid that layout"
ccVersion: "2.1.319"
variables:
  - "WORKTREE_PATH"
  - "ISOLATION_WORKTREES_DIRECTORY_PATH"
  - "HOST_CHECKOUT_PATH"
  - "SAFE_DISPLAY_PATH_FN"
  - "PATH_JOIN_FN"
-->
Refusing to use ${WORKTREE_PATH} as an isolation worktree: it is under ${ISOLATION_WORKTREES_DIRECTORY_PATH}, so ${HOST_CHECKOUT_PATH} must list it as a worktree, but ${HOST_CHECKOUT_PATH}'s own repository could not be confirmed. Usual causes: its .git is a pointer file or symlink whose target does not name it back (a --separate-git-dir clone, for one) or is empty or left over, a stray file named commondir in its git directory (for an ordinary checkout, ${SAFE_DISPLAY_PATH_FN(PATH_JOIN_FN(HOST_CHECKOUT_PATH,".git","commondir"),"the commondir file in its .git")} — deleting that one file is the fix), or ${HOST_CHECKOUT_PATH} itself sitting in another checkout's .claude/worktrees. Fix that (or remove a left-over .git file) and retry, or create the worktree somewhere that is not inside ${SAFE_DISPLAY_PATH_FN(ISOLATION_WORKTREES_DIRECTORY_PATH,"that directory")}.
