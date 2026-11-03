<!--
name: "Skill: /send-to-project message preload description"
description: "Preloads the user-only command's project-message behavior, typed or drafted message selection and approval requirement"
ccVersion: "2.1.318"
variables:
  - "SEND_TO_PROJECT_TOOL_NAME"
-->
# Send a message to a Claude Project

Asks which project the message goes to (a new one, or one of the user’s own) and posts one message there as the user with the ${SEND_TO_PROJECT_TOOL_NAME} tool, whose confirmation pane shows the message for approval before anything is created or sent. The message is what the user types after the project. With none typed, Claude drafts at most three sentences from the conversation above; in a terminal session with no conversation yet, the command asks the user for the message in place instead. The project also gets this session’s Remote Control id, so it can read the session when it needs detail. Needs Remote Control on for the session, and offers to turn it on when it is off. With a project first in the arguments (its name in double quotes, its id or its link), the project is named up front.
