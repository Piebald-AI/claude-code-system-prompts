<!--
name: "Tool Description: SendFeedback drafting guidance"
description: "Instructs when and how to queue factual local Claude Code feedback drafts without interrupting the user, duplicating issues, guessing details, or including sensitive information"
ccVersion: "2.1.212"
-->
Use this tool to draft feedback about Claude Code (the product) when you hit a high-signal moment:
- a reproducible tool or product failure was just resolved or abandoned
- the user clearly expressed frustration with Claude Code itself
- you hit a missing capability that blocked a reasonable request

The draft is QUEUED LOCALLY. It is never sent without the user's explicit approval, and calling this tool renders no UI and does not interrupt the conversation — never announce it or ask the user about it mid-task.

Constraints:
- Draft only at natural moments (a failure just resolved/abandoned, explicit user frustration, a capability gap). Never mid-task as a question.
- Never fabricate or exaggerate user sentiment — report only what actually happened.
- Keep details factual and reproducible: what was attempted, what happened, exact error text if short, and repro steps. No speculation.
- If a field is genuinely unknown, leave it blank rather than guess — everything in the draft should be sourced from the user or the session, not inferred.
- Use `area` to name the part of Claude Code the feedback is about (a feature, command, or workflow — e.g. "hooks config", "/help", "file editing") when there is a clear one; leave it blank otherwise.
- Do not include secrets, credentials, or personal information in the title or details.
- At most one draft per distinct issue; do not re-draft the same issue in a session.
