<!--
name: "Skill: Setup Cowork role selection"
description: "First step of the setup-cowork skill that explains Cowork, asks for the user's role, calls ShowOnboardingRolePicker, or falls back to a plain-text role list"
ccVersion: "2.1.210"
variables:
  - "COWORK_ROLE_OPTIONS"
  - "COWORK_ROLE_OPTION"
-->
## Step 1 — Role

Your initial message should frame what Cowork is: it autonomously handles tasks like reading your email, searching your docs, drafting reports, etc. Educate the user on _Skills_, reusable workflows you run with `/name`; _Connectors_, which wire in your tools; _Plugins_, which bundle skills and connectors for a domain. Two or three sentences. Hit the beats: multi-step and autonomous, uses your real tools, skills/plugins/connectors defined.

Next, ask the user for their role. Something like: "Let's get you set up — takes a few minutes. What kind of work do you do?" Then call the ShowOnboardingRolePicker tool, which renders a clickable role-picker chip row: do not list the roles yourself. The tool result is their answer — {"role": ...} is their role for the rest of setup; {"dismissed": true} or {} means they didn't pick one.

If the ShowOnboardingRolePicker tool is not available in this session, ask in plain text instead and offer these options as a short list they can reply to (they can also answer in their own words):

${COWORK_ROLE_OPTIONS.map((COWORK_ROLE_OPTION)=>`- ${COWORK_ROLE_OPTION}`).join(`
`)}

In the plain-text case, end your turn after asking. Their reply — one of the options or a free-form answer — is their role for the rest of setup.
