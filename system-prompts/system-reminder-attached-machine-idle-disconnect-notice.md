<!--
name: "System Reminder: Attached machine idle disconnect notice"
description: "Explains that idle attached machines stopped serving the session and how to reconnect"
ccVersion: "2.1.323"
variables:
  - "NO_MACHINE_ATTACHED_BY_OWN_WORD_PREFIX"
  - "FORMATTED_IDLE_MACHINE_LIST"
  - "IS_SINGLE_IDLE_MACHINE"
  - "IDLE_MACHINE_PRONOUN"
  - "CAPITALIZE_FN"
  - "GET_RUN_COMMANDS_HERE_INSTRUCTION_FN"
  - "IDLE_MACHINE_POSSESSIVE"
  - "HAS_COMPUTER_FOLDER_TOOLS"
  - "LIST_COMPUTER_FOLDERS_TOOL_NAME"
  - "REQUEST_COMPUTER_FOLDER_TOOL_NAME"
-->
${NO_MACHINE_ATTACHED_BY_OWN_WORD_PREFIX} ${FORMATTED_IDLE_MACHINE_LIST}. ${IS_SINGLE_IDLE_MACHINE?"It":"They"} stopped serving this session because the session had run nothing there for a while: an idle computer frees its place for other sessions, and nothing on ${IDLE_MACHINE_PRONOUN} needs restarting. ${CAPITALIZE_FN(GET_RUN_COMMANDS_HERE_INSTRUCTION_FN())}; if the task still needs ${IDLE_MACHINE_POSSESSIVE} files, tools or logins, do not do that part here: ${HAS_COMPUTER_FOLDER_TOOLS?`call ${LIST_COMPUTER_FOLDERS_TOOL_NAME} and ask for the folder again with ${REQUEST_COMPUTER_FOLDER_TOOL_NAME} (the user approves the request)`:`tell the user that ${IS_SINGLE_IDLE_MACHINE?"it was":"they were"} let go for idleness and that asking for the folder again is what brings ${IDLE_MACHINE_PRONOUN} back`}. Do not poll or schedule a wait for ${IDLE_MACHINE_PRONOUN}.
