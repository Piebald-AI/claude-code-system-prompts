<!--
name: "System Reminder: Device file commit storage delay"
description: "Directs a device file commit retry after storage catches up, then isolates waiting files and requests a fresh upload or reports that saving failed"
ccVersion: "2.1.331"
variables:
  - "SEND_USER_FILE_TOOL_NAME"
  - "PROJECT_FILES_DIRECTORY"
-->
Nothing was copied: the newest version of a file in this call may not be stored yet. Make sure nothing is still writing these files or holding them open, wait ten seconds, and call device_commit_files again. If it fails again, copy the files one call at a time to find the one that waits. For that file, call ${SEND_USER_FILE_TOOL_NAME} now, if you have it, and pass the new fileUuid in place of stagedPath, or tell the user that it could not be saved yet. A file under ${PROJECT_FILES_DIRECTORY} also waits while the project's storage is full.
