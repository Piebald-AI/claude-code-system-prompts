<!--
name: "Data: Sandbox Windows backend setting"
description: "Describes Windows sandbox backend selection, settings priority and the conditions that refuse sandboxed commands"
ccVersion: "2.1.329"
variables:
  - "PROJECT_SETTINGS_DESCRIPTION"
-->
Windows only: how sandboxed commands are confined. There is no default: until it is set, sandboxed commands are refused. "sandboxuser" runs them as the dedicated sandbox account that the sandbox set-up creates. "mxc" runs them in a Microsoft eXecution Container (BaseContainer) through the MXC SDK, with no install step; experimental. Managed settings decide over --settings, and --settings over user settings. On "mxc" only the PowerShell tool is enabled and Bash commands are refused (MXC cannot run Git Bash yet); network.allowLocalBinding does not apply, and sandboxed commands are refused while network.tlsTerminate is set, or while managed settings lock reads (filesystem.allowManagedReadPathsOnly) without picking "mxc" themselves. Read from user, managed/policy or --settings settings only; a value in ${PROJECT_SETTINGS_DESCRIPTION} is ignored.
