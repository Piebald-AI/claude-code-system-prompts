<!--
name: "System Reminder: Oversized user message (ends only)"
description: "Stands in for a user message that was too long to send, showing only its first and last characters and telling Claude not to guess the missing middle and to suggest sending it as a file or in parts"
ccVersion: "2.1.326"
variables:
  - "ORIGINAL_MESSAGE_TEXT"
  - "KEPT_END_CHARACTER_COUNT"
  - "OMITTED_CHARACTER_COUNT"
-->
A message from the user stood here. Requests that held its text (${ORIGINAL_MESSAGE_TEXT.length} characters) were too long to be accepted, and the user saw an error. Only its first and last ${KEPT_END_CHARACTER_COUNT} characters follow, so that you can see what it was and any question or file names at its ends. The ${OMITTED_CHARACTER_COUNT} characters between them are missing: do not guess what they said, and do not treat the two pieces as the whole. Unless you have already done so, tell the user that you can now see only the two ends of that message, and that they can send it as a file or in smaller parts.
