<!--
name: "System Reminder: Artifact database batch blocked for repeated refused writes"
description: "Explains that a repeated refused operation caused an atomic database batch to be rejected and requires changing or dropping that entry rather than resending the batch unchanged"
ccVersion: "2.1.319"
variables:
  - "MAP_ARTIFACT_DB_ERROR_CODE_FN"
  - "ARTIFACT_DB_ERROR_CODE"
-->
db batch write failed (${MAP_ARTIFACT_DB_ERROR_CODE_FN(ARTIFACT_DB_ERROR_CODE)}): one of the writes repeats an operation on a path the server refused earlier (a missing document, a path you may not write, or an invalid argument), and after repeated refused writes to this artifact it is briefly turning such repeats away, whatever data they carry; the batch is atomic, so nothing was written. Do not resend the batch as it is: drop or change the entry that was refused before (the server does not say which; for example, use set to create a document that should exist), or stop
