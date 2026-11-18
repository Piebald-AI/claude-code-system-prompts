<!--
name: "Data: MCP hook on_failure field"
description: "Explains when a failed MCP hook call lets an action proceed or stops it"
ccVersion: "2.1.328"
-->
What happens when this hook's call fails: its MCP server is not connected or not signed in, the call times out or returns an error, or the tool answers with JSON that fails validation. 'continue' (default): the failure is reported and the action goes ahead. 'block': the action the event guards (a tool call, a permission request, a prompt) is blocked each time, for as long as the call fails. With 'block', the tool must answer with a hook's JSON output, with {} or with nothing: plain text, an image, or JSON that holds none of a hook output's fields, or only 'reason', also counts as a failure. That does not hold on PreCompact and WorktreeCreate, where plain text is the hook's answer, or on events whose block stops nothing. Any other value reads as 'block'. Ignored on Setup, SessionStart, Stop, SubagentStop, TaskCompleted and TeammateIdle.
