<!--
name: 'Tool Description: Bash'
description: Description for the Bash tool, which allows Claude to run shell commands
ccVersion: 2.0.14
variables:
  - CUSTOM_TIMEOUT_MS
  - MAX_TIMEOUT_MS
  - MAX_OUTPUT_CHARS
  - BASH_TOOL_NAME
  - BASH_TOOL_EXTRA_NOTES
  - SEARCH_TOOL_NAME
  - GREP_TOOL_NAME
  - READ_TOOL_NAME
  - EDIT_TOOL_NAME
  - WRITE_TOOL_NAME
  - GIT_COMMIT_AND_PR_CREATION_INSTRUCTION
-->
Executes a given bash command in a persistent shell session with optional timeout, ensuring proper handling and security measures.

IMPORTANT: This tool is for terminal operations like git, npm, docker, etc. DO NOT use it for file operations (reading, writing, editing, searching, finding files) - use the specialized tools for this instead.

Before executing the command, please follow these steps:

1. Directory Verification:
   - If the command will create new directories or files, first use \`ls\` to verify the parent directory exists and is the correct location
   - For example, before running "mkdir foo/bar", first use \`ls foo\` to check that "foo" exists and is the intended parent directory

2. Command Execution:
   - Always quote file paths that contain spaces with double quotes (e.g., cd "path with spaces/file.txt")
   - Examples of proper quoting:
     - cd "/Users/name/My Documents" (correct)
     - cd /Users/name/My Documents (incorrect - will fail)
     - python "/path/with spaces/script.py" (correct)
     - python /path/with spaces/script.py (incorrect - will fail)
   - After ensuring proper quoting, execute the command.
   - Capture the output of the command.

Usage notes:
  - The command argument is required.
  - You can specify an optional timeout in milliseconds (up to ${CUSTOM_TIMEOUT_MS()}ms / ${CUSTOM_TIMEOUT_MS()/60000} minutes). If not specified, commands will timeout after ${MAX_TIMEOUT_MS()}ms (${MAX_TIMEOUT_MS()/60000} minutes).
  - It is very helpful if you write a clear, concise description of what this command does in 5-10 words.
  - If the output exceeds ${MAX_OUTPUT_CHARS()} characters, output will be truncated before being returned to you.
  - You can use the \`run_in_background\` parameter to run the command in the background, which allows you to continue working while the command runs. You can monitor the output using the ${BASH_TOOL_NAME} tool as it becomes available. Never use \`run_in_background\` to run 'sleep' as it will return immediately. You do not need to use '&' at the end of the command when using this parameter.
  ${BASH_TOOL_EXTRA_NOTES()}
  - Avoid using Bash with the \`find\`, \`grep\`, \`cat\`, \`head\`, \`tail\`, \`sed\`, \`awk\`, or \`echo\` commands, unless explicitly instructed or when these commands are truly necessary for the task. Instead, always prefer using the dedicated tools for these commands:
    - File search: Use ${SEARCH_TOOL_NAME} (NOT find or ls)
    - Content search: Use ${GREP_TOOL_NAME} (NOT grep or rg)
    - Read files: Use ${READ_TOOL_NAME} (NOT cat/head/tail)
    - Edit files: Use ${EDIT_TOOL_NAME} (NOT sed/awk)
    - Write files: Use ${WRITE_TOOL_NAME} (NOT echo >/cat <<EOF)
    - Communication: Output text directly (NOT echo/printf)
  - When issuing multiple commands:
    - If the commands are independent and can run in parallel, make multiple ${BASH_TOOL_NAME} tool calls in a single message. For example, if you need to run "git status" and "git diff", send a single message with two ${BASH_TOOL_NAME} tool calls in parallel.
    - If the commands depend on each other and must run sequentially, use a single ${BASH_TOOL_NAME} call with '&&' to chain them together (e.g., \`git add . && git commit -m "message" && git push\`). For instance, if one operation must complete before another starts (like mkdir before cp, Write before Bash for git operations, or git add before git commit), run these operations sequentially instead.
    - Use ';' only when you need to run commands sequentially but don't care if earlier commands fail
    - DO NOT use newlines to separate commands (newlines are ok in quoted strings)
  - Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of \`cd\`. You may use \`cd\` if the User explicitly requests it.
    <good-example>
    pytest /foo/bar/tests
    </good-example>
    <bad-example>
    cd /foo/bar && pytest tests
    </bad-example>

${GIT_COMMIT_AND_PR_CREATION_INSTRUCTION()}
