<!--
name: "Data: Organization provider sign-in changed request refusal"
description: "Refuses a request after the session stops using its organization sign-in and explains how to sign in again or restart"
ccVersion: "2.1.329"
-->
Claude Code did not send this request. This session sends its requests to the API provider that came with an organization sign-in, but the session no longer runs under that sign-in. Usually, this is because you signed out or signed in to another account, in this window or in another window. To continue, run /login and choose the organization that your administrators manage in Anthropic's Enterprise Admin Console. If Claude Code still does not send requests, exit and run `claude`. A new session uses the account that you are signed in to now.
