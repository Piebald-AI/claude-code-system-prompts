<!--
name: "Data: SDK interrupt spare_background_tasks field"
description: "Documents the per-request interrupt flag that ends the current turn while leaving background agents and workflows running, with observer and server exceptions"
ccVersion: "2.1.321"
-->
@internal True: this Stop ends the turn and leaves running background agents and workflows alone, as a Stop does for a client that declared perTaskStopAffordance. A running observer still stops. Written by a client that has its own stop for each task, for a person's Stop that should end only the turn. Holds for this request alone, whatever a client declared at initialize. A CLI that does not read it treats the request as it treats any other, and a claude-code-server tenant ends those tasks whatever this says.
