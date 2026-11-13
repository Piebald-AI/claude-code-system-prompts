<!--
name: "Data: Teleport stash index update failure error"
description: "Teleport error saying the changes were stashed but the checkout's index could not be updated to match, so git status will show phantom changes, with steps to check .git/index, run git reset, and run /teleport again"
ccVersion: "2.1.323"
variables:
  - "ERROR_CODE"
  - "CAUGHT_ERROR"
  - "INDEX_INSTALL_ERROR_CLASS"
  - "INDEX_INSTALL_STEP_LABELS"
  - "INDEX_INSTALL_STEP"
-->
Your changes were stashed (`git stash list` shows them), but this checkout's index could not be updated to match (${ERROR_CODE??(CAUGHT_ERROR instanceof INDEX_INSTALL_ERROR_CLASS?CAUGHT_ERROR.message:`the ${INDEX_INSTALL_STEP_LABELS[INDEX_INSTALL_STEP]} failed`)}), so `git status` will show changes that are not there. First check that .git/index is a plain file: if it is a link, delete it, because git would write to the file it leads to. Then run `git reset` in this checkout (if that fails, check that .git/index is not a folder and that you can write to the .git folder; if git says index.lock exists and no other git is running, delete that file first) and run /teleport again; your changes stay in the stash.
