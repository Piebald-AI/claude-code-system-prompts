<!--
name: "Data: Steward git-only watch permissions notice"
description: "Summarizes which host checks and comments the watch can see and warns that merging the base or taking remote commits can run programs as the user"
ccVersion: "2.1.331"
variables:
  - "BRANCH_WATCH"
  - "REMOTE_HOST_NAME"
  - "CAN_READ_HOST_CHECKS_FN"
  - "FORMAT_TRUSTED_REVIEWERS_FN"
  - "MUST_WATCH_COMMENTS_MANUALLY"
  - "HEAD_BRANCH"
  - "BASE_BRANCH"
  - "WATCH_START_OPTIONS"
-->
${BRANCH_WATCH.host===void 0?`Claude can't see checks or comments on ${REMOTE_HOST_NAME}, so watch those yourself.`:`Claude Code reads ${REMOTE_HOST_NAME}'s web API, with git's saved sign-in: ${[...CAN_READ_HOST_CHECKS_FN(BRANCH_WATCH.host)?["checks"]:[],...BRANCH_WATCH.host.written.last===void 0?[]:[`comments by you and ${FORMAT_TRUSTED_REVIEWERS_FN(BRANCH_WATCH.host)}`]].join(", and ")||"whether the request is merged or closed"}.${CAN_READ_HOST_CHECKS_FN(BRANCH_WATCH.host)&&!MUST_WATCH_COMMENTS_MANUALLY?"":` Watch its ${[...CAN_READ_HOST_CHECKS_FN(BRANCH_WATCH.host)?[]:["checks"],...MUST_WATCH_COMMENTS_MANUALLY?["comments"]:[]].join(" and ")} yourself.`}`} As you, Claude may push to ${HEAD_BRANCH} and merge ${BASE_BRANCH} into it${WATCH_START_OPTIONS.isAuto?", unattended":""}. While Claude watches, anyone who lands a change on ${BASE_BRANCH} or pushes to ${HEAD_BRANCH} can run programs here as you.
