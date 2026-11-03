<!--
name: "System Reminder: Sandbox hard-linked guarded file refusal"
description: "Refuses sandboxed commands and unsandboxed retries while a guarded file has extra hard links, identifies displayable affected locations and explains recovery without restarting"
ccVersion: "2.1.317"
variables:
  - "DISPLAYABLE_HARD_LINK_LOCATIONS"
  - "ALL_HARD_LINK_LOCATIONS"
-->
Sandbox is enabled but failed to initialize: the sandbox cannot protect one or more of the files it guards${DISPLAYABLE_HARD_LINK_LOCATIONS.length===0?"":` ${DISPLAYABLE_HARD_LINK_LOCATIONS.join(" and ")}${DISPLAYABLE_HARD_LINK_LOCATIONS.length<ALL_HARD_LINK_LOCATIONS.length?" and elsewhere":""}`}, because at least one of them has more than one hard link (another name points at the same file). Until someone removes the extra link (from a terminal outside Claude Code), commands that would run in the sandbox are refused, and so is a request to run one outside the sandbox (dangerouslyDisableSandbox): do not retry that way. No restart is needed once the link is gone. If you did not create that link, treat the file as untrusted.
