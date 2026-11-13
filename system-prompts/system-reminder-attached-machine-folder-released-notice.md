<!--
name: "System Reminder: Attached machine folder released notice"
description: "Tells the session that no machine is attached any more because the person at each computer disconnected the session from its folder, directs running commands here, saying what that leaves undone, asking for the folder again only if the user wants, and never polling or waiting"
ccVersion: "2.1.323"
variables:
  - "NO_MACHINE_ATTACHED_BY_OWN_WORD_PREFIX"
  - "FORMATTED_RELEASED_MACHINE_LIST"
  - "IS_SINGLE_RELEASED_MACHINE"
  - "RELEASED_MACHINE_PRONOUN"
  - "CAPITALIZE_FN"
  - "GET_RUN_COMMANDS_HERE_INSTRUCTION_FN"
  - "RELEASED_MACHINE_POSSESSIVE"
-->
${NO_MACHINE_ATTACHED_BY_OWN_WORD_PREFIX} ${FORMATTED_RELEASED_MACHINE_LIST}. The person at ${IS_SINGLE_RELEASED_MACHINE?"that computer":"those computers"} disconnected this session from the folder it was using there; nothing on ${RELEASED_MACHINE_PRONOUN} is down. ${CAPITALIZE_FN(GET_RUN_COMMANDS_HERE_INSTRUCTION_FN())}; if the task needs ${RELEASED_MACHINE_POSSESSIVE} files, tools or logins, tell the user what that leaves undone, and ask for the folder again only if the user wants you to. Do not poll or schedule a wait for ${RELEASED_MACHINE_PRONOUN}.
