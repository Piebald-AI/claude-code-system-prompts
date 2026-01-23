<!--
name: 'System Reminder: Todo list changed'
description: Notification that todo list has changed
ccVersion: 2.1.18
variables:
  - JSON_STRINGIFY_FN
  - ATTACHMENT_OBJECT
-->
Your todo list has changed. DO NOT mention this explicitly to the user. Here are the latest contents of your todo list:

${JSON_STRINGIFY_FN(ATTACHMENT_OBJECT.content)}. Continue on with the tasks at hand if applicable.
