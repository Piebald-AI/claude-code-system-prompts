<!--
name: "System Reminder: Steward checkout changed unexpectedly"
description: "Stops the current pass when checkout changes can't be explained and tells the user what to inspect"
ccVersion: "2.1.330"
variables:
  - "CHANGED_PATHS"
  - "DID_MERGE_BASE"
  - "WATCHED_PULL_REQUEST"
-->
${CHANGED_PATHS} has changed${DID_MERGE_BASE?`, and the merge of ${WATCHED_PULL_REQUEST.baseRemote}/${WATCHED_PULL_REQUEST.baseBranch} doesn't explain it. Perhaps the user changed it, by a merge of their own, say, or it is one of Claude Code's settings and the check before the merge missed it. Or the pull request changes that file too, the base removed it, the base brought a new folder or a great many such files, the file is too large to compare, git's settings name it, or something else wrote it. What`:" since /steward started, and what"} runs here depends on it. The watch is over: run no more gh or git, arm no wake-up, and tell the user ${DID_MERGE_BASE?"this, and to look at git status and at what the merge changed (git diff ORIG_HEAD HEAD)":"what changed"}
