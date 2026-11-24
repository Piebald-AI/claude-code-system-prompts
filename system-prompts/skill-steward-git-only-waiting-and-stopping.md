<!--
name: "Skill: Steward git-only waiting and stopping"
description: "Schedules git-only watch passes around remote changes, defers background review findings to a new pass and defines when to stop and report the branch's state"
ccVersion: "2.1.331"
variables:
  - "REPORT_BEFORE_WAKE"
  - "REPORT_INSTRUCTION"
  - "WAKE_INSTRUCTION"
  - "HEAD_BRANCH"
  - "BASE_BRANCH"
  - "GET_HOST_WATCH_CAPABILITIES_FN"
  - "BRANCH_WATCH"
  - "FORMAT_HOST_REQUEST_KIND_FN"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "FIRST_PASS_DELAY_SECONDS"
  - "HEAD_REMOTE"
  - "MAX_WATCH_DAYS"
  - "FORMAT_USER_REPORT_FN"
  - "IS_BRIEF_MODE_FN"
  - "STEWARD_COMMAND_NAME"
  - "FORMAT_BASE_REF_FN"
  - "REVIEW_HANDOFF_NOTE_FN"
-->
## Waiting

A turn that ends without a wake-up ends the watch, but for the one that waits for a background review. So at the end of each pass, unless you are stopping (the start's hand-over has its own delay):
${REPORT_BEFORE_WAKE?`1. First ${REPORT_INSTRUCTION}
2. Then, as the last action of the turn, ${WAKE_INSTRUCTION}`:`1. First ${WAKE_INSTRUCTION}
2. Then ${REPORT_INSTRUCTION}`}

Between your passes Claude Code asks the remote by itself, every two minutes. Once `${HEAD_BRANCH}` and `${BASE_BRANCH}` conflict, somebody else pushes to `${HEAD_BRANCH}`, ${GET_HOST_WATCH_CAPABILITIES_FN(BRANCH_WATCH.host).checks?"a check turns red or green, ":""}${GET_HOST_WATCH_CAPABILITIES_FN(BRANCH_WATCH.host).words?"somebody whose words count writes, ":""}${GET_HOST_WATCH_CAPABILITIES_FN(BRANCH_WATCH.host).end?`the ${FORMAT_HOST_REQUEST_KIND_FN(BRANCH_WATCH.host)} is merged or closed, `:""}or `${HEAD_BRANCH}` is gone or adds nothing any more, it wakes you within a few minutes, whatever delay you gave, though no sooner than ten minutes after it last woke you. Otherwise it puts your wake-up off, so that a quiet watch costs the user no turn. A base that merely moves is no news. Start no wait or poll of your own.

**A turn that a task notification begins** (the review's findings) changes nothing: no edit, no commit, no push. Unless you have stopped, or the user has pressed Esc or started a /loop since, call ${SCHEDULE_WAKEUP_TOOL_NAME} with the same `prompt` and `delaySeconds: ${FIRST_PASS_DELAY_SECONDS}`, and end the turn. The pass that it starts does the work, under these rules.

## Stopping

Claude Code ends the watch by itself once `${HEAD_BRANCH}` is gone from `${HEAD_REMOTE}` or adds nothing to `${BASE_BRANCH}` any more, ${GET_HOST_WATCH_CAPABILITIES_FN(BRANCH_WATCH.host).end?`its ${FORMAT_HOST_REQUEST_KIND_FN(BRANCH_WATCH.host)} is merged, closed or aimed at another branch, `:""}another branch is checked out, the session goes into bypass mode or plan mode or loses the fence, or ${MAX_WATCH_DAYS} days are over. Stop it yourself when the user says stop.${!GET_HOST_WATCH_CAPABILITIES_FN(BRANCH_WATCH.host).words?"":` Or when somebody whose words Claude Code kept asks on the ${FORMAT_HOST_REQUEST_KIND_FN(BRANCH_WATCH.host)} that you stop, hold off or leave the branch alone, or says that they are handling it: push nothing more, and tell the user who asked.`}

To stop: call ${SCHEDULE_WAKEUP_TOOL_NAME} with `stop: true` and nothing else, then ${FORMAT_USER_REPORT_FN({briefMode:IS_BRIEF_MODE_FN()})}: where the branch stands, what is still open, why you stopped, and "Run /${STEWARD_COMMAND_NAME} ${FORMAT_BASE_REF_FN(BRANCH_WATCH)} to keep watching."${REVIEW_HANDOFF_NOTE_FN()}
