<!--
name: "Skill: Steward watch ended"
description: "Explains why a pull request watch ended and asks for a final status without further changes"
ccVersion: "2.1.330"
variables:
  - "STEWARD_COMMAND_NAME"
  - "PULL_REQUEST_NUMBER"
  - "PULL_REQUEST_STATE"
  - "HAS_REACHED_WATCH_LIMIT"
  - "HAS_REPEATED_READ_FAILURES"
  - "FAILED_PASS_LIMIT"
  - "MAX_WATCH_DAYS"
  - "PERMISSION_MODE_WARNING"
  - "IS_WATCH_TURNED_OFF"
  - "WATCH_STOP_REASON"
  - "WATCH_BINDING_ERROR"
  - "WATCH_BINDING_RESULT"
  - "REMOTE_BINDING_CHANGE"
  - "USER_TAKEOVER_STEPS"
  - "FORMAT_TOOL_RESTRICTIONS_FN"
  - "MERGE_RECHECK_FAILURE"
  - "RECHECK_LIMIT"
  - "SAVED_WATCH"
  - "FORMAT_USER_REPORT_FN"
  - "IS_BRIEF_MODE_FN"
  - "SHOULD_SUGGEST_RESTART"
  - "REVIEW_HANDOFF_NOTE_FN"
-->
# /${STEWARD_COMMAND_NAME}: the watch of pull request #${PULL_REQUEST_NUMBER} has ended

${PULL_REQUEST_STATE.kind==="closed"?`It is ${PULL_REQUEST_STATE.state}.`:HAS_REACHED_WATCH_LIMIT?HAS_REPEATED_READ_FAILURES?`For ${FAILED_PASS_LIMIT} passes in a row Claude Code's own looks between them couldn't tell whether anything had changed, so each pass cost a turn. Most likely a read by gh or git fails: `gh pr checks ${PULL_REQUEST_NUMBER}` and `git rev-parse HEAD` show which.`:`It has reached its time limit (${MAX_WATCH_DAYS} days at most).`:PERMISSION_MODE_WARNING!==void 0?`Nothing would ask before a command now: ${PERMISSION_MODE_WARNING}.`:IS_WATCH_TURNED_OFF?`/${STEWARD_COMMAND_NAME} has been turned off.`:WATCH_STOP_REASON!==void 0?`It can't go on: ${WATCH_STOP_REASON}.`:WATCH_BINDING_ERROR!==void 0||typeof WATCH_BINDING_RESULT==="string"?`Claude Code can no longer hold it to this pull request: ${WATCH_BINDING_ERROR??WATCH_BINDING_RESULT}.`:REMOTE_BINDING_CHANGE!==void 0?`Claude Code can no longer hold it to this pull request: ${REMOTE_BINDING_CHANGE.say}.`:PULL_REQUEST_STATE.kind==="not_yours"?`It isn't the user's to drive from here any more: ${PULL_REQUEST_STATE.why}.`:USER_TAKEOVER_STEPS!==void 0?`${FORMAT_TOOL_RESTRICTIONS_FN(USER_TAKEOVER_STEPS.now)}. Tell the user how to take over. They ${USER_TAKEOVER_STEPS.takeOver}, then run /${STEWARD_COMMAND_NAME} ${PULL_REQUEST_NUMBER}.`:MERGE_RECHECK_FAILURE!==void 0?`${RECHECK_LIMIT} wake-ups in a row couldn't check what the last merge of the base changed. That merge may still be open in the checkout: tell the user that `git status` shows it.`:PULL_REQUEST_STATE.kind==="unknown"?`${RECHECK_LIMIT} looks in a row couldn't read it: ${PULL_REQUEST_STATE.say}.`:`This session's folder is no longer a checkout of ${SAVED_WATCH.where} with that pull request.`} The wake-up is cancelled already.

Change nothing: no edit, no commit, no push, no comment. Then ${FORMAT_USER_REPORT_FN({briefMode:IS_BRIEF_MODE_FN()})}: why the watch ended, where the pull request stood when you last looked, and what is still open.${HAS_REACHED_WATCH_LIMIT&&SHOULD_SUGGEST_RESTART?` End with: "Run /${STEWARD_COMMAND_NAME} again to keep watching."`:""}${REVIEW_HANDOFF_NOTE_FN()}
