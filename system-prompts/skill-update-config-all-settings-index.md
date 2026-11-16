<!--
name: "Skill: Update config all settings index"
description: "Appends an index of every top-level settings.json key with the start of its description, and tells Claude to read the key's schema file from the skill's directory before writing an unfamiliar key"
ccVersion: "2.1.326"
variables:
  - "OBJECT_GLOBAL"
  - "SETTINGS_SCHEMA"
  - "SETTING_KEY"
  - "SETTING_SCHEMA"
  - "SETTING_DESCRIPTION"
  - "TRUNCATE_TEXT_FN"
  - "MAX_SETTING_DESCRIPTION_LENGTH"
-->


## All Settings

Every top-level key of settings.json, with the start of its description. Before you write a key whose exact shape is not shown above, Read `schema/<key>.json` in this skill's base directory (for example `schema/sandbox.json`): it holds the key's full description and JSON schema, nested keys included. Read only the keys you need. The directory does not survive a resume: if a Read fails, load this skill again for a new one.

${OBJECT_GLOBAL.entries(SETTINGS_SCHEMA.properties??{}).map(([SETTING_KEY,SETTING_SCHEMA])=>{let SETTING_DESCRIPTION=typeof SETTING_SCHEMA==="object"?SETTING_SCHEMA.description??OBJECT_GLOBAL.keys(SETTING_SCHEMA.properties??{}).join(", "):"";return`- ${SETTING_KEY}: ${TRUNCATE_TEXT_FN(SETTING_DESCRIPTION,MAX_SETTING_DESCRIPTION_LENGTH)}`}).join(`
`)}
