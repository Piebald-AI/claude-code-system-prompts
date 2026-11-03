<!--
name: "Skill: /send-to-project message slash command"
description: "Directs one project-message tool call with command-selected inputs, user confirmation and controlled retry only after a requested revision"
ccVersion: "2.1.318"
variables:
  - "SEND_TO_PROJECT_TOOL_NAME"
  - "TOOL_SEARCH_TOOL_NAME"
  - "MESSAGE_TOOL_INPUT_GUIDANCE"
  - "USER_TYPED_MESSAGE_REVISION_CONTEXT_BLOCK"
-->
# Send a message to a Claude Project

The user ran /send-to-project in this session and chose the project. The command posts one message in that project as the user. The project is also told which session this is, so it can read this conversation when it needs detail.

If `${SEND_TO_PROJECT_TOOL_NAME}` is not in your tool list yet, load it first with `${TOOL_SEARCH_TOOL_NAME} select:${SEND_TO_PROJECT_TOOL_NAME}`. Then call it once, with these inputs and nothing before the call:

${MESSAGE_TOOL_INPUT_GUIDANCE}

The tool’s confirmation pane shows the user the message and asks them, so do not paste the message into your reply and do not ask for a go-ahead first. If the user declines the pane, nothing was created or sent. A decline can carry what they want changed, which arrives with the rejection: write the message with that change in `proposal.summary` and call the tool again with the other inputs as they were. A bare decline means stop. Once a call has gone through, never call it again in this run.

After a call goes through, reply with the lines the tool’s result gives, as it says: one fact per line, names as the markdown links it wrote, never an id or a bare URL.
${USER_TYPED_MESSAGE_REVISION_CONTEXT_BLOCK}
