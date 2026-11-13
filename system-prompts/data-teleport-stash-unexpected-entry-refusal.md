<!--
name: "Data: Teleport stash unexpected entry refusal"
description: "Explains how to inspect and recover the top stash when its entries change unexpectedly or cannot be read, with extra repair instructions for unsafe Git files"
ccVersion: "2.1.324"
variables:
  - "UNSAFE_GIT_DIR_ENTRY"
  - "TRUNCATE_PATH_FN"
  - "REPLACE_CONTROL_CHARACTERS_FN"
  - "STASH_SHOW_COMMAND"
  - "GIT_BASH_DISPLAY_NOTE"
-->
the stash list holds something /teleport did not put there, or could not be read, so /teleport stopped. ${UNSAFE_GIT_DIR_ENTRY===null?"":`Before any git stash command: ${TRUNCATE_PATH_FN(REPLACE_CONTROL_CHARACTERS_FN(UNSAFE_GIT_DIR_ENTRY),200)} (or a folder on the way to it) is a link, names another ref, cannot be read, or is not a plain file, and git would read and write through it. If you did not set this up, remove the link, or a stash file that reads "ref: …" (the file a link leads to is not touched). Never delete HEAD itself, and at the object store or the ref table first move what a link leads to back into a plain folder at that name, since it may be your repository's own objects or refs. `}Do not run `git stash pop` yet: a sandboxed command may have planted an entry through a MERGE_AUTOSTASH record, and `git stash list` can hide that entry or show it under this stash's name. Run `${STASH_SHOW_COMMAND} | cat -v` (${GIT_BASH_DISPLAY_NOTE}), which shows the changes pop would make. If they are the changes you just made, pop. If they are an older stash of yours, or git finds no stash, leave it: this stash's entry is gone. If they are anything else, run `git stash drop`, which drops that entry, and run that `git stash show` again.
