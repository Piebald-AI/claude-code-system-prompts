<!--
name: "Data: Organization changed conversation restart refusal"
description: "Stops requests after the process leaves its organization and asks for a new conversation or process before continuing"
ccVersion: "2.1.329"
variables:
  - "PREVIOUS_ORGANIZATION_UUID"
  - "IS_VSCODE_HOST_FN"
-->
Claude Code did not send this request. This Claude Code process ran under your organization (${PREVIOUS_ORGANIZATION_UUID}). Now, the process does not run under that organization. Usually, this is because you signed out or signed in to another account, in this window or in another window. The process may still hold the conversation it had under that organization, including what you typed, file contents and command output. ${IS_VSCODE_HOST_FN()?"To continue, start a new conversation.":"To continue, start Claude Code again. In a terminal, exit Claude Code, then run claude."}
