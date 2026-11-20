<!--
name: "Data: Required Anthropic sign-in host provider refusal"
description: "Explains why a host-managed provider can't meet the computer's Anthropic sign-in requirement and how to sign in from a terminal"
ccVersion: "2.1.329"
variables:
  - "SIGN_IN_REFUSAL_EFFECT_NOTE"
  - "HAS_NO_FORCED_LOGIN_ORGANIZATION"
-->
This computer's settings require a sign-in to Anthropic that this app cannot use, ${SIGN_IN_REFUSAL_EFFECT_NOTE}. Ask your administrator about that setting (enforceAnthropicSignIn). To use Claude Code in a terminal on this computer instead, run `claude auth login` there. Choose the account or organization that has your Claude subscription.${HAS_NO_FORCED_LOGIN_ORGANIZATION?"":" Or, if your company reaches Claude through its own cloud account or server, choose the organization that your administrators manage in Anthropic's Enterprise Admin Console."}
