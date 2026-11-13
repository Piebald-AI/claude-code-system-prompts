<!--
name: "Data: Teleport stash unsafe object store or ref table refusal"
description: "Teleport error saying nothing was stashed because an object store or ref table entry is a link, unreadable or otherwise not what git keeps there, with guidance not to delete what it leads to and to stash or commit manually before running /teleport again"
ccVersion: "2.1.323"
variables:
  - "GIT_DIR_ENTRY_PATH"
-->
Nothing was stashed: ${GIT_DIR_ENTRY_PATH} is a link, could not be read, is not the plain folder or file git keeps there, or holds a name or a number of entries git would not make, so git could write the stash's new objects or refs somewhere else. If you did not set this up: do not just delete a link at the object store, one of its folders or the ref table, since what it leads to may be your repository's own objects or refs; move them back into a plain folder at that name (for the alternates file, a plain file). If the store is shared like this on purpose, stash or commit your changes yourself. Then run /teleport again.
