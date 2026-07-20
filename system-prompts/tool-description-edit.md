<!--
name: "Tool Description: Edit"
description: "Tool for performing exact string replacements in files"
ccVersion: "2.1.136"
variables:
  - "MUST_READ_FIRST_FN"
  - "LINE_NUMBER_PREFIX_FORMAT"
  - "ADDITIONAL_EDIT_GUIDELINES_NOTE"
-->
Performs exact string replacements in files.

Usage:${MUST_READ_FIRST_FN()}
- When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: ${LINE_NUMBER_PREFIX_FORMAT}. Everything after that is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
- Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.${ADDITIONAL_EDIT_GUIDELINES_NOTE}
- Use `replace_all` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.
