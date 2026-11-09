<!--
name: "Skill: Claude API deprecated or retired models notice"
description: "Section appended to the Claude API skill listing deprecated or retired Claude models found in the project with their status, dates and current replacements, and telling Claude to mention it once briefly without changing existing model IDs unprompted"
ccVersion: "2.1.321"
variables:
  - "RETIRING_MODELS"
  - "RETIRING_MODEL_ENTRY"
  - "DETECTED_MODEL_FAMILIES"
  - "FORMATTED_RETIREMENT_DATE"
  - "RETIREMENT_DATE_FORMATTER"
  - "DATE_CLASS"
  - "MODEL_ID"
  - "TODAY_ISO_DATE"
  - "CURRENT_MODEL_FAMILY_LABELS"
  - "SKILL_MODEL_VARS"
  - "SHOULD_SUGGEST_MIGRATE_COMMAND"
-->
## Deprecated or Retired Models in This Project

Files in this project name these Claude API models, which are deprecated or retired:

${RETIRING_MODELS.filter((RETIRING_MODEL_ENTRY)=>DETECTED_MODEL_FAMILIES.includes(RETIRING_MODEL_ENTRY.family)).map((RETIRING_MODEL_ENTRY)=>{let FORMATTED_RETIREMENT_DATE=RETIREMENT_DATE_FORMATTER.format(new DATE_CLASS(`${RETIRING_MODEL_ENTRY.date}T00:00:00Z`));return`- ${RETIRING_MODEL_ENTRY.name} (${RETIRING_MODEL_ENTRY.ids.map((MODEL_ID)=>``${MODEL_ID}``).join(", ")}): ${RETIRING_MODEL_ENTRY.status==="deprecated"&&TODAY_ISO_DATE<=RETIRING_MODEL_ENTRY.date?`deprecated; it retires on ${FORMATTED_RETIREMENT_DATE}`:`retired on ${FORMATTED_RETIREMENT_DATE}, so Claude API requests to it fail`}. Current ${CURRENT_MODEL_FAMILY_LABELS[RETIRING_MODEL_ENTRY.current]} model: `${SKILL_MODEL_VARS[RETIRING_MODEL_ENTRY.current]}`.`}).join(`
`)}

The first time you read, write, or run code that calls one of these models, tell the user once, briefly, in one short note that covers all of them: each model's status and date${SHOULD_SUGGEST_MIGRATE_COMMAND?", the current model, and that `/claude-api migrate` can make the switch":" and the current model"}. Mentions only in docs, changelogs, tests, or third-party code are not worth raising. Leave model IDs already in the user's code as they are unless the user asks you to change them or to fix errors they cause; new code you write uses current models. These dates are the Claude API's; Amazon Bedrock and Vertex AI set their own schedules.
