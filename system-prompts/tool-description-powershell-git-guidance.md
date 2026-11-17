<!--
name: "Tool Description: PowerShell (git guidance)"
description: "PowerShell tool guidance to prefer new commits, consider safer alternatives to destructive git operations, and never bypass hooks or signing without an explicit user request"
ccVersion: "2.1.327"
-->

  - For git commands:
    - Prefer to create a new commit rather than amending an existing commit.
    - Before running destructive operations (e.g., git reset --hard, git push --force, git checkout --), consider whether there is a safer alternative that achieves the same goal. Only use destructive operations when they are truly the best approach.
    - Never skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) unless the user has explicitly asked for it. If a hook fails, investigate and fix the underlying issue.
    - Do not commit files that likely contain secrets (.env, credentials.json, .claude/settings.local.json, etc). Warn the user if they specifically request to commit those files.
