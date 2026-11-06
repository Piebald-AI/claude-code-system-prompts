<!--
name: "System Reminder: Artifact database batch not-found refusal"
description: "Explains that an atomic database batch wrote nothing after a missing-document or access refusal and directs rereading expected documents, creating with set, and dropping inapplicable or forbidden entries"
ccVersion: "2.1.319"
variables:
  - "MAP_ARTIFACT_DB_ERROR_CODE_FN"
  - "ARTIFACT_DB_ERROR_CODE"
-->
db batch write failed (${MAP_ARTIFACT_DB_ERROR_CODE_FN(ARTIFACT_DB_ERROR_CODE)}): the artifact's database refused one of the writes: most often it updates a document that does not exist (update needs an existing one), deletes from a database that has never been written to (nothing to delete), or the database's access rules or your access level do not let you write its path; the batch is atomic, so nothing was written. Read back any document you expected to exist before re-creating it; create documents that should exist with set, and drop the entries that have nothing to do or that you may not write
