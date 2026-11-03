<!--
name: "System Reminder: Staged files failed to arrive"
description: "Warns that staged file paths may be missing or outdated and adds specific remediation guidance for disk-space and filename-length failures"
ccVersion: "2.1.318"
variables:
  - "FAILED_STAGED_FILE_PATHS"
  - "IS_SINGLE_FAILED_FILE"
  - "FORMAT_STAGED_FILE_PATHS_FN"
  - "FILE_COPY_FAILURE_REASONS"
-->
${FAILED_STAGED_FILE_PATHS.length} ${IS_SINGLE_FAILED_FILE?"file":"files"} may not have arrived here, so ${IS_SINGLE_FAILED_FILE?"this path":"these paths"} may be missing or hold an older copy: ${FORMAT_STAGED_FILE_PATHS_FN(FAILED_STAGED_FILE_PATHS)}${FILE_COPY_FAILURE_REASONS.has("no_space")?`
At least one of these copies failed with "no space left on device". That file is not sent again by itself. Make space. Then ask the user to attach it, or make it again if you made it. Ask the user before you delete one of their files.`:""}${FILE_COPY_FAILURE_REASONS.has("name_too_long")?`
At least one of these names is too long for the file system here (the usual limit is 255 bytes). That file can arrive only after the name is made shorter.`:""}
