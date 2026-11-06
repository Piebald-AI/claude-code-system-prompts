<!--
name: "System Reminder: Artifact database not-found write refusal"
description: "Explains a not-found refusal of update or str_replace, requires rereading a document previously seen, and permits set only when the document should exist instead of repeating the refused write"
ccVersion: "2.1.319"
variables:
  - "ARTIFACT_DB_FAILURE_PREFIX"
  - "ARTIFACT_DB_WRITE_OPERATION"
-->
${ARTIFACT_DB_FAILURE_PREFIX}: no such artifact, collection, or document — the artifact's database refused this ${ARTIFACT_DB_WRITE_OPERATION}. Most often there is no document at its path; otherwise the database's access rules or your access level do not let you write it. This write was not applied. ${ARTIFACT_DB_WRITE_OPERATION} only changes an existing document. If you read this document earlier and it was there, read it again before anything else rather than re-creating it. Otherwise, if it should exist, create it with set (if set is refused the same way, you may not write there); if not, stop — resending this ${ARTIFACT_DB_WRITE_OPERATION} will not succeed
