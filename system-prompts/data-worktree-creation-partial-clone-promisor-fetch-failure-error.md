<!--
name: "Data: Worktree creation partial clone promisor fetch failure error"
description: "Worktree creation error for a partial clone when objects needed for a commit could not be fetched from its promisor remote, with advice that depends on whether the remote is pinned or names its own upload-pack program"
ccVersion: "2.1.323"
variables:
  - "MISSING_OBJECT_IDS"
  - "BASE_COMMIT_SHORT_SHA"
  - "FORMAT_PROMISOR_REMOTE_NAME_FN"
  - "PROMISOR_REMOTE_NAME"
  - "SELECT_PROMISOR_FETCH_ADVICE_FN"
  - "REPOSITORY_PATH"
  - "IS_SHELL_SAFE_REMOTE_NAME_FN"
  - "FETCH_FAILURE_DETAIL"
-->
This repository is a partial clone, and ${MISSING_OBJECT_IDS.length===1?"an object":`${MISSING_OBJECT_IDS.length} objects`} needed for commit ${BASE_COMMIT_SHORT_SHA} could not be fetched from its promisor remote ${FORMAT_PROMISOR_REMOTE_NAME_FN(PROMISOR_REMOTE_NAME)} before checking it out (Claude Code checks worktrees out with git's on-demand fetching switched off). ${await SELECT_PROMISOR_FETCH_ADVICE_FN(REPOSITORY_PATH,[PROMISOR_REMOTE_NAME],{unpinned:`Check that the remote is reachable (${IS_SHELL_SAFE_REMOTE_NAME_FN(PROMISOR_REMOTE_NAME)?`for example "git fetch ${PROMISOR_REMOTE_NAME}"`:'run "git remote -v" to see which remotes are configured'}) and try again.`,pinned:"Check that the remote is reachable and try again.",ownUploadPackNamed:"The repository's config file names its own upload-pack program (a remote.<name>.uploadpack line), and Claude Code ran git's own instead. If you did not set that program, remove the line and try again. If you did, fetch the objects yourself and try again."})} ${FETCH_FAILURE_DETAIL}
