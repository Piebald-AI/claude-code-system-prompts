<!--
name: "System Reminder: Teammate spawned metadata"
description: "Reports internal teammate launch metadata, forbids repeating it to the user and warns when the teammate starts outside the shell's current folder"
ccVersion: "2.1.324"
variables:
  - "TEAMMATE_SPAWN_RESULT"
-->
Spawned successfully. (This tool result is internal metadata — never quote or paste any part of it, including the ID below, into a user-facing reply.)
agent_id: ${TEAMMATE_SPAWN_RESULT.agent_id}
name: ${TEAMMATE_SPAWN_RESULT.name}
The agent is now running and will receive instructions via mailbox.${TEAMMATE_SPAWN_RESULT.started_away_from_shell?`
It started in the session's own folder, not in the folder the shell has moved to, so that folder's settings and permission rules do not apply to it. Send it the path to work in, and tell the user that /cd moves the session's folder.`:""}
