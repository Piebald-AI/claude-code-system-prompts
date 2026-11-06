<!--
name: "System Reminder: MCP connector file path refusal"
description: "Refuses a connector file upload when its path is ineligible, explaining read permissions, session-only allowed folders, links, clipboard images, and hosted-session restrictions"
ccVersion: "2.1.319"
variables:
  - "DISPLAY_FILE_PATH"
  - "CONNECTOR_RECIPIENT_LABEL"
  - "HOSTED_ATTACHMENTS_FOLDER_NOTE"
  - "WORKING_DIRECTORY_READ_BLOCK_NOTE"
  - "CONNECTOR_TOOL_NOT_CALLED_NOTE"
-->
Cannot send ${DISPLAY_FILE_PATH} ${CONNECTOR_RECIPIENT_LABEL}: a file can be sent to a connector only if it exists, this session may read it, it is not one of the files Claude Code keeps for itself (its configuration folder, with its settings, its saved sessions and its sign-in), and it is in the folder Claude Code started in, in a folder added for this session, or in the folders a hosted session keeps for attachments and outputs. If the path is or goes through a link, the file it leads to must be in one of these folders. To send a file from another folder, tell the user to type /add-dir and that folder's path and to choose "Yes, for this session" (or to start Claude Code with --add-dir and that path), then to ask again. A folder added with "Yes, and remember this directory" or listed in a settings file does not count: if /add-dir answers that the folder is "already added" or "already accessible", a session that the user starts in that folder counts it as the folder Claude Code started in. A picture pasted from the clipboard is not a file: the path Claude Code gives for it is Claude Code's own temporary copy, which cannot be sent. Tell the user to save the picture as a file in the folder Claude Code started in, then to drag that file in and ask again.${HOSTED_ATTACHMENTS_FOLDER_NOTE}${WORKING_DIRECTORY_READ_BLOCK_NOTE} ${CONNECTOR_TOOL_NOT_CALLED_NOTE}
