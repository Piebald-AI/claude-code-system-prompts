<!--
name: "Skill: Steward start git-only branch watch"
description: "Starts a git-only branch watch with its terms and command rules, optionally runs a review and schedules the first pass without changing files in the startup turn"
ccVersion: "2.1.331"
variables:
  - "WATCH_COMMAND_NAME"
  - "SHOULD_REVIEW"
  - "HEAD_BRANCH"
  - "TERMS_ALREADY_SHOWN"
  - "BUILD_REPLY_OPENING_INSTRUCTIONS_FN"
  - "FORMAT_QUOTED_LINES_FN"
  - "BUILD_WATCH_SUMMARY_LINES_FN"
  - "BRANCH_WATCH"
  - "FULL_TERMS_LINES"
  - "WATCH_COMMANDS"
  - "BUILD_GIT_ONLY_WATCH_RULES_FN"
  - "WATCH_BINDING"
  - "BUILD_GIT_ONLY_WAIT_AND_STOP_GUIDANCE_FN"
  - "IS_SANDBOX_ENABLED_FN"
  - "FORMAT_SANDBOX_DOMAIN_NOTE_FN"
  - "REMOTE_HOST_NAME"
  - "WATCH_START_OPTIONS"
  - "BASE_REF"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "WATCH_TIMING"
  - "FORMAT_WATCH_PROMPT_FN"
-->
# /${WATCH_COMMAND_NAME}: ${SHOULD_REVIEW?`review ${HEAD_BRANCH}, then watch it`:`watch ${HEAD_BRANCH}`}, with git alone

${TERMS_ALREADY_SHOWN?"Claude Code itself has already shown the user these lines. Don't repeat them:":BUILD_REPLY_OPENING_INSTRUCTIONS_FN("lines")}

${FORMAT_QUOTED_LINES_FN(BUILD_WATCH_SUMMARY_LINES_FN(TERMS_ALREADY_SHOWN?BRANCH_WATCH:{...e,folds:!1}))}

The full terms of this run${TERMS_ALREADY_SHOWN?", which the user can open in that row":""}. They hold as they stand. Print them only if the user asks:

${FORMAT_QUOTED_LINES_FN(FULL_TERMS_LINES)}

Add a line on any unpushed commits (they go up) and uncommitted changes (they don't): `${WATCH_COMMANDS.status}`.

${BUILD_GIT_ONLY_WATCH_RULES_FN(WATCH_BINDING,WATCH_BINDING.root,WATCH_COMMANDS,BRANCH_WATCH.isTurnSourceKnown,BRANCH_WATCH.stop,BUILD_GIT_ONLY_WAIT_AND_STOP_GUIDANCE_FN.host!==void 0)}

${IS_SANDBOX_ENABLED_FN()?`## First, try the remote

Run `${WATCH_COMMANDS.fetchBase}`${FORMAT_SANDBOX_DOMAIN_NOTE_FN(REMOTE_HOST_NAME)} now, while the user is here. If the sandbox blocks it (the message speaks of a network or host allowlist), this watch can't work: try no other way, stop as "Stopping" says, and tell the user that Claude Code's sandbox doesn't let git reach ${REMOTE_HOST_NAME}, in the message's own terms.

`:""}${SHOULD_REVIEW?`## 1. Review

${BRANCH_WATCH.callReview} TARGET is `${WATCH_START_OPTIONS}...HEAD`, after `${WATCH_COMMANDS.fetchBase}`${FORMAT_SANDBOX_DOMAIN_NOTE_FN(REMOTE_HOST_NAME)}, so that the review covers the local head and its unpushed commits.

If the tool says that the review runs in the background, say so in one line and end your turn, with no wake-up: the findings begin the next turn.

## 2. Hand over to the first pass

This turn changes nothing: no edit, no commit, no push. Once the findings are back in this turn, call`:`## Hand over to the first pass

This turn changes nothing: no edit, no commit, no push. Call`} ${BASE_REF} with `prompt` exactly `${SCHEDULE_WAKEUP_TOOL_NAME(BUILD_GIT_ONLY_WAIT_AND_STOP_GUIDANCE_FN)}`, a one-sentence `reason` and ${BRANCH_WATCH.hasWorkNow?``delaySeconds: ${WATCH_TIMING.secondsAfterANotification}`, tell the user that the first check-in starts in a minute, and end the turn. That pass ${SHOULD_REVIEW?"deals with the findings":"does the work"}.`:``delaySeconds: ${WATCH_TIMING.secondsWhileQuiet}`, tell the user that nothing needs doing now and that you look again when something changes, and end the turn.`}

${FORMAT_WATCH_PROMPT_FN(BUILD_GIT_ONLY_WAIT_AND_STOP_GUIDANCE_FN,WATCH_TIMING)}
