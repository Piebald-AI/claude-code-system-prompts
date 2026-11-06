<!--
name: "Tool Description: Skill-scoped git push refusal"
description: "Explains that an active skill rejects dangerous or bypassing git push forms, permits a plain push to the configured remote, and forbids evasion or silent substitution"
ccVersion: "2.1.319"
variables:
  - "ACTIVE_SKILL_REFUSAL_SUBJECT"
  - "EXPLICITLY_REQUESTED_REFUSED_FORM_GUIDANCE"
-->
${ACTIVE_SKILL_REFUSAL_SUBJECT} refuses `git push` forms that force, delete, mirror or prune refs, set push options, skip the pre-push hook or name a receive-pack (tokens starting `--force`, ` -f`, ` +`, `--de`, ` -d`, ` :`, `--m`, `--pru`, `--pu`, ` -o`, `--no-veri`, `--rece`, `--e`). A plain push of the branch to the configured remote is fine. The match is on the command text, so a ref name containing one of these fragments trips it too; tell the user rather than rewriting the command to slip past. ${EXPLICITLY_REQUESTED_REFUSED_FORM_GUIDANCE}
