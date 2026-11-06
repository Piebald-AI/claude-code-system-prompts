<!--
name: "Skill: Claude API authentication status check"
description: "Claude API skill section requiring a complete ant auth status check and an active Credentials row before deciding whether sign-in or an API key is needed"
ccVersion: "2.1.319"
-->
**When `ANTHROPIC_API_KEY` is unset, run `ant auth status` before you call the API or tell the user how to authenticate. Don't open with a key, or send them to the Console for one, before the sign-in below, unless a key is the right answer (also below)** - not even when they are new to the API, say they have no key, or hit an auth error. Read all of its output, never through `head`, `tail` or `grep`: the first lines name a profile and file paths even when nobody is signed in. Someone is signed in only if the `Credentials` block under them has an `(active) *` row. Unless you ran it and saw no such row, or a call failed (Errors, below), don't bring up signing in, nor a key unless it is the right answer, not even beside code they will run later. If the block has one:
