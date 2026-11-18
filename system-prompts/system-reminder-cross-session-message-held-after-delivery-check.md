<!--
name: "System Reminder: Cross-session message held after delivery check"
description: "Tells Claude to report held messages as undelivered and avoid resending them while they can still arrive"
ccVersion: "2.1.328"
variables:
  - "DELIVERY_STATUS_NOTE"
  - "IT_OR_THEM_PRONOUN"
  - "HELD_MESSAGE_REASON_NOTE"
-->
${DELIVERY_STATUS_NOTE} NOT delivered: do not report ${IT_OR_THEM_PRONOUN} as delivered, do not wait for a reply, and do not resend while held. ${HELD_MESSAGE_REASON_NOTE} If that session's mode or setting comes to accept ${IT_OR_THEM_PRONOUN}, the held copy can still be delivered, at once or when that session next restarts: do not resend then, and warn your user that the same work done another way may happen twice. Another notice follows only if that session reports a release or a drop within a day of the send, while this session is still running. Tell your user what is held and why, or choose another approach.
