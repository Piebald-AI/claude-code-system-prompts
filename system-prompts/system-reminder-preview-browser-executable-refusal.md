<!--
name: "System Reminder: Preview browser executable refusal"
description: "Explains why preview rejects browser executables the session could modify and how to select a browser outside those locations"
ccVersion: "2.1.327"
variables:
  - "CHROME_INSTALL_COMMAND"
  - "CAN_RUN_CHROME_INSTALL"
  - "REFUSED_BROWSER_PATHS"
-->
preview will not launch a browser this session's commands could have planted or altered: each one it found sits somewhere they can write without asking (a working directory, a temp dir, a sandbox write root, or a path a Write or Edit allow rule covers) — ${CHROME_INSTALL_COMMAND===void 0?"install Chrome outside those places":CAN_RUN_CHROME_INSTALL?"install one outside those places with the command below":`install one outside those places (run via Bash, one-time, ~270 MB: ${CHROME_INSTALL_COMMAND})`}, or point BUN_CHROME_PATH at one from your shell. Refused: ${REFUSED_BROWSER_PATHS.join("; ")}${CAN_RUN_CHROME_INSTALL&&CHROME_INSTALL_COMMAND!==void 0?`
${CHROME_INSTALL_COMMAND}`:""}
