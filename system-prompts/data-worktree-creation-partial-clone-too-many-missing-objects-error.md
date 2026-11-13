<!--
name: "Data: Worktree creation partial clone too many missing objects error"
description: "Worktree creation error for a partial clone whose commit needs more than about 1.5 million missing objects, advising a sparse worktree or, when safe, checking the commit out once in the main checkout"
ccVersion: "2.1.323"
variables:
  - "BASE_COMMIT_SHORT_SHA"
  - "SELECT_PROMISOR_FETCH_ADVICE_FN"
  - "REPOSITORY_PATH"
  - "PROMISOR_REMOTE_NAMES"
-->
This repository is a partial clone, and commit ${BASE_COMMIT_SHORT_SHA} needs more than about 1.5 million objects it does not have, too many to fetch before checking it out. ${await SELECT_PROMISOR_FETCH_ADVICE_FN(REPOSITORY_PATH,PROMISOR_REMOTE_NAMES,{unpinned:"Limit the worktree with the worktree.sparsePaths setting, or check that commit out once in the main checkout so git fetches them, then try again.",pinned:"Limit the worktree with the worktree.sparsePaths setting, then try again.",ownUploadPackNamed:"Limit the worktree with the worktree.sparsePaths setting, then try again. Do not check the commit out in the main checkout first: git would start the upload-pack program that the repository's config file names."})}
