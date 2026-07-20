<!--
name: "Agent Prompt: /review slash command"
description: "Instructions for the /review command to review a GitHub pull request by gathering PR context and diff with gh, applying optional user instructions, and presenting verified findings"
ccVersion: "2.1.202"
variables:
  - "PR_NUMBER"
  - "ADDITIONAL_REVIEW_INSTRUCTIONS"
-->
Review target: GitHub pull request `${PR_NUMBER}`.

Gather this target's diff with (instead of any local `git diff`):
1. `gh pr view ${PR_NUMBER} --json title,body,author,baseRefName,headRefName,state,additions,deletions,changedFiles,labels` for context
2. `gh pr diff ${PR_NUMBER}` for the unified diff

The PR's diff is the only review scope — local working-tree changes are out of scope. When you need surrounding code, Read the files in this checkout if it matches the PR's branch, otherwise fetch file contents via `gh`.
${ADDITIONAL_REVIEW_INSTRUCTIONS?`
Additional instructions from the user: ${ADDITIONAL_REVIEW_INSTRUCTIONS}
`:""}
Analyze the changes and provide a thorough code review that includes:
- An overview of what the PR does
- Analysis of code quality and style
- Specific suggestions for improvements
- Any potential issues or risks

Keep your review concise but thorough. Focus on:
- Code correctness
- Following project conventions
- Performance implications
- Test coverage
- Security considerations

Format your review with clear sections and bullet points.
