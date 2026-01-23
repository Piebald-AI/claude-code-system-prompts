<!--
name: 'System Reminder: Lines selected in IDE'
description: Notification about lines selected by user in IDE
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
  - TRUNCATED_CONTENT
-->
The user selected the lines ${ATTACHMENT_OBJECT.lineStart} to ${ATTACHMENT_OBJECT.lineEnd} from ${ATTACHMENT_OBJECT.filename}:
${TRUNCATED_CONTENT}

This may or may not be related to the current task.
