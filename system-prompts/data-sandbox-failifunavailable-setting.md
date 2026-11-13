<!--
name: "Data: Sandbox failIfUnavailable setting"
description: "Describes when sandbox.failIfUnavailable prevents startup and why hosted cloud containers instead start with a warning"
ccVersion: "2.1.324"
-->
Exit with an error at startup if sandbox.enabled is true but the sandbox cannot start (missing dependencies or unsupported platform). When false (default), a warning is shown and commands run unsandboxed. Intended for managed-settings deployments that require sandboxing as a hard gate. A Claude Code on the web, scheduled-task or Cowork cloud session (Anthropic's cloud container, which has no command sandbox) starts anyway with a warning: the container isolates it, and the sandbox.filesystem and sandbox.network rules in settings are not enforced there. 
