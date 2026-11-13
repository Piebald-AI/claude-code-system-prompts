<!--
name: "Data: SDK initialize response managed_settings_applied field"
description: "Describes the internal initialize response field reporting whether the request's managedSettings are the ones the process stored at launch, what true does and does not prove, when it is absent, and that a host must hold its prompt until it is true"
ccVersion: "2.1.323"
-->
@internal Whether the `managedSettings` in this initialize are the ones the process stored at launch under --managed-settings-in-initialize, so a re-sent initialize with the same settings also reads true. True does not say that they are in force: state.parentSettingsIncluded of list_permission_rules says whether they count beside the machine's own managed settings. The request's `managedSettings` field sets nothing after launch. Absent when the request carried none, on CLIs that predate this field (those never read `managedSettings`), and from responders that do not store them. A host that sent them must send no prompt until this is true; the TypeScript SDK holds the prompt, and ends the session on any other answer.
