<!--
name: "Data: Teleport stash unsafe ref file refusal"
description: "Teleport error saying nothing was stashed because a ref file or a folder on the way to it is a link, has a second name, names another ref, or is not a plain file, with safe repair steps and a warning never to delete HEAD or plain ref files"
ccVersion: "2.1.323"
variables:
  - "GIT_DIR_ENTRY_PATH"
-->
Nothing was stashed: ${GIT_DIR_ENTRY_PATH} (or a folder on the way to it) is a link, has a second name, names another ref, cannot be read, or is not a plain file, so git could write the stash's records somewhere else. If you did not set this up: delete the link, or the file that reads "ref: …" (the file a link leads to is not touched), but never delete HEAD itself, which git needs and which normally reads "ref: …"; for a file with a second name, copy it to a new name in the same folder and move the copy back over it, which keeps its contents. Do not delete a plain file there: it may hold your branches or your stash list. If the setup is intended (git-new-workdir links these names), stash or commit your changes yourself. Then run /teleport again.
