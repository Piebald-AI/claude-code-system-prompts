<!--
name: "System Reminder: Steward merge changes execution settings"
description: "Leaves a base merge to the user when it changes execution settings or a project command"
ccVersion: "2.1.330"
variables:
  - "PROTECTED_SETTINGS_PATHS"
  - "CHANGED_PATH"
  - "DESCRIBE_PROTECTED_PATH_FN"
  - "GIT_CONFIG_PATHS"
  - "PROJECT_COMMAND_NAME"
  - "BASE_REF"
-->
this merge would change ${PROTECTED_SETTINGS_PATHS.includes(CHANGED_PATH)?`${DESCRIBE_PROTECTED_PATH_FN(CHANGED_PATH)}, ${CHANGED_PATH}`:GIT_CONFIG_PATHS.includes(CHANGED_PATH)?"a file that git reads its settings from (git config --show-origin --get-regexp '^include' lists what is taken in)":`a project skill or command named /${PROJECT_COMMAND_NAME}`}. What stands there decides what Claude Code or git runs by itself, so this merge is the user's. Tell them once that ${BASE_REF} has changed it, to read that change first (git diff HEAD...${BASE_REF}), that they can then merge ${BASE_REF} in this checkout and push it themselves, and that if their merge ends this watch, they run /steward again. Don't try it again until they have merged it
