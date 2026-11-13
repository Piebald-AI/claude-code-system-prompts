<!--
name: "Data: Sandbox project false value ignored under higher-priority policy"
description: "Explains when project-level false values for sandbox.enabled and sandbox.failIfUnavailable are ignored because a higher-priority source sets true"
ccVersion: "2.1.324"
variables:
  - "HIGHER_PRIORITY_SANDBOX_POLICY_CONDITIONS"
  - "PROJECT_SETTINGS_SOURCE_DESCRIPTION"
-->
${HIGHER_PRIORITY_SANDBOX_POLICY_CONDITIONS}, and managed, --settings or user settings set true, false from ${PROJECT_SETTINGS_SOURCE_DESCRIPTION} is ignored (true there still applies).
