<!--
name: "System Reminder: Auto mode dynamically constructed command refusal"
description: "Explains that a command assembled at runtime was not covered by auto mode's whole-script check and requests a new script containing the complete command"
ccVersion: "2.1.318"
variables:
  - "TOOL_NAME"
-->
This ${TOOL_NAME} command was NOT run. Auto mode checks each piece of code as a whole before it starts, and that check covers only a command that the code spells out in full. Your code put this one together as it ran (a ${} value, a variable, .cwd() or .env()), or it uses the name $ or ${TOOL_NAME} for something other than a call. This is not a judgment that the command is unsafe. Send it again in a new piece of code with the whole command written out, its values included, as in $`git commit -m "fix typo"`; for another directory, start the command with cd.
