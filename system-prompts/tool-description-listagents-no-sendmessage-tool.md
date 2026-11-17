<!--
name: "Tool Description: ListAgents (no SendMessage tool)"
description: "Describes the ListAgents tool for sessions without a SendMessage tool: it lists visible agents and Claude sessions plus this session's own name, and explains that replies must go through the host application's messaging tool or be relayed to the user"
ccVersion: "2.1.327"
variables:
  - "SEND_MESSAGE_TOOL_NAME"
-->
Lists the agents and Claude sessions this session can see — in-process subagents you spawned, the teammates on your team, other local Claude sessions on this machine, your Claude sessions running in the cloud (when this session has cloud access), and (when Remote Control is connected here) your account's other sessions, each row labeled by kind — plus this session's own name, the one other sessions use to message it. This session has no ${SEND_MESSAGE_TOOL_NAME} tool, so it cannot message them with it; other sessions can still message this one. To reply, use your host application's own messaging tool if it provides one — otherwise a reply from here is not possible, and if one is needed, tell your user. A long listing comes in pages: for the next one, pass the `cursor` its last line gives.
