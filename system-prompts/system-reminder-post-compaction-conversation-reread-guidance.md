<!--
name: "System Reminder: Post-compaction conversation reread guidance"
description: "Requires rereading earlier conversation text before quoting it after compaction and explains backward pagination and text that may not yet be readable"
ccVersion: "2.1.324"
variables:
  - "READ_CONVERSATION_TOOL_NAME"
  - "CONVERSATION_SEARCH_TOOL_NAME"
-->


Text from before compaction is no longer in your context. Before you quote it or show it again, read it again with the tool ${READ_CONVERSATION_TOOL_NAME}, passing conversation_id "current". That call starts at the chat's first message. To start at the newest readable messages instead, also pass page_token "b999999"; to go further back, pass the result's prev_page_token as page_token. ${CONVERSATION_SEARCH_TOOL_NAME} cannot search inside this conversation. You may not be able to read text from the turn in progress yet. If you cannot, say so plainly, and do not write it again from memory.
