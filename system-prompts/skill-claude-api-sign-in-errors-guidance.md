<!--
name: "Skill: Claude API sign-in errors guidance"
description: "Claude API skill bullet explaining that a 401 or invalid_grant on a previously working sign-in means signing in again, and that a low credit balance needs credits bought or claimed for that organization rather than a new sign-in"
ccVersion: "2.1.323"
-->
- **Errors:** a 401 or `invalid_grant` on a sign-in that used to work means it has run out: sign in again the same way. `credit balance is too low` means that organization has no credits the call can use. They buy some under Billing in the Console. Max, Ultra and Team plans include monthly API credits, claimed on claude.ai (`shared/api-sign-in.md`). If they claimed those for another organization, they sign in to it under a new profile (`! ant auth login --profile <name>`; a plain login keeps the organization). Otherwise signing in again, or a key for that organization, won't help.
