<!--
name: "Data: Required Anthropic sign-in missing without organization setting"
description: "Explains a missing required sign-in when managed settings name no organization for cloud-provider sessions"
ccVersion: "2.1.329"
variables:
  - "SIGN_IN_REFUSAL_EFFECT_NOTE"
-->
This computer's managed settings require a sign-in to Anthropic (enforceAnthropicSignIn), and none is stored or this session cannot read it (`--bare` and an app that manages the provider read none), ${SIGN_IN_REFUSAL_EFFECT_NOTE}. For a session on Anthropic's API, run `claude auth login`, then start `claude` again. An organization sign-in (to the organization that your administrators manage in Anthropic's Enterprise Admin Console, not a claude.ai login) would count for a session on a cloud provider or behind a custom base URL, but only if these managed settings name that organization (forceLoginOrgUUID). They name none. If your company has such an organization, ask your administrator to add it. An API key, an auth token or a key helper is not a sign-in.
