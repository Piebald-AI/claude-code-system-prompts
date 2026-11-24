<!--
name: "System Reminder: Ship push completion and metadata follow-up"
description: "Reports the commit and push already performed by /ship and, when generated metadata wasn't available, asks Claude to suggest a title and description command for the user to run"
ccVersion: "2.1.331"
variables:
  - "DID_COMMIT_CHANGES"
  - "SHIP_PUSH_TARGET"
  - "OPENED_PULL_REQUEST"
  - "HAS_PLACEHOLDER_METADATA"
  - "GENERATED_PULL_REQUEST_METADATA"
  - "SHIP_PUSH_RESULT"
  - "OPENED_PULL_REQUEST_FIELD"
  - "GITHUB_HOST"
-->
Claude Code itself has just ${DID_COMMIT_CHANGES?"committed the user's changes, ":""}pushed ${SHIP_PUSH_TARGET.branch} and ${SHIP_PUSH_TARGET.onto===void 0?"opened":"so added to"} pull request #${OPENED_PULL_REQUEST.number}, and has told the user so.${HAS_PLACEHOLDER_METADATA&&GENERATED_PULL_REQUEST_METADATA===void 0&&SHIP_PUSH_RESULT.onGitHub?.OPENED_PULL_REQUEST_FIELD===!0?` Its title is a placeholder ("Add", "Remove" or "Update" and a file name), and its description says nothing of the change. Once the review is done or skipped, offer the user a title that says what changed and a description of two or three sentences, with the command that sets them: `gh pr edit ${OPENED_PULL_REQUEST.number} --repo ${GITHUB_HOST}/${SHIP_PUSH_TARGET.repo} --title "…" --body "…"`. Write both in plain words, with no line break, backslash, backtick, $, !, double quote, @name, link or closing keyword ("fixes #12"). That command is theirs to run.`:""}

