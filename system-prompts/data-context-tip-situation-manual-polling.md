<!--
name: 'Data: Context tip situation — manual polling'
description: Situation text for detecting when the user is manually polling status and should be shown the /loop context tip
ccVersion: 2.1.191
-->
User has asked Claude to check the same status multiple times across recent turns — "is the deploy done?", "check CI again", "any update on the build?", "check once more". They are manually polling. Also matches when the user says "keep checking until X" or "check every few minutes" and Claude ran the check just once — Claude cannot poll on its own without /loop. IMPORTANT: Do NOT match a single status check, or checks Claude runs as part of a larger task it is driving (e.g., running tests while implementing a feature).
