<!--
name: "System Reminder: Code Mode auto mode hook rewrite refusal"
description: "Refuses Code Mode execution after a hook rewrites a call and limits retries before directing the user to adjust the hook or permission mode"
ccVersion: "2.1.318"
-->
This code was NOT run. In Code Mode, auto mode doesn't run code after a hook changed its call from what you wrote. This also applies when a hook changed an earlier tool call in the same response. This is not a judgment that the code is unsafe. If this response had other tool calls, you may send this code once more, in a response with no other tool calls. Otherwise, don't send it again. Go on with work that doesn't need it, and tell the user that a hook (a PreToolUse hook, or a mod's) changes your code. They can turn that hook off (or ask their administrator, if their organization set it), or leave auto mode with Shift+Tab (for example for Manual mode), where they are asked about each of the code's tool calls that needs approval.
