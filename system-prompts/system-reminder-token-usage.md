<!--
name: 'System Reminder: Token usage'
description: Current token usage statistics
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
-->
Token usage: ${ATTACHMENT_OBJECT.used}/${ATTACHMENT_OBJECT.total}; ${ATTACHMENT_OBJECT.remaining} remaining
