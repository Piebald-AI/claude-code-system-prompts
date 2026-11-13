<!--
name: "Data: Worktree creation outside-repository write refusal"
description: "Worktree creation refusal when git could write outside the repository through a git folder entry that is a link, a symbolic ref or otherwise not a plain file, noting which checkout tools make such entries and to inspect the entry before changing anything"
ccVersion: "2.1.323"
variables:
  - "WORKTREE_NAME"
  - "FORMAT_GIT_DIR_ENTRY_FN"
  - "UNSAFE_GIT_DIR_ENTRY"
-->
Cannot create worktree "${WORKTREE_NAME}": git could write outside this repository through ${FORMAT_GIT_DIR_ENTRY_FN(UNSAFE_GIT_DIR_ENTRY)} or a folder on the way to it, which is a link, a symbolic ref, a list naming another path or another entry that is not a plain file, or could not be checked. Checkouts made by git-new-workdir or older versions of Android's repo tool, and copies made with hard links (with cp -al, say), have such entries: use a plain clone instead. Otherwise a command run earlier may have planted it: look at that entry before changing anything.
