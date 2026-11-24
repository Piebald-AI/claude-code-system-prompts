<!--
name: "Data: Steward relative PATH entry refusal"
description: "Identifies empty or relative PATH entries that make the git and gh programs uncertain and tells the user how to replace or remove them before restarting Claude Code"
ccVersion: "2.1.331"
variables:
  - "FIRST_UNSAFE_PATH_INDEX"
  - "PATH_ENTRIES"
  - "UNSAFE_PATH_INDICES"
  - "UNSAFE_PATH_ENTRY"
  - "IS_UNATTENDED_WATCH"
  - "PATH_ENTRY_INDEX_BINDING"
-->
entry ${FIRST_UNSAFE_PATH_INDEX+1} of ${PATH_ENTRIES.length} on your PATH${UNSAFE_PATH_INDICES.length>1?` (and ${UNSAFE_PATH_INDICES.length-1} more)`:""} ${UNSAFE_PATH_ENTRY===""?"is empty (a stray colon), which stands for the current folder":UNSAFE_PATH_ENTRY==="."?'is ".", the current folder':UNSAFE_PATH_ENTRY.startsWith("~")?'begins with "~", which only a shell expands':"is a relative path, which changes with the current folder"}, so it isn't clear which gh and git ${IS_UNATTENDED_WATCH?"an unattended watch ":""}would run. Take ${UNSAFE_PATH_INDICES.length>1?"them":"it"} out${UNSAFE_PATH_INDICES.every((PATH_ENTRY_INDEX_BINDING)=>PATH_ENTRIES[PATH_ENTRY_INDEX_BINDING]==="")?" of your shell's profile, and out of":`, or write ${UNSAFE_PATH_INDICES.length>1?"them as full paths":"it as a full path"}, in your shell's profile, and in`} Claude Code's settings if an env block there sets PATH, then quit Claude Code and start it again from a new terminal
