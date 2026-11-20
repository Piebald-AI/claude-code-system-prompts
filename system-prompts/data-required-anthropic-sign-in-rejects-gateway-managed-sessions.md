<!--
name: "Data: Required Anthropic sign-in rejects gateway-managed sessions"
description: "Explains how an administrator can resolve a gateway-managed organization's conflict with enforced Anthropic sign-in"
ccVersion: "2.1.329"
variables:
  - "SIGN_IN_REFUSAL_PREFIX"
-->
${SIGN_IN_REFUSAL_PREFIX} This computer's managed settings require a sign-in to Anthropic (enforceAnthropicSignIn). The organization that you signed in to (an organization sign-in, not a claude.ai login) lets its gateway manage Claude Code. A session that a gateway manages does not meet that setting. Ask your administrator to do one of these two things: remove enforceAnthropicSignIn from this computer's managed settings and name the gateway in those settings (forceLoginGatewayUrl), or, in Anthropic's Enterprise Admin Console, change how the gateway is set up for Claude Code.
