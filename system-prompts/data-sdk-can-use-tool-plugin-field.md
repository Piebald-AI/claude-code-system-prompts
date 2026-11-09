<!--
name: "Data: SDK can_use_tool plugin field"
description: "Identifies the engine-supplied plugin name shown for a permission request and explains missing names and safe display"
ccVersion: "2.1.321"
-->
@internal The plugin whose `$` call (`$.ui.ask`, `$.tool.call`, `$.agent.spawn`) started the run this ask belongs to, by the name it is loaded under: who the terminal's dialog says the ask is from. The engine's word, which no plugin sets. Empty when no name can be sent: on a run resumed from an agent a plugin steered, whose name was not kept, and for a name that fails the shown-name rule (docs/shown-name-rule.md), such as one with a hidden character. Show `from a plugin` for it. Absent for the model's own calls. Untrusted text; escape before display.
