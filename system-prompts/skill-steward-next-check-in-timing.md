<!--
name: "Skill: Steward next check-in timing"
description: "Schedules the next watch pass sooner after a push or during active checks and allows quiet passes to be hidden"
ccVersion: "2.1.330"
variables:
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "FORMAT_WATCH_PROMPT_FN"
  - "WATCHED_PULL_REQUEST"
  - "AFTER_PUSH_DELAY_SECONDS"
  - "CHECKS_RUNNING_DELAY_SECONDS"
  - "IDLE_DELAY_SECONDS"
-->
call ${SCHEDULE_WAKEUP_TOOL_NAME} with `prompt` exactly `${FORMAT_WATCH_PROMPT_FN(WATCHED_PULL_REQUEST.pr)}`, a one-sentence `reason`, `noop: true` only if this pass changed nothing and you have nothing new to tell the user (a pass with `noop: true` is folded away on the screen at the next wake-up, so a first Ready or Still needed report, or a question, is never one), and `delaySeconds`:
   - ${AFTER_PUSH_DELAY_SECONDS} if you pushed in this pass, or left a red check's log to a later pass and no check is pending, or `mergeable` is `UNKNOWN`, or gh says "no checks reported" within five minutes of a push: checks take a moment to show up. Any later, this repository runs no checks on that head, which counts as green and as nothing running.
   - ${CHECKS_RUNNING_DELAY_SECONDS} while checks run (bucket `pending`). A check that has been pending for over an hour counts as not running.
   - ${IDLE_DELAY_SECONDS} when nothing is running.
