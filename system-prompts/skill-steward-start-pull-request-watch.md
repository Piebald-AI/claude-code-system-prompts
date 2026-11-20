<!--
name: "Skill: Steward start pull request watch"
description: "Sets up a watch with or without an initial review, avoids duplicate reviews, and hands off to the first pass"
ccVersion: "2.1.330"
variables:
  - "STEWARD_COMMAND_NAME"
  - "SHOULD_REVIEW"
  - "WATCHED_PULL_REQUEST"
  - "COMMAND_LEADING_NOTE"
  - "TERMS_ALREADY_SHOWN"
  - "TERMS_SHOWN_NOTE"
  - "FORMAT_QUOTED_LINES_FN"
  - "STARTUP_SUMMARY_LINES"
  - "WATCH_TERMS"
  - "AUTO_MERGE_WARNING_GUIDANCE"
  - "USE_FOLDED_TERMS"
  - "USER_WATCH_COMMAND"
  - "FULL_TERMS_LINES"
  - "BUILD_WATCH_RULES_FN"
  - "WATCH_COMMANDS"
  - "STOP_COMMAND"
  - "BUILD_REVIEW_AGENT_GUIDANCE_FN"
  - "REVIEW_AGENT_SETTINGS"
  - "REMOTE_PULL_REQUEST_HEAD"
  - "REVIEW_TOOL_GUIDANCE"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "FORMAT_WATCH_PROMPT_FN"
  - "FIRST_PASS_DELAY_SECONDS"
  - "BUILD_WAIT_AND_STOP_GUIDANCE_FN"
  - "REPORT_BEFORE_WAKE"
-->
# /${STEWARD_COMMAND_NAME}: ${SHOULD_REVIEW?`review pull request #${WATCHED_PULL_REQUEST.pr}, then watch it`:`watch pull request #${WATCHED_PULL_REQUEST.pr}`}

${COMMAND_LEADING_NOTE}${TERMS_ALREADY_SHOWN?TERMS_SHOWN_NOTE:"Before any tool call, begin your reply with these lines, word for word:"}

${FORMAT_QUOTED_LINES_FN(STARTUP_SUMMARY_LINES)}${WATCH_TERMS.autoMerge===void 0?"":`

${AUTO_MERGE_WARNING_GUIDANCE}`}

The full terms of this run, which the user can open ${USE_FOLDED_TERMS&&TERMS_ALREADY_SHOWN?"in that row":`with ${USER_WATCH_COMMAND} terms`}. They hold as they stand. Print them only if the user asks:

${FORMAT_QUOTED_LINES_FN(FULL_TERMS_LINES)}

${BUILD_WATCH_RULES_FN(WATCHED_PULL_REQUEST,WATCH_COMMANDS,STOP_COMMAND)}

## First, what is here

Add a line on any unpushed commits (they go up) and uncommitted changes (they don't): `${WATCH_COMMANDS.status}`.

${SHOULD_REVIEW?`## 1. Don't do it twice

${BUILD_REVIEW_AGENT_GUIDANCE_FN(REVIEW_AGENT_SETTINGS)} In this order:
- **A hosted review of this head**, if the local `HEAD` is ${REMOTE_PULL_REQUEST_HEAD.headSha}: `${WATCH_COMMANDS.hostedReview.replace("HEAD_SHA",REMOTE_PULL_REQUEST_HEAD.headSha)}`. It is running if that prints `queued` or `in_progress` and it started under an hour ago (`date -u`). It is done if that prints `completed` and Claude's hosted review has reported on that commit. Either way say so and skip step 2: its findings reach you as a bot's comments.
- **Your own earlier review**, if you have posted one: SHA is the head that it names. If SHA is the local `HEAD`, say so and skip step 2. If it is an ancestor of `HEAD` (`${WATCH_COMMANDS.isAncestor}`), look at `${WATCH_COMMANDS.logSince}`. Nothing but merges of the base: skip step 2. No merge of the base: review only what came since, with `SHA..HEAD` as TARGET. Both: keep the whole TARGET.

## 2. Review

${REVIEW_TOOL_GUIDANCE} Unless step 1 set it, TARGET is `${WATCHED_PULL_REQUEST.baseRemote}/${WATCHED_PULL_REQUEST.baseBranch}...HEAD`, after `${WATCH_COMMANDS.fetchBase}`, so that the review covers the local head and its unpushed commits.

If the tool says that the review runs in the background, say so in one line and end your turn, with no wake-up: the findings begin the next turn.

## 3. Hand over to the first pass

This turn changes nothing: no edit, no commit, no push, no comment. Once the findings are back in this turn, or step 1 skipped the review, call`:`## Hand over to the first pass

This turn changes nothing: no edit, no commit, no push, no comment. Call`} ${SCHEDULE_WAKEUP_TOOL_NAME} with `prompt` exactly `${FORMAT_WATCH_PROMPT_FN(WATCHED_PULL_REQUEST.pr)}`, a one-sentence `reason` and `delaySeconds: ${FIRST_PASS_DELAY_SECONDS}`, tell the user that the first check-in starts in a minute, and end the turn. That pass ${SHOULD_REVIEW?"deals with the findings":"does the work"}. It comes with what has been written on the pull request by then, which code reads afresh for each pass${SHOULD_REVIEW?": a review can take a while, and somebody may have asked you to stop meanwhile":""}.

${BUILD_WAIT_AND_STOP_GUIDANCE_FN(WATCHED_PULL_REQUEST,REPORT_BEFORE_WAKE)}
