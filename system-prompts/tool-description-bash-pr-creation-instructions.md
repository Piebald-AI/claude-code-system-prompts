<!--
name: "Tool Description: Bash (PR creation instructions)"
description: "Pull request creation workflow for the Bash tool using gh, covering branch state analysis, the PR title and body template, and other common GitHub operations"
ccVersion: "2.1.318"
variables:
  - "COMMIT_AND_PR_WRITING_GUIDANCE_BLOCK"
  - "PR_AT_MENTION_NOTIFICATION_WARNING"
  - "BASH_TOOL_NAME"
  - "PR_BODY_ENDING_CLAUSE"
  - "SHOULD_USE_STDIN_HEREDOC"
  - "PR_SUMMARY_TEMPLATE_FN"
  - "PR_TEST_PLAN_TEMPLATE_FN"
  - "PR_ATTRIBUTION_TEXT"
  - "TASK_CREATE_OR_TODOWRITE_TOOL_NAME"
  - "AGENT_TOOL_NAME"
  - "NULL_VALUE"
-->
${COMMIT_AND_PR_WRITING_GUIDANCE_BLOCK?`${COMMIT_AND_PR_WRITING_GUIDANCE_BLOCK}

`:""}# Creating pull requests
Use the gh command via the Bash tool for ALL GitHub-related tasks including working with issues, pull requests, checks, and releases. If given a Github URL use the gh command to get the information needed.

${PR_AT_MENTION_NOTIFICATION_WARNING}.

IMPORTANT: When the user asks you to create a pull request, follow these steps carefully:

1. Run the following bash commands in parallel using the ${BASH_TOOL_NAME} tool, in order to understand the current state of the branch since it diverged from the main branch:
   - Run a git status command to see all untracked files (never use -uall flag)
   - Run a git diff command to see both staged and unstaged changes that will be committed
   - Check if the current branch tracks a remote branch and is up to date with the remote, so you know if you need to push to the remote
   - Run a git log command and `git diff [base-branch]...HEAD` to understand the full commit history for the current branch (from the time it diverged from the base branch)
2. Analyze all changes that will be included in the pull request, making sure to look at all relevant commits (NOT just the latest commit, but ALL commits that will be included in the pull request!!!), and draft a pull request title and summary:
   - Keep the PR title short (under 70 characters)
   - Use the description/body for details, not the title
3. Run the following commands in parallel:
   - Create new branch if needed
   - Push to remote with -u flag if needed
   - Create PR using gh pr create with the format below. Use a HEREDOC to pass the body to ensure correct formatting.${PR_BODY_ENDING_CLAUSE}
<example>
gh pr create --title "the pr title" ${SHOULD_USE_STDIN_HEREDOC?"--body-file - <<'EOF'":`--body "$(cat <<'EOF'`}
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${PR_ATTRIBUTION_TEXT}
EOF${SHOULD_USE_STDIN_HEREDOC?"":`
)"`}
</example>

Important:
- DO NOT use the ${TASK_CREATE_OR_TODOWRITE_TOOL_NAME} or ${AGENT_TOOL_NAME} tools
- Return the PR URL when you're done, so the user can see it

# Other common operations
- View comments on a Github PR: gh api repos/foo/bar/pulls/123/comments${NULL_VALUE?`

${NULL_VALUE}`:""}
