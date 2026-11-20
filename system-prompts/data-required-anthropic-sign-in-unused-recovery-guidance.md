<!--
name: "Data: Required Anthropic sign-in unused recovery guidance"
description: "Lists credential overrides, provider choices and managed-settings problems that can keep a required saved sign-in from being used"
ccVersion: "2.1.329"
variables:
  - "SIGN_IN_REFUSAL_EFFECT_NOTE"
  - "GET_ORGANIZATION_SIGN_IN_COMMAND_FN"
-->
This computer's managed settings require a sign-in to Anthropic (enforceAnthropicSignIn), and this session does not run under the one that is stored, ${SIGN_IN_REFUSAL_EFFECT_NOTE}. A claude.ai login counts for a session on Anthropic's API. An organization sign-in (to the organization that your administrators manage in Anthropic's Enterprise Admin Console) counts for a session on a cloud provider or behind a custom base URL that takes that organization's settings. The usual causes: `--bare`; an Anthropic API key, an auth token or a key helper, which decides before a claude.ai login (unset `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` if one is set); a claude.ai login on a session that is not on Anthropic's API, with no organization sign-in stored (run ${GET_ORGANIZATION_SIGN_IN_COMMAND_FN()}); an organization sign-in on a session that is on Anthropic's API; an `Authorization` line or an API key line in `ANTHROPIC_CUSTOM_HEADERS`; Claude Desktop or another app that starts Claude Code and manages the provider; a Claude apps gateway session, or `CLAUDE_CODE_USE_GATEWAY`; the computer's own managed settings, which keep priority over the organization that you signed in to unless their `forceLoginOrgUUID` names it (ask your administrator); a managed settings file that Claude Code could not read (start `claude` again, and if the problem continues, ask your administrator).
