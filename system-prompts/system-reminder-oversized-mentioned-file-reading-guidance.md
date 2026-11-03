<!--
name: "System Reminder: Oversized mentioned file reading guidance"
description: "Directs reading an unattached oversized mentioned file in portions, estimates the required calls and requires disclosure when an answer uses only searches or partial content"
ccVersion: "2.1.318"
variables:
  - "MENTIONED_FILES_NOTICE"
  - "FORMAT_FILE_SIZE_FN"
  - "ATTACHMENT_OBJECT"
  - "READ_TOOL_NAME"
  - "ESTIMATED_READ_CALL_COUNT"
  - "PLURALIZE_FN"
-->
${MENTIONED_FILES_NOTICE} (${FORMAT_FILE_SIZE_FN(ATTACHMENT_OBJECT.fileSize)}). It was too large to attach, so you have not seen any of it. Read all of it before you answer, in portions with ${READ_TOOL_NAME}'s offset and limit, unless the request needs only a part of it, such as one fact that a search can find or a first look at what the file holds. A search shows only the lines that match its words, so it misses what is worded differently. ${ATTACHMENT_OBJECT.readAllOfIt==="over_size_limit"?`${READ_TOOL_NAME} needs a limit for a file this large, and it returns`:`${READ_TOOL_NAME} returns`} at most 25,000 tokens a call, about 60 KB of plain text, so the whole file takes about ${ESTIMATED_READ_CALL_COUNT} ${PLURALIZE_FN(ESTIMATED_READ_CALL_COUNT,"call")}. If you answer from searches or from part of the file, tell the user so, and name what you searched for.
