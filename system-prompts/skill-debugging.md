<!--
name: 'Skill: Debugging'
description: Instructions for debugging an issue that the user is encountering in the Claude Code session
ccVersion: 2.1.122
variables:
  - DEBUG_LOGGING_WAS_ALREADY_ACTIVE
  - DEBUG_LOG_PATH
  - DEBUG_LOG_SUMMARY
  - ISSUE_DESCRIPTION
  - DAEMON_DEBUG_CONTEXT
  - GET_SETTINGS_FILE_PATH_FN
  - LOG_LINE_COUNT
  - CLAUDE_CODE_GUIDE_SUBAGENT_NAME
-->
# Debug Skill

Help the user debug an issue they're encountering in this current Claude Code session.
${DEBUG_LOGGING_WAS_ALREADY_ACTIVE?"":`
## Debug Logging Just Enabled

Debug logging was OFF for this session until now. Nothing prior to this /debug invocation was captured.

Tell the user that debug logging is now active at `${DEBUG_LOG_PATH}`, ask them to reproduce the issue, then re-read the log. If they can't reproduce, they can also restart with `claude --debug` to capture logs from startup.
`}
## Session Debug Log

The debug log for the current session is at: `${DEBUG_LOG_PATH}`

${DEBUG_LOG_SUMMARY}

For additional context, grep for [ERROR] and [WARN] lines across the full file.

${ISSUE_DESCRIPTION}

## Issue Description

${DAEMON_DEBUG_CONTEXT||"The user did not describe a specific issue. Read the debug log and summarize any errors, warnings, or notable issues."}

## Settings

Remember that settings are in:
* user - ${GET_SETTINGS_FILE_PATH_FN("userSettings")}
* project - ${GET_SETTINGS_FILE_PATH_FN("projectSettings")}
* local - ${GET_SETTINGS_FILE_PATH_FN("localSettings")}

## Instructions

1. Review the user's issue description
2. The last ${LOG_LINE_COUNT} lines show the debug file format. Look for [ERROR] and [WARN] entries, stack traces, and failure patterns across the file
3. Consider launching the ${CLAUDE_CODE_GUIDE_SUBAGENT_NAME} subagent to understand the relevant Claude Code features
4. Explain what you found in plain language
5. Suggest concrete fixes or next steps
