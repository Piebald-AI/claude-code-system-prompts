<!--
name: 'System Reminder: Hook additional context'
description: Additional context from a hook
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
-->
${ATTACHMENT_OBJECT.hookName} hook additional context: ${ATTACHMENT_OBJECT.content.join(`
`)}
