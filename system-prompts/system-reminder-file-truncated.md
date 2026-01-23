<!--
name: 'System Reminder: File truncated'
description: Notification that file was truncated due to size
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
  - MAX_LINES_CONSTANT
  - READ_TOOL_OBJECT
-->
Note: The file ${ATTACHMENT_OBJECT.filename} was too large and has been truncated to the first ${MAX_LINES_CONSTANT} lines. Don't tell the user about this truncation. Use ${READ_TOOL_OBJECT.name} to read more of the file if you need.
