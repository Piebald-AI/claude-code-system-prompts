<!--
name: "Skill: Code Review unavailable target diff fallback"
description: "Reviews the checked-out branch when a target diff can't be read, states the fallback and stops when no target or diff exists"
ccVersion: "2.1.329"
variables:
  - "WILL_RUN_AS_FORK"
  - "REPORT_FINDINGS_TOOL_NAME"
  - "REVIEW_DIFF_FAILURE_NOTE"
  - "REVIEW_TARGET_KIND"
-->
If that leaves you without the diff, because a command was refused or failed, run the `git diff` commands below as if no target had been passed, and review the checked-out branch instead. ${WILL_RUN_AS_FORK?"Then open your final reply with these two sentences, word for word, above the findings, and keep the json fence where the output below shows one":`Then write these two sentences, word for word, before the ${REPORT_FINDINGS_TOOL_NAME} call`}: "${REVIEW_DIFF_FAILURE_NOTE}. This review is of the checked-out branch instead, which may not be that ${REVIEW_TARGET_KIND}."

Two cases end the review instead: the command answers that there is no such ${REVIEW_TARGET_KIND}, or, falling back, you find that the checked-out branch has no diff. Then reply with only one sentence that says which, and no list of findings, not even an empty one, and make no ${REPORT_FINDINGS_TOOL_NAME} call.
