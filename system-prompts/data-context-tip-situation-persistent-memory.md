<!--
name: 'Data: Context tip situation — persistent memory'
description: Situation text for detecting when the user is restating persistent project context and should be shown the memory context tip
ccVersion: 2.1.191
-->
User restates a fact or preference about their project or setup that they have told Claude before — "as I mentioned", "like I said", "remember I use X", "I keep telling you" — or explicitly asks Claude to remember something for future sessions. They are trying to establish persistent context via conversation. IMPORTANT: Do NOT match tone/verbosity preferences (that is verbose-preference), per-tool-event rules (that is hooks-automation), or wanting to resume prior-session work (that is previous-session-reference).
