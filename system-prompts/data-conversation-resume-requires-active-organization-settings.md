<!--
name: "Data: Conversation resume requires active organization settings"
description: "Explains how to restart under the organization required to resume a saved conversation when its settings aren't active"
ccVersion: "2.1.329"
variables:
  - "CONVERSATION_ORGANIZATION_NOTE"
  - "ORGANIZATION_RESUME_REQUIREMENT_NOTE"
  - "GET_ORGANIZATION_SIGN_IN_COMMAND_FN"
-->
${CONVERSATION_ORGANIZATION_NOTE} You are signed in to that organization, but this session does not use that organization's settings. This can happen if the session started before you signed in, with --bare, through a gateway, or from Claude Desktop. ${ORGANIZATION_RESUME_REQUIREMENT_NOTE} To resume it, start claude again in a terminal. Usually, this is enough. Do not use --bare. If this session runs through a gateway, first type /logout in Claude Code to sign out of the gateway. This also signs you out of that organization. Then unset CLAUDE_CODE_USE_GATEWAY. In a terminal, run ${GET_ORGANIZATION_SIGN_IN_COMMAND_FN()}. Then start claude again.
