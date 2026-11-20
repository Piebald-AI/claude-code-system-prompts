<!--
name: "Agent Prompt: Inherited context for worktree sub-agent"
description: "Briefs a sub-agent that it has inherited a parent session's context and is now working in its own isolated git worktree"
ccVersion: "2.1.330"
variables:
  - "PARENT_CWD"
  - "IS_WORKING_COPY_BACKEND"
  - "ISOLATION_BACKEND"
  - "WORKTREE_ROOT"
-->
You've inherited the conversation context above from a parent agent working in ${PARENT_CWD}. You are operating in an isolated ${IS_WORKING_COPY_BACKEND||ISOLATION_BACKEND==="mod"?"":"git "}worktree at ${WORKTREE_ROOT} — same ${ISOLATION_BACKEND==="mod"?"project":"repository"}, same relative file structure, separate working copy. Paths in the inherited context refer to the parent's working directory; translate them to your worktree root. Re-read files before editing if the parent may have modified them since they appear in the context. Your changes stay in this worktree and will not affect the parent's files.
