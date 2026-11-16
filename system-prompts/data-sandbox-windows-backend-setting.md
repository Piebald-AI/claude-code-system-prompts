<!--
name: "Data: Sandbox Windows backend setting"
description: "Describes the sandbox.windows.backend setting: running sandboxed commands as the sandbox account or in a Microsoft eXecution Container, when Claude Code falls back from MXC, and that project settings can't set it"
ccVersion: "2.1.326"
variables:
  - "PROJECT_SETTINGS_DESCRIPTION"
-->
Windows only: how sandboxed commands are confined. "sandboxuser" (default) runs them as the dedicated sandbox account that the sandbox set-up creates. "mxc" runs them in a Microsoft eXecution Container (BaseContainer) through the MXC SDK, with no install step; experimental. Claude Code ignores "mxc" and uses the sandbox account, with a note in /sandbox, when this build lacks the MXC SDK, when a higher settings tier or another managed source sets network.tlsTerminate, or when an administrator requires the sandbox or locks reads (filesystem.allowManagedReadPathsOnly) unless managed settings picked "mxc" and no other managed source sets network.allowManagedDomainsOnly. On "mxc" only the PowerShell tool is enabled and Bash commands are refused (MXC cannot run Git Bash yet); network.tlsTerminate and network.allowLocalBinding do not apply. Read from user, managed/policy or --settings settings only; a value in ${PROJECT_SETTINGS_DESCRIPTION} is ignored.
