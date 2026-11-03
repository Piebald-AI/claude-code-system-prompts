<!--
name: "System Reminder: Async hook success additional context"
description: "Labels additional context from a successful asynchronous hook with the hook name when its response uses plain output framing"
ccVersion: "2.1.318"
variables:
  - "ATTACHMENT_OBJECT"
  - "HOOK_SPECIFIC_OUTPUT"
-->
${ATTACHMENT_OBJECT.hookName} hook success: ${HOOK_SPECIFIC_OUTPUT.additionalContext}
