<!--
name: "Skill: Steward git-only watch ended"
description: "Reports why a git-only branch watch ended, forbids further changes and suggests restarting only when the branch can still be watched"
ccVersion: "2.1.331"
variables:
  - "STEWARD_COMMAND_NAME"
  - "HEAD_BRANCH"
  - "BRANCH_READ_RESULT"
  - "FORMAT_HOST_REQUEST_KIND_FN"
  - "WATCH_BINDING"
  - "HEAD_REMOTE"
  - "BASE_BRANCH"
  - "WATCH_END_DETAILS"
  - "PLAN_MODE_STOP_NOTICE"
  - "REPOSITORY_NAME"
  - "FORMAT_USER_REPORT_FN"
  - "IS_BRIEF_MODE_FN"
  - "HAS_REACHED_WATCH_LIMIT"
  - "HAS_LOCAL_STOP_CONDITION"
  - "GET_HOST_READ_FAILURE_FN"
  - "FORMAT_BASE_REF_FN"
  - "REVIEW_HANDOFF_NOTE_FN"
-->
# /${STEWARD_COMMAND_NAME}: the watch of ${HEAD_BRANCH} has ended

${BRANCH_READ_RESULT.kind==="closed"?BRANCH_READ_RESULT.isHostsWord?`Its ${FORMAT_HOST_REQUEST_KIND_FN(WATCH_BINDING.host)} was ${BRANCH_READ_RESULT.state==="merged"?"merged":"closed without a merge"}.`:BRANCH_READ_RESULT.state==="closed"?`${HEAD_BRANCH} is gone from ${HEAD_REMOTE}.`:`${HEAD_BRANCH} adds nothing to ${BASE_BRANCH} any more: it was merged, or its changes got there another way.`:WATCH_END_DETAILS.passesWithNoLook!==void 0?`For ${WATCH_END_DETAILS.passesWithNoLook} passes in a row Claude Code's own looks between them couldn't tell whether anything had changed, so each pass cost a turn. Most likely git can't reach the remote: tell the user that `git ls-remote ${HEAD_REMOTE}` shows why.`:WATCH_END_DETAILS.timeIsUp?`It has reached its time limit (${WATCH_END_DETAILS.days} days at most).`:WATCH_END_DETAILS.bypass!==void 0?`Nothing would ask before a command now: ${WATCH_END_DETAILS.bypass}.`:WATCH_END_DETAILS.isOff||WATCH_END_DETAILS.isPlanning?WATCH_END_DETAILS.isOff?`/${STEWARD_COMMAND_NAME} has been turned off.`:PLAN_MODE_STOP_NOTICE:WATCH_END_DETAILS.denied!==void 0?`It can't go on: ${WATCH_END_DETAILS.denied}.`:WATCH_END_DETAILS.notReached!==void 0?`${WATCH_END_DETAILS.notReached}.`:WATCH_END_DETAILS.notHeld!==void 0?`Claude Code can no longer hold it to this branch: ${WATCH_END_DETAILS.notHeld}.`:BRANCH_READ_RESULT.kind==="not_yours"?`It can't be looked after from here any more: ${BRANCH_READ_RESULT.why}.`:WATCH_END_DETAILS.isNotYet?`${WATCH_END_DETAILS.unreadLooks} wake-ups in a row couldn't check what the last merge of the base changed. That merge may still be open in the checkout: tell the user that `git status` shows it.`:BRANCH_READ_RESULT.kind==="unknown"?`${WATCH_END_DETAILS.unreadLooks} wake-ups in a row couldn't read it: ${BRANCH_READ_RESULT.say}.`:`This session's folder is no longer a checkout of ${REPOSITORY_NAME}.`} The wake-up is cancelled already.

Change nothing: no edit, no commit, no push. Then ${FORMAT_USER_REPORT_FN({briefMode:IS_BRIEF_MODE_FN()})}: why the watch ended, where the branch stood when you last looked, and what is still open.${HAS_REACHED_WATCH_LIMIT&&BRANCH_READ_RESULT.kind==="yours"||!HAS_LOCAL_STOP_CONDITION&&BRANCH_READ_RESULT.kind==="unknown"&&(WATCH_BINDING.host&&GET_HOST_READ_FAILURE_FN(WATCH_BINDING.host))!=="new_each_time"?` End with: "Run /${STEWARD_COMMAND_NAME} ${FORMAT_BASE_REF_FN(WATCH_BINDING)} to keep watching."`:BRANCH_READ_RESULT.kind==="closed"?" There is nothing left to watch, so don't offer to start again.":""}${REVIEW_HANDOFF_NOTE_FN()}
