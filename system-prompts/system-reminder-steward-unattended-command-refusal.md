<!--
name: "System Reminder: Steward unattended command refusal"
description: "Explains why a command was refused during an unattended pass and directs larger requests back to the user"
ccVersion: "2.1.330"
variables:
  - "REFUSAL_REASON"
  - "WATCHED_PULL_REQUEST"
  - "FORMAT_USER_HANDOFF_FN"
  - "IS_TERMINAL_SESSION_FN"
-->
Claude Code did not run this: ${REFUSAL_REASON}. While /steward runs unattended on pull request #${WATCHED_PULL_REQUEST.pr}, only its listed gh and git commands, written out in full, and its own tools can run. A read does run when it is written plainly: one git command to a line, from the checkout's top folder, with nothing for the shell to fill in, as in git diff main...HEAD, git log, git show, git status, git ls-files. For anything else look for no other way: tell the user what you wanted to do and why, and go on with the rest. If the user asked for this themselves, ask them to type ${FORMAT_USER_HANDOFF_FN(WATCHED_PULL_REQUEST)}${IS_TERMINAL_SESSION_FN()?", or to type the request again after this turn ends":""}.
