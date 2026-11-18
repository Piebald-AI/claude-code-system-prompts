<!--
name: "System Reminder: Cross-session message held notice"
description: "Tells Claude that its message to another session is held and was not delivered, explains the permission-mode mismatch that usually causes it, and directs it not to report delivery, wait, or resend but to tell the user or choose another approach"
ccVersion: "2.1.328"
variables:
  - "CROSS_SESSION_DELIVERY_NOTICE_PREFIX"
  - "MESSAGES_SUBJECT_PHRASE"
  - "WAS_OR_WERE_VERB"
  - "RECIPIENT_DETAIL_SUFFIX"
  - "IT_OR_THEM_PRONOUN"
-->
${CROSS_SESSION_DELIVERY_NOTICE_PREFIX} ${MESSAGES_SUBJECT_PHRASE} ${WAS_OR_WERE_VERB} held by that session${RECIPIENT_DETAIL_SUFFIX}. NOT delivered: its Claude has not seen ${IT_OR_THEM_PRONOUN}. Do not report ${IT_OR_THEM_PRONOUN} as delivered, do not wait for a reply, and do not resend while held. The usual cause is that the two sessions run in different permission modes: a terminal session then asks its user to approve, but a Claude Desktop or non-interactive session cannot ask, so there the hold expires undelivered unless the modes come to match. A session can also be set to hold every message. Another notice follows on release, denial or expiry. Tell your user what is held and why, or choose another approach.
