<!--
name: "System Reminder: Memory sync delete not sent"
description: "Tells Claude that memory sync is not sending changes, so a memory delete has probably not gone out and shared memory may still hold the content, and not to tell the user the content is gone or promise a place to delete it"
ccVersion: "2.1.323"
variables:
  - "DELETED_MEMORY_FILE_LIST"
-->
Memory sync is not sending changes right now, so the delete of ${DELETED_MEMORY_FILE_LIST} has probably not gone out. Shared memory may still hold that content, and other sessions can read it. If sync resumes during this session, the delete may still go out; if the session ends first, a later session can download that content again. Do not tell the user that content is gone, and if you already did, correct that. The user can usually delete a Project's files in the Memory section of that Project's settings on claude.ai, but other memory may have no such place, so do not promise one.
