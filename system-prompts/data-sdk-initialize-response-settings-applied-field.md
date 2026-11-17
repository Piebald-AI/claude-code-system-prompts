<!--
name: "Data: SDK initialize response settings_applied field"
description: "Reports whether Claude Code used the host's startup settings before the SDK sends a prompt"
ccVersion: "2.1.327"
-->
@internal Whether the `settings` in this initialize are the ones the process took at launch under --initialize-fields=settings, so a re-sent initialize with the same settings also reads true. False: this Claude Code knows the field and does not confirm these settings, for example because the flag was lost on the way, the process was started with others, or they are nested too deeply to compare. Absent when the request carried none, on CLIs that predate this key, and from responders that do not take them. True does not say that every rule in them is in force: list_permission_rules does. The field sets nothing after launch. A host that sent it must send no prompt until this is true; the TypeScript SDK holds the prompt, and ends the session on any other answer.
