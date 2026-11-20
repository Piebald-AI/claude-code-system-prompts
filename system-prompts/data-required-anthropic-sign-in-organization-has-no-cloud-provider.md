<!--
name: "Data: Required Anthropic sign-in organization has no cloud provider"
description: "Explains why required organization sign-in can't run without a cloud provider and gives administrator and account-switching steps"
ccVersion: "2.1.329"
variables:
  - "SIGN_IN_REFUSAL_PREFIX"
  - "IS_REQUEST_REFUSAL"
  - "ORGANIZATION_CLOUD_PROVIDER_MISSING_NOTE"
-->
${SIGN_IN_REFUSAL_PREFIX} This computer's managed settings require a sign-in to Anthropic (enforceAnthropicSignIn). ${IS_REQUEST_REFUSAL?ORGANIZATION_CLOUD_PROVIDER_MISSING_NOTE:"You use an organization sign-in (not a claude.ai login). That organization's settings name no cloud provider for Claude Code. Under that sign-in, Claude Code does not use a claude.ai login"}. Ask your administrator to set up a cloud provider, then start Claude Code again. Or, at your shell prompt, run `claude auth logout`. This command signs you out of every account. Then start Claude Code, sign in, and choose the account or organization that has your Claude subscription. An API key does not meet this setting.
