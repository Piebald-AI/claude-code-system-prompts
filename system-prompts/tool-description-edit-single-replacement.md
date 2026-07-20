<!--
name: "Tool Description: Edit single replacement"
description: "Tool description for performing exact string replacement in a file, including prior-read and line-prefix requirements"
ccVersion: "2.1.173"
variables:
  - "READ_TOOL_NAME"
  - "SUPPORTS_COLON_LINE_PREFIX"
-->
Performs exact string replacement in a file.

- You must ${READ_TOOL_NAME} the file in this conversation before editing, or the call will fail.
- `old_string` must match the file exactly, including indentation, and be unique — the edit fails otherwise. Strip the Read line prefix (${SUPPORTS_COLON_LINE_PREFIX?"line number + a single tab or `:`":"line number + tab"}) before matching.
- `replace_all: true` replaces every occurrence instead.
