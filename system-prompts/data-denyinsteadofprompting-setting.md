<!--
name: "Data: denyInsteadOfPrompting setting"
description: "Documents the permissions.denyInsteadOfPrompting setting that immediately denies otherwise interactive tool requests while preserving permission rules and hooks"
ccVersion: "2.1.319"
-->
Never wait for a person to answer a tool permission prompt: a call that would prompt is denied at once, the model is told, and the turn carries on. This is what --permission-prompts none does for -p, in every kind of session, subagents and agent teams included. Allow rules, the permission mode, auto mode's classifier and PermissionRequest hooks decide first, as they do without it; it only ever denies, and allows nothing. Claude's questions and plan mode's tools are not offered to the model, and an MCP server's request for input is cancelled unless an Elicitation hook answers it. An app or script that answers prompts through canUseTool or --permission-prompt-tool is not asked either: answer from a PermissionRequest hook instead. Read from user settings, --settings and managed settings; project and local settings are ignored, and true in any of those sources wins.
