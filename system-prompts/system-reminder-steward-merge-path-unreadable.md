<!--
name: "System Reminder: Steward merge path unreadable"
description: "Leaves merges to the user when a link or unreadable path prevents checking changes to execution settings"
ccVersion: "2.1.330"
variables:
  - "PROTECTED_SETTINGS_PATHS"
  - "UNREADABLE_PATH"
  - "FORMAT_CHECKOUT_PATH_FN"
  - "CHECKOUT_ROOT"
-->
in this checkout ${PROTECTED_SETTINGS_PATHS.includes(UNREADABLE_PATH)?FORMAT_CHECKOUT_PATH_FN(CHECKOUT_ROOT,UNREADABLE_PATH):"a file that git reads its settings from (git config --show-origin --get-regexp '^include' lists what is taken in), or a folder above it,"} is a link, or can't be read, on the way to a file that tells Claude Code or git what to run, such as Claude Code's settings or .mcp.json, so whether a merge would change that file can't be told beforehand. Leave every merge to the user: tell them so once, and that they can run the merge themselves, go on with the rest, and don't try one again while the link stands
