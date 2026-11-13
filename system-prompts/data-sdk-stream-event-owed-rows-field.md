<!--
name: "Data: SDK stream event owed_rows field"
description: "Documents the stream-event field listing UUIDs of Project document-read and changed Project-context rows written before the first model request, present alongside user_message_uuid"
ccVersion: "2.1.324"
-->
@internal The uuids of the rows that this turn wrote ahead of its first model request and that change what Claude holds of the chat's claude.ai Project. A read of the transcript at the turn's start can lack them. A `project_doc_reads` row records Claude Code's own read of the Project's documents. It is listed when it names a document, and the conversation already held a reply or an earlier such row. A `session_context` row is listed when it replaces an earlier one and its `attachedProject` differs from that row's. Empty when the turn wrote no row to list. The rows may not have reached the session server yet. Present exactly when user_message_uuid is, on the same stream events; absent from older producers, and then it states nothing.
