<!--
name: 'System Reminder: Compact file reference'
description: Reference to file read before conversation summarization
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
  - READ_TOOL_OBJECT
-->
Note: ${ATTACHMENT_OBJECT.filename} was read before the last conversation was summarized, but the contents are too large to include. Use ${READ_TOOL_OBJECT.name} tool if you need to access it.
