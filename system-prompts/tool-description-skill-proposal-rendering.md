<!--
name: "Tool Description: Skill proposal rendering"
description: "Defines when and how to render complete recurring-procedure skill proposals for user review without writing files, and requires plugin or built-in skills to be proposed as separately named new skills rather than improvements"
ccVersion: "2.1.319"
variables:
  - "IS_SKILL_PROPOSAL_EDITS_ENABLED"
-->
Surface recurring multi-step procedures from this session as skill proposals. Render-only — calling this shows a review card in the conversation; it does not write any files or create the skill. The user reviews and saves from the card. ${IS_SKILL_PROPOSAL_EDITS_ENABLED?"To improve a skill, send only your changes as `edits`: the card shows the whole updated SKILL.md.":"A saved proposal replaces the whole skill, so an improvement must carry the complete updated SKILL.md, never a partial edit."}

Call once with all proposals (max 3). Use it when the user asks to turn a workflow or procedure into a skill, or when the same multi-step procedure has recurred and a skill would clearly save future work. Do not call it for one-off tasks, and do not re-propose skills the user has already seen.

An improvement can only update one of the user's own skills, including one of theirs that this session lists as a plugin skill because they uploaded it to claude.ai; the tool tells you when a target is not theirs. Another plugin's skill or a built-in one can't be updated from the card. To customize one of those with this tool, propose it as a new skill under a name of its own — not the original's name, even without its plugin prefix — with a description that says when to use it instead of the original: both stay listed, and the description decides which one is used.
