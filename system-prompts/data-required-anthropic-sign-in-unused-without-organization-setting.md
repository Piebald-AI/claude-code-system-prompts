<!--
name: "Data: Required Anthropic sign-in unused without organization setting"
description: "Explains why a saved sign-in isn't used when managed settings name no organization, including credential and host overrides"
ccVersion: "2.1.329"
variables:
  - "SIGN_IN_REFUSAL_EFFECT_NOTE"
-->
This computer's managed settings require a sign-in to Anthropic (enforceAnthropicSignIn), and this session does not run under the one that is stored, ${SIGN_IN_REFUSAL_EFFECT_NOTE}. A claude.ai login counts for a session on Anthropic's API. An organization sign-in (to the organization that your administrators manage in Anthropic's Enterprise Admin Console, not a claude.ai login) would count for a session on a cloud provider or behind a custom base URL, but only if these managed settings name that organization (forceLoginOrgUUID). They name none. If your company has such an organization, ask your administrator to add it. Other causes, on Anthropic's API: `--bare`; an Anthropic API key, an auth token or a key helper, which decides before the sign-in (unset `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` if one is set); an `Authorization` line or an API key line in `ANTHROPIC_CUSTOM_HEADERS`; Claude Desktop or another app that starts Claude Code and manages the provider.
