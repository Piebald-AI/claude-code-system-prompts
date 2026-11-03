<!--
name: "System Reminder: Resumed command approval directory verification failure"
description: "Refuses a command approved before a restart when its original directory cannot be verified and directs a fresh call from the intended directory"
ccVersion: "2.1.318"
variables:
  - "SESSION_START_DIRECTORY"
  - "GET_CWD_FN"
-->
This call was not run. The command was approved before Claude Code restarted, and Claude Code could not confirm that the shell is back in the directory where it was approved. ${SESSION_START_DIRECTORY===void 0?"It does not keep track of that directory across a restart in a session that has been in a worktree.":"That directory may be gone or replaced, lie outside the directory where the session started, or be one that Claude Code needs approval to enter or is not allowed to examine."} The shell's directory is ${GET_CWD_FN()}. If the command still makes sense, cd to the directory it was meant for and make the call again; it may need approval again.
