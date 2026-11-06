<!--
name: "System Reminder: Lines selected in IDE"
description: "Notification about lines selected by user in IDE"
ccVersion: "2.1.319"
variables:
  - "ATTACHMENT_OBJECT"
  - "ESCAPE_UNTRUSTED_TEXT_FN"
  - "NEUTRALIZE_UNTRUSTED_ATTACHMENT_TAGS_FN"
  - "TRUNCATE_CONTENT_FN"
-->
The user selected the lines ${ATTACHMENT_OBJECT.lineStart} to ${ATTACHMENT_OBJECT.lineEnd} from ${ESCAPE_UNTRUSTED_TEXT_FN(ATTACHMENT_OBJECT.filename)}:
${NEUTRALIZE_UNTRUSTED_ATTACHMENT_TAGS_FN(TRUNCATE_CONTENT_FN(ATTACHMENT_OBJECT.content),ATTACHMENT_OBJECT,ATTACHMENT_OBJECT.filename)}

This may or may not be related to the current task.
