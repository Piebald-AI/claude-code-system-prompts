<!--
name: "Skill: Steward waiting and stopping"
description: "Explains automatic wake-ups, when the watch ends, and how to stop and report the pull request's status"
ccVersion: "2.1.330"
variables:
  - "REPORT_BEFORE_WAKE"
  - "REPORT_INSTRUCTION"
  - "WAKE_INSTRUCTION"
  - "CHECKS_RUNNING_DELAY_SECONDS"
  - "QUIET_PASS_LIMIT"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "FIRST_PASS_DELAY_SECONDS"
  - "MAX_WATCH_DAYS"
  - "FORMAT_USER_REPORT_FN"
  - "IS_BRIEF_MODE_FN"
  - "STEWARD_COMMAND_NAME"
  - "REVIEW_HANDOFF_NOTE_FN"
-->
## Waiting

A turn that ends without a wake-up ends the watch, but for the one that waits for a background review. So at the end of each pass, unless you are stopping (the start's hand-over has its own delay):
${REPORT_BEFORE_WAKE?`1. First ${REPORT_INSTRUCTION}
2. Then, as the last action of the turn, ${WAKE_INSTRUCTION}`:`1. First ${WAKE_INSTRUCTION}
2. Then ${REPORT_INSTRUCTION}`}

Between your passes Claude Code looks at the pull request by itself, every two minutes. Once something changes (the first check of a round goes red, the round ends, somebody whom you read writes, a head moves, it is merged or closed), it wakes you within a few minutes, whatever delay you gave, though no sooner than ten minutes after it last woke you. A wake-up of ${CHECKS_RUNNING_DELAY_SECONDS} seconds or less comes at its time all the same, until ${QUIET_PASS_LIMIT} passes in a row have found nothing new. The one for when nothing is running it puts off for as long as all is as this pass found it, so that a quiet watch costs the user no turn. Start no wait or poll of your own.

**A turn that a task notification begins** (the review's findings) changes nothing: no edit, no commit, no push, no comment. Unless you have stopped, or the user has pressed Esc or started a /loop since, call ${SCHEDULE_WAKEUP_TOOL_NAME} with the same `prompt` and `delaySeconds: ${FIRST_PASS_DELAY_SECONDS}`, and end the turn. The pass that it starts does the work, under these rules.

## Stopping

Claude Code ends the watch by itself once the pull request is merged or closed, is no longer the user's to drive from this checkout, is aimed at another base branch, carries a hosted agent's label, the session goes into bypass mode or loses the fence, or ${MAX_WATCH_DAYS} days are over. Stop it yourself when:
- The user says stop. Or a trusted person asks on the pull request that you stop, hold off or leave the branch alone, or says that they are handling it: push nothing more, and tell the user who asked.

To stop: call ${SCHEDULE_WAKEUP_TOOL_NAME} with `stop: true` and nothing else, then ${FORMAT_USER_REPORT_FN({briefMode:IS_BRIEF_MODE_FN()})}: where the pull request stands, what is still open, why you stopped, and "Run /${STEWARD_COMMAND_NAME} again to keep watching."${REVIEW_HANDOFF_NOTE_FN()}
