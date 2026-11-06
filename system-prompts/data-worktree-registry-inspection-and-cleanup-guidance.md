<!--
name: "Data: Worktree registry inspection and cleanup guidance"
description: "Recovery guidance requiring manual removal of planted links and duplicate or stray registry entries before pruning, unlocking, and recreating a worktree"
ccVersion: "2.1.319"
variables:
  - "HOST_CHECKOUT_DISPLAY_PATH"
  - "WORKTREE_REGISTRY_DISPLAY_PATH"
-->
Before any git worktree command in ${HOST_CHECKOUT_DISPLAY_PATH}, look through ${WORKTREE_REGISTRY_DISPLAY_PATH} by hand: git keeps one plain directory there per linked worktree, the one that worktree's .git file names (gitdir: followed by its path). Remove any symbolic link with unlink (never rm with a trailing slash, which follows the link) and delete every entry that is not named by the .git file of a worktree you have, a second entry for the same worktree included — code running in a worktree can plant any of these, git worktree prune follows a planted link and empties the directory it points to, and of two entries naming one worktree it keeps whichever name sorts first. Then run git worktree prune in ${HOST_CHECKOUT_DISPLAY_PATH}; if git worktree list there still shows this path, run git worktree unlock on it and prune again, until it is no longer listed. Then recreate the worktree (on a new branch if git says the old one is already used by a worktree elsewhere).
