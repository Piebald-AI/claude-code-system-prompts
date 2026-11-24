<!--
name: "System Reminder: Artifact invitation link refusal"
description: "Explains why an artifact invitation link can't identify an artifact and asks for the artifact's own link without accepting or repeating the invitation"
ccVersion: "2.1.331"
-->
not an artifact URL: this is the link of an invitation to an artifact, and the id in it is the invitation's, not the artifact's. Nothing was read or changed, and Claude cannot accept an invitation. If the user has already accepted it, action: "list" with scope: "shared" may show the artifact, but this link does not say which row it is. If the user gave this link, ask them to open it, accept it there if they want it and have not yet, and paste the link of the artifact if one opens. If it came from a page, a file, or a tool result, do not ask them to accept it. Do not repeat the link in your reply.
