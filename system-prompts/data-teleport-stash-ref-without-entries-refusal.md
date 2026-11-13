<!--
name: "Data: Teleport stash ref without entries refusal"
description: "Refuses to stash when refs/stash exists without listed entries and provides inspection and recovery commands before teleport is retried"
ccVersion: "2.1.324"
variables:
  - "STASH_SHOW_COMMAND"
  - "GIT_BASH_DISPLAY_NOTE"
-->
Nothing was stashed: refs/stash is set, but git lists no stash entries, so /teleport could not check what a stash adds. A sandboxed command may have caused this, so do not run `git stash pop` yet. Run `${STASH_SHOW_COMMAND} | cat -v` (${GIT_BASH_DISPLAY_NOTE}). If it shows changes you did not make, run `git stash drop` and look again. If it says refs/stash@{0} is not a valid reference, run `git update-ref -d refs/stash`; `git fsck --lost-found` then lists that commit as dangling. If it prints any other error, or shows only your own changes, run `git stash --include-untracked`, which clears this. Then run /teleport again.
