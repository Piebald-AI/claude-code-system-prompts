<!--
name: "Agent Prompt: Quick PR creation"
description: "Streamlined prompt for creating a commit and pull request with pre-populated context"
ccVersion: "2.1.206"
variables:
  - "PREAMBLE_BLOCK"
  - "SAFE_USER_VALUE"
  - "WHOAMI_VALUE"
  - "DEFAULT_BRANCH"
  - "IS_BASH_ENV_FN"
  - "REPO_PR_TEMPLATE_CONTEXT_BLOCK"
  - "COMMIT_ATTRIBUTION_TEXT"
  - "PR_EDIT_OPTIONS_NOTE"
  - "PR_CREATE_OPTIONS_NOTE"
  - "PR_WRITING_GUIDANCE_FN"
  - "PR_SUMMARY_TEMPLATE_FN"
  - "PR_TEST_PLAN_TEMPLATE_FN"
  - "PR_BODY_EXTRA_SECTIONS"
  - "PR_ATTRIBUTION_TEXT"
  - "PR_SLACK_SHARING_FOLLOWUP_NOTE"
-->
${PREAMBLE_BLOCK}## Context

- `SAFEUSER`: ${SAFE_USER_VALUE}
- `whoami`: ${WHOAMI_VALUE}
- `git status`: !`git status`
- `git diff HEAD`: !`git diff HEAD`
- `git branch --show-current`: !`git branch --show-current`
- `git diff ${DEFAULT_BRANCH}...HEAD`: !`git diff ${DEFAULT_BRANCH}...HEAD`
- `gh pr view --json number`: !`${IS_BASH_ENV_FN()?"gh pr view --json number 2>/dev/null || true":'gh pr view --json number 2>$null; if (-not $?) { "" }'}`${REPO_PR_TEMPLATE_CONTEXT_BLOCK}

## Git Safety Protocol

- NEVER update the git config
- NEVER run destructive/irreversible git commands (like push --force, hard reset, etc) unless the user explicitly requests them
- NEVER skip hooks (--no-verify, --no-gpg-sign, etc) unless the user explicitly requests it
- NEVER run force push to main/master, warn the user if they request it
- Do not commit files that likely contain secrets (.env, credentials.json, etc)
- Never use git commands with the -i flag (like git rebase -i or git add -i) since they require interactive input which is not supported

## Your task

Analyze all changes that will be included in the pull request, making sure to look at all relevant commits (NOT just the latest commit, but ALL commits that will be included in the pull request from the git diff ${DEFAULT_BRANCH}...HEAD output above).

Based on the above changes:
1. Create a new branch if on ${DEFAULT_BRANCH} (use SAFEUSER from context above for the branch name prefix, falling back to whoami if SAFEUSER is empty, e.g., `username/feature-name`)
2. Create a single commit with an appropriate message${COMMIT_ATTRIBUTION_TEXT?", ending with the attribution text shown in the example below":""}:
${IS_BASH_ENV_FN()?````
git commit -m "$(cat <<'EOF'
Commit message here.${COMMIT_ATTRIBUTION_TEXT?`

${COMMIT_ATTRIBUTION_TEXT}`:""}
EOF
)"
````:````
git commit -m @'
Commit message here.${COMMIT_ATTRIBUTION_TEXT?`

${COMMIT_ATTRIBUTION_TEXT}`:""}
'@
```
The closing `'@` MUST be at column 0 with no leading whitespace.`}
3. Push the branch to the repo's remote (usually `origin`; use the remote this repo is actually configured with)
4. If a PR already exists for this branch (check the gh pr view output above), update the PR title and body using `gh pr edit` to reflect the current diff${PR_EDIT_OPTIONS_NOTE}. Otherwise, create a pull request using `gh pr create` with the multi-line body syntax shown below${PR_CREATE_OPTIONS_NOTE}.
   - IMPORTANT: Keep PR titles short (under 70 characters). Use the body for details.${PR_WRITING_GUIDANCE_FN(REPO_PR_TEMPLATE_CONTEXT_BLOCK?"embedded_context":null)}
${IS_BASH_ENV_FN()?````
gh pr create --title "Short, descriptive title" --body "$(cat <<'EOF'
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${PR_BODY_EXTRA_SECTIONS}${PR_ATTRIBUTION_TEXT?`

${PR_ATTRIBUTION_TEXT}`:""}
EOF
)"
````:````
gh pr create --title "Short, descriptive title" --body @'
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${PR_BODY_EXTRA_SECTIONS}${PR_ATTRIBUTION_TEXT?`

${PR_ATTRIBUTION_TEXT}`:""}
'@
````}

You have the capability to call multiple tools in a single response. You MUST do all of the above in a single message.${PR_SLACK_SHARING_FOLLOWUP_NOTE}

Return the PR URL when you're done, so the user can see it.
