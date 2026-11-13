<!--
name: "Data: Teleport stash MERGE_AUTOSTASH refusal"
description: "Refuses to stash when MERGE_AUTOSTASH exists and explains how to finish an intended merge or remove an unexpected record before retrying teleport"
ccVersion: "2.1.324"
variables:
  - "MERGE_AUTOSTASH_PATH"
-->
Nothing was stashed: this checkout has a MERGE_AUTOSTASH record. A stash would add the commit it names to your stash list, where `git stash pop` would apply it. If you started a merge that set your changes aside, finish or abort that merge. If you did not, a sandboxed command may have planted the record: delete ${MERGE_AUTOSTASH_PATH} if it exists, then run `git update-ref -d --no-deref MERGE_AUTOSTASH`. Neither applies anything. A branch or tag of that name causes this too: rename it. Then run /teleport again.
