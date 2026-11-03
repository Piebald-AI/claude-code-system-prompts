<!--
name: "Skill: /send-to-project work brief preload description"
description: "Preloads the user-only command's project work-brief transfer behavior, approval requirement and Remote Control dependency"
ccVersion: "2.1.318"
variables:
  - "SEND_TO_PROJECT_TOOL_NAME"
-->
# Send this session’s work to a Claude Project

Asks which project the work goes to (a new one, or one of the user’s own), has Claude draft a short brief of the work from the conversation above (what it is, where it stands, what is left) and sends that with the ${SEND_TO_PROJECT_TOOL_NAME} tool, whose confirmation pane shows the brief for approval before anything is created or sent. The project gets the brief as its setup card and this session’s Remote Control id, so its coordinator can read the session when it needs detail. Needs Remote Control on for the session, and offers to turn it on when it is off. With a project first in the arguments (its name in double quotes, its id or its link), the project is named up front. Nothing on this computer is read until the user runs the command.
