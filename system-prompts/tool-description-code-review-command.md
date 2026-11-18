<!--
name: "Tool Description: Code review command"
description: "Describes the code review command, its effort levels, PR comment mode, fix mode, and --max-findings limit, with optional ultra cloud review and post-flag notes"
ccVersion: "2.1.328"
variables:
  - "SIMPLIFY_COMMAND_NAME"
  - "EFFORT_LEVELS"
  - "ULTRA_CLOUD_REVIEW_CLAUSE"
  - "ULTRA_POST_FLAG_NOTE"
-->
Review the current diff, or a PR number/branch/path target, for correctness bugs (plus broken CLAUDE.md rules and cleanups where the model's recipe covers them; see /${SIMPLIFY_COMMAND_NAME}) at the effort level given first, before any target (${EFFORT_LEVELS.join("|")}: from few high-confidence findings to many, some uncertain${ULTRA_CLOUD_REVIEW_CLAUSE}); with no level given, it reuses the level you typed last. Pass --comment to post findings as inline PR comments, or --fix to apply them to the working tree after the review. Pass --max-findings <n> to report up to n findings, or --max-findings all for every finding. The choice stays until you pass --max-findings default.${ULTRA_POST_FLAG_NOTE}
