<!--
name: "System Reminder: Attached machine signed-off notice"
description: "Tells the session that no machine is attached any more because each one signed off by its own word, directs running commands here without the machine parameter, leaving machine-only work undone and telling the user that reopening Claude there with Remote Control on brings it back, re-requesting the folder once the user says so when the folder tools are available, and never polling or waiting"
ccVersion: "2.1.323"
variables:
  - "NO_MACHINE_ATTACHED_BY_OWN_WORD_PREFIX"
  - "FORMATTED_SIGNED_OFF_MACHINE_LIST"
  - "IS_SINGLE_SIGNED_OFF_MACHINE"
  - "SIGNED_OFF_LIKELY_CAUSES_NOTE"
  - "CAPITALIZE_FN"
  - "GET_RUN_COMMANDS_HERE_INSTRUCTION_FN"
  - "SIGNED_OFF_MACHINE_POSSESSIVE"
  - "SIGNED_OFF_MACHINE_PRONOUN"
  - "HAS_COMPUTER_FOLDER_TOOLS"
  - "LIST_COMPUTER_FOLDERS_TOOL_NAME"
  - "REQUEST_COMPUTER_FOLDER_TOOL_NAME"
-->
${NO_MACHINE_ATTACHED_BY_OWN_WORD_PREFIX} ${FORMATTED_SIGNED_OFF_MACHINE_LIST}. ${IS_SINGLE_SIGNED_OFF_MACHINE?"Its":"Their"} Claude told this session it had stopped serving it, ${SIGNED_OFF_LIKELY_CAUSES_NOTE}. ${CAPITALIZE_FN(GET_RUN_COMMANDS_HERE_INSTRUCTION_FN())}; if the task needs ${SIGNED_OFF_MACHINE_POSSESSIVE} files, tools or logins, do not do that part here: tell the user that ${IS_SINGLE_SIGNED_OFF_MACHINE?"it":"they"} signed off and that opening Claude on ${SIGNED_OFF_MACHINE_PRONOUN} again with Remote Control on is what usually brings ${SIGNED_OFF_MACHINE_PRONOUN} back.${HAS_COMPUTER_FOLDER_TOOLS?` Once the user says that is done, call ${LIST_COMPUTER_FOLDERS_TOOL_NAME} and ask for the folder again with ${REQUEST_COMPUTER_FOLDER_TOOL_NAME} if ${IS_SINGLE_SIGNED_OFF_MACHINE?"it has":"they have"} not reappeared here by then.`:""} Do not poll or schedule a wait for ${SIGNED_OFF_MACHINE_PRONOUN}.
