<!--
name: "System Reminder: Resumed command approval directory verification failure"
description: "Refuses a command approved before a restart when its original directory cannot be verified and directs a fresh call from the intended directory"
ccVersion: "2.1.329"
variables:
  - "APPROVAL_DIRECTORY_CHECK_FAILURE_REASON"
  - "APPROVAL_DIRECTORY_BASE_PATH"
  - "SHELL_DIRECTORY_STATEMENT"
-->
This call was not run. Claude Code could not confirm that the shell is back in the directory where it was approved. ${APPROVAL_DIRECTORY_CHECK_FAILURE_REASON==="no_record"?"It kept no record of that directory.":APPROVAL_DIRECTORY_CHECK_FAILURE_REASON==="shell_unheard"?"The machine that runs the tools did not say where its shell stands.":APPROVAL_DIRECTORY_BASE_PATH===void 0?"It does not keep track of that directory across a restart in a session that has been in a worktree.":"That directory may be gone or replaced, lie outside the directory where the session started, or be one that Claude Code needs approval to enter or is not allowed to examine."} ${SHELL_DIRECTORY_STATEMENT} If the command still makes sense, cd to the directory it was meant for and make the call again; it may need approval again.
