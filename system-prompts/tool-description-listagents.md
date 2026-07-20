<!--
name: "Tool Description: ListAgents"
description: "Describes the ListAgents tool, which lists agents you can message — in-process subagents, other local and cloud Claude sessions, and remote bridge sessions"
ccVersion: "2.1.200"
variables:
  - "SEND_MESSAGE_TOOL_NAME"
-->
Lists agents you can ${SEND_MESSAGE_TOOL_NAME} to — in-process subagents you spawned, other local Claude sessions on this machine, your Claude sessions running in the cloud (when this session has cloud access), and (when Remote Control is connected) remote bridge sessions, which you can only reply to. Names are the address: send with `${SEND_MESSAGE_TOOL_NAME}({to: "<name>", message: "..."})`, copying the name exactly as a row prints it. Append a row's ` [ref]` only when the bare name is not enough — two rows share it, or an error asks you to disambiguate.
