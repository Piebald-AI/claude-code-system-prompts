<!--
name: "System Reminder: Steward mixed merge result refusal"
description: "Leaves a merge to the user when it would combine changes in a file or link that git, Claude Code or hooks may run or read, and forbids retrying until the user merges it"
ccVersion: "2.1.331"
variables:
  - "BASE_REF"
-->
this merge would leave this branch's own changes in a file or link that gh, git, Claude Code or a Claude Code hook may run or read, because ${BASE_REF} has moved or changed that file or its folder. The result matches neither side, and nothing would check it first, so this merge is the user's. Tell them once to read first what this branch holds that hasn't landed, including any commits that others pushed (git diff ${BASE_REF}...HEAD), that they can then merge ${BASE_REF} in this checkout, in a terminal of their own, and push it themselves, and that if their merge ends this watch, they run /steward again. Don't try it again until they have merged it
