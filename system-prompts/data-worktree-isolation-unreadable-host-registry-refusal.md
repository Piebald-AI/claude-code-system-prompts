<!--
name: "Data: Worktree isolation unreadable host registry refusal"
description: "Error text refusing an isolation worktree whose host registry cannot be read safely and requiring manual inspection before git worktree commands"
ccVersion: "2.1.319"
variables:
  - "WORKTREE_PATH"
  - "HOST_CHECKOUT_PATH"
  - "WORKTREE_REGISTRY_PATH"
  - "HOST_CHECKOUT_DISPLAY_PATH"
-->
Refusing to use ${WORKTREE_PATH} as an isolation worktree: the list of linked worktrees ${HOST_CHECKOUT_PATH} keeps in ${WORKTREE_REGISTRY_PATH} could not be read in full, or something other than a plain directory (a symbolic link, say) stands in its place, so whether it registers this worktree could not be checked. Look at it by hand before any git worktree command in ${HOST_CHECKOUT_DISPLAY_PATH}: if a symbolic link stands there, remove it with unlink — not rm with a trailing slash, and not git worktree prune, which both follow the link into the directory it points to (code running in a worktree can plant one); if it is a directory that cannot be read or holds more entries than git made for your worktrees, make it readable and delete by hand every entry that is not named by the .git file of a worktree you have; then retry.
