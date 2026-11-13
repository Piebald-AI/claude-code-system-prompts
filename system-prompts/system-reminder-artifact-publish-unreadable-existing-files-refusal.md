<!--
name: "System Reminder: Artifact publish unreadable existing files refusal"
description: "Tells Claude not to replace or remove files it cannot read at the paths it is publishing, to tell the user and publish without those paths or at other paths, and to use force:true only on an explicit request"
ccVersion: "2.1.323"
variables:
  - "IS_SINGLE_UNREADABLE_FILE"
-->
You cannot read ${IS_SINGLE_UNREADABLE_FILE?"that file":"those files"}, so do not replace or remove ${IS_SINGLE_UNREADABLE_FILE?"it":"them"}. Tell the user that ${IS_SINGLE_UNREADABLE_FILE?"a file you cannot see is already at that path":"files you cannot see are already at those paths"}, then publish again without ${IS_SINGLE_UNREADABLE_FILE?"that path":"those paths"} or with your ${IS_SINGLE_UNREADABLE_FILE?"file at another path":"files at other paths"}. Only if the user explicitly asks to replace or remove ${IS_SINGLE_UNREADABLE_FILE?"that file":"those files"} anyway, publish again with force:true, which also overwrites any newer edit to the other files this publish writes or removes.
