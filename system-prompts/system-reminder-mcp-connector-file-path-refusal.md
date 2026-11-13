<!--
name: "System Reminder: MCP connector file path refusal"
description: "Refuses a connector file send without revealing whether the path exists and explains session-folder access, read restrictions and how to retry"
ccVersion: "2.1.324"
variables:
  - "FILE_SEND_REFUSAL_PREFIX"
  - "READ_BLOCK_SETTING_NAMES"
  - "HAS_MULTIPLE_FILES"
  - "HOSTED_ATTACHMENTS_FOLDER_NOTE"
  - "CONNECTOR_TOOL_NOT_CALLED_NOTE"
-->
${FILE_SEND_REFUSAL_PREFIX}: there is no such file, or Claude Code does not send it from outside this session's folders (for example a link, a folder, a file that is too large or named like a credential, one of Claude Code's own files, ${READ_BLOCK_SETTING_NAMES===""?"":`one that ${READ_BLOCK_SETTING_NAMES} covers, `}or one that is not in the user's home or temporary folder, on that folder's own disk). Claude Code does not say which, so that a refusal cannot show what is there.${HAS_MULTIPLE_FILES?" This may be about any of this call's files, or about how many the approval prompt can list: send one per call.":""} If the path is right, the user can add its folder with /add-dir ("Yes, for this session"), or start Claude Code there, and ask again.${HOSTED_ATTACHMENTS_FOLDER_NOTE} ${CONNECTOR_TOOL_NOT_CALLED_NOTE}
