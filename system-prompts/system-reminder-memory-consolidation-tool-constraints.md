<!--
name: "System Reminder: Memory consolidation tool constraints"
description: "Restricts the memory consolidation job to read-only shell access plus deleting memory files and lists sessions to review"
ccVersion: "2.1.173"
variables:
  - "SESSIONS_TO_REVIEW"
  - "SESSION_ID"
-->


**Tool constraints for this run:** Shell access is restricted to read-only commands (`ls`, `find`, `grep`, `cat`, `stat`, `wc`, `head`, `tail`, and similar) plus deleting `.md` paths inside the memory directory. Anything else that writes, redirects to a file, or modifies state will be denied. Plan your exploration with this in mind — no need to probe.

Sessions since last consolidation (${SESSIONS_TO_REVIEW.length}):
${SESSIONS_TO_REVIEW.map((SESSION_ID)=>`- ${SESSION_ID}`).join(`
`)}
