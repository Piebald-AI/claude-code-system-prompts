<!--
name: 'System Reminder: File shorter than offset'
description: Warning when file read offset exceeds file length
ccVersion: 2.1.18
variables:
  - RESULT_OBJECT
-->
<system-reminder>Warning: the file exists but is shorter than the provided offset (${RESULT_OBJECT.file.startLine}). The file has ${RESULT_OBJECT.file.totalLines} lines.</system-reminder>
