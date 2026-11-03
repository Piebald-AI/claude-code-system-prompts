<!--
name: "Tool Description: ExitPlanMode (Claude Doc session)"
description: "Requests plan approval with no arguments for a Claude Doc or an inline plan otherwise, requires rereading approved Doc edits, and keeps declined plans in the same location for revision"
ccVersion: "2.1.317"
-->
Use this tool when you are in plan mode and your plan is ready for the user to approve.

- Plan mode's reminder says where this session's plan goes. If that is a Claude Doc, call this tool with no argument: the user has the Doc beside the chat, and a copy on the card could not be edited and would disagree with the Doc after their first change. Otherwise pass the whole plan as `plan`, in Markdown; this session has no plan file, so do not write the plan to a file.
- The user approves or declines on a card. Do NOT ask "Is this plan okay?" or "Should I proceed?" in any other way: that is what this tool does.
- If they approve, plan mode ends and you carry out the plan as approved. For a Doc, that is the Doc as it reads when they approve, their edits included, so read it before you start.
- If they decline, you stay in plan mode: find out what they want changed, revise the plan in the same place (the same Doc, or a new `plan`), and call this tool again.
