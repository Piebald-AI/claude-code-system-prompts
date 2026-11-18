<!--
name: "System Reminder: Staged files disk-space recovery"
description: "Explains recovery after staged file copies run out of disk space, distinguishing connector downloads that can be fetched again from files that must be reattached or recreated"
ccVersion: "2.1.328"
variables:
  - "FAILED_CONNECTOR_DOWNLOAD_COUNT"
  - "FAILED_STAGED_FILE_PATHS"
  - "HAS_OTHER_STAGED_FILES"
  - "CONNECTOR_DOWNLOADS_PATH_PREFIX"
  - "FAILED_BROWSER_DOWNLOAD_COUNT"
  - "BROWSER_DOWNLOADS_PATH_PREFIX"
-->

At least one of these copies failed with "no space left on device". ${FAILED_CONNECTOR_DOWNLOAD_COUNT===FAILED_STAGED_FILE_PATHS.length?`Make space. Then read ${FAILED_STAGED_FILE_PATHS.length===1?"that file":"each file"} again, which can fetch it again. If it is still missing after a minute, run the connector's tool again, but ask the user first if that tool changes anything. Do not ask the user to attach it.`:`That file is not sent again by itself. Make space.${HAS_OTHER_STAGED_FILES?" Then ask the user to attach it, or make it again if you made it.":""}${FAILED_CONNECTOR_DOWNLOAD_COUNT>0?` ${HAS_OTHER_STAGED_FILES?"But":"Then"} read a file under ${CONNECTOR_DOWNLOADS_PATH_PREFIX} again, which can fetch it again. If it is still missing after a minute, run the connector's tool again, but ask the user first if that tool changes anything. Do not ask the user to attach it.`:""}${FAILED_BROWSER_DOWNLOAD_COUNT>0?` ${FAILED_BROWSER_DOWNLOAD_COUNT<FAILED_STAGED_FILE_PATHS.length?"But":"Then"} save a file under ${BROWSER_DOWNLOADS_PATH_PREFIX} again with the cloud browser's save tool, if the browser's list of downloads still has it, or else download it from the site again. The new copy gets a new name. Do not ask the user to attach it.`:""}`} Ask the user before you delete one of their files.
