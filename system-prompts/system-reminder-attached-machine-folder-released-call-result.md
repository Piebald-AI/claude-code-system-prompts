<!--
name: "System Reminder: Attached machine folder released (call result)"
description: "Tells Claude that the person at an attached machine disconnected the session from the folder it was using, that nothing is down, to do the rest without that machine and say what is left undone, and to ask for the folder again only if the user wants"
ccVersion: "2.1.323"
variables:
  - "RELEASED_MACHINE_NAME"
  - "DO_NOT_CALL_UNTIL_ATTACHED_INSTRUCTION_FN"
-->
The person at ${RELEASED_MACHINE_NAME} disconnected this session from the folder it was using there. Nothing on ${RELEASED_MACHINE_NAME} is down. Do the rest of the task without ${RELEASED_MACHINE_NAME} and tell the user what that leaves undone; ask for the folder again only if the user wants you to. ${DO_NOT_CALL_UNTIL_ATTACHED_INSTRUCTION_FN(RELEASED_MACHINE_NAME)}
