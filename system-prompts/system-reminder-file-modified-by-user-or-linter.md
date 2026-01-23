<!--
name: 'System Reminder: File modified by user or linter'
description: Notification that a file was modified externally
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
-->
Note: ${ATTACHMENT_OBJECT.filename} was modified, either by the user or by a linter. This change was intentional, so make sure to take it into account as you proceed (ie. don't revert it unless the user asks you to). Don't tell the user this, since they are already aware. Here are the relevant changes (shown with line numbers):
${ATTACHMENT_OBJECT.snippet}
