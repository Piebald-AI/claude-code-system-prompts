<!--
name: "System Reminder: Ship branch behind a cloud watcher"
description: "Explains why Ship skipped review when the branch is behind an active cloud watcher and what the user can do next"
ccVersion: "2.1.330"
variables:
  - "PULL_REQUEST_STATUS"
  - "CLOUD_SESSION_LABEL"
  - "STEWARD_LABELS"
  - "SESSION_HOME_URL_FN"
-->
${PULL_REQUEST_STATUS.isWatched?`The ${CLOUD_SESSION_LABEL} and ${STEWARD_LABELS.watching} labels on #${PULL_REQUEST_STATUS.number} say a cloud session or PR Steward`:`The ${CLOUD_SESSION_LABEL} label on #${PULL_REQUEST_STATUS.number} says a cloud session`} is already watching it. It also pushes to the branch. Your local branch doesn't match GitHub. To add work from here, ${PULL_REQUEST_STATUS.isWatched?`wait until the ${STEWARD_LABELS.working} label is gone, `:""}pull, then commit and push. /ship started no review. For one, run /ship again once your branch matches GitHub and nothing is left to commit.
${PULL_REQUEST_STATUS.isWatched?`To stop it, archive the session at ${SESSION_HOME_URL_FN()}/code if it hasn't ended, and remove both labels, which also stops PR Steward.`:`To stop that session, archive it at ${SESSION_HOME_URL_FN()}/code and remove the label.`}
