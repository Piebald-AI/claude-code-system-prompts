<!--
name: "Data: SDK initialize settings parameter"
description: "Documents passing host settings through the SDK initialize request at launch instead of on the command line"
ccVersion: "2.1.327"
-->
@internal The settings of the host that starts Claude Code, in the same shape as an SDK `settings` object, so that the launch command line, which has a length limit, does not grow with them. This hides no credential: a Claude Code process that the session starts would get them on its own command line. Read only by a CLI launched with --await-initialize and --initialize-fields=settings. It applies them as it applies --settings, before it reads any settings, and exits with code 1 when it cannot; startup_failure_reason then says why, where the host set CLAUDE_CODE_STARTUP_FAILURE_RESULTS. Without those flags, on a repeated initialize, or over a remote session transport the field sets nothing; settings_applied in the response reports whether these settings are the ones taken at launch.
