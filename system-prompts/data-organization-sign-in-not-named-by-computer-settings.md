<!--
name: "Data: Organization sign-in not named by computer settings"
description: "Explains why an organization sign-in is inactive when the computer's managed settings didn't name its organization"
ccVersion: "2.1.329"
-->
You have an organization sign-in (not a claude.ai login). This computer's managed settings did not name the organization of that sign-in when Claude Code started. So Claude Code uses none of these: that organization's cloud provider, your Anthropic API key, or your claude.ai login. To use a claude.ai login, run /login in an interactive session, or `claude auth login` at your shell prompt. Choose the account or organization that has your Claude subscription. That login replaces the organization sign-in. Or run `claude auth logout`, which signs you out of every account. Then start Claude Code again with your API key, or sign in. Or ask your IT administrator to add the organization to forceLoginOrgUUID in this computer's managed settings, if it isn't there yet. Then start Claude Code again with no API key set, because that setting refuses one.
