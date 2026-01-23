<!--
name: 'System Reminder: Hook blocking error'
description: Error from a blocking hook command
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
-->
${ATTACHMENT_OBJECT.hookName} hook blocking error from command: "${ATTACHMENT_OBJECT.blockingError.command}": ${ATTACHMENT_OBJECT.blockingError.blockingError}
