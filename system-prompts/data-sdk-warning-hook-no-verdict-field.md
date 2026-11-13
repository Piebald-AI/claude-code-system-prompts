<!--
name: "Data: SDK warning hook_no_verdict field"
description: "Documents structured warning details for a PreToolUse hook that gave no verdict without refusing the call, including timeout and plugin fields"
ccVersion: "2.1.324"
-->
@internal Present on the warning, tagged `hook_no_verdict`, that a PreToolUse hook gave no verdict on the call `tool_use_id` and that its failure did not refuse the call, so a host can word the notice itself instead of reading `content`. Another hook, a rule or the person may still stop that call. Sent once per hook in a session, for the first such call. `timed_out` is true for a hook that ended with no answer, usually at its timeout. `plugin_id` and `plugin_root` are there for a plugin's hook. Not sent for a hook that ran and chose a non-blocking exit, nor where the failure refused the call.
