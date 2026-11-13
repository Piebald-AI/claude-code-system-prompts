<!--
name: "Data: Sandbox linked worktree write denial warning"
description: "Warns that a worktrees directory could not be inspected without following a possible remote link and lists the paths denied writes to protect linked worktrees"
ccVersion: "2.1.324"
variables:
  - "WORKTREES_DIRECTORY_PATH"
  - "WRITE_DENIED_PATHS"
  - "GET_PLATFORM_FN"
-->
[Sandbox] ${WORKTREES_DIRECTORY_PATH} is, or is inside, a link that leads or may lead to another computer, or could not be checked without following one, so Claude Code did not look inside it. Instead it write-denied ${WRITE_DENIED_PATHS.join(" and ")}, so git commands in the sandbox cannot update any linked worktree of this repository (add, commit, checkout), including this session's own.${GET_PLATFORM_FN()==="macos"?" On macOS this holds only if one of those paths is the real folder: a deny on a link does not stop writes through it.":""} If you did not make that link, remove it and restart Claude Code.
