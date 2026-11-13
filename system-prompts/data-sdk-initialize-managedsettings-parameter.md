<!--
name: "Data: SDK initialize managedSettings parameter"
description: "Describes the internal initialize request field carrying the launching host's managed settings, which launch flags make the CLI read and apply it, the exit on failure, and the cases where the field sets nothing"
ccVersion: "2.1.323"
-->
@internal The managed settings of the host that starts Claude Code, in the same shape as the SDK `managedSettings` option, so that the launch command line does not grow with them. Read only by a CLI launched with --await-initialize and --managed-settings-in-initialize. It applies them as it applies --managed-settings, before it reads any settings, and exits with code 1 when it cannot; startup_failure_reason then says why, where the host set CLAUDE_CODE_STARTUP_FAILURE_RESULTS. Without those flags, on a repeated initialize, or over a remote session transport the field sets nothing; managed_settings_applied in the response reports whether these settings are the ones stored at launch.
