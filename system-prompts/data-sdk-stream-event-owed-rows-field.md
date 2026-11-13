<!--
name: "Data: SDK stream event owed_rows field"
description: "Describes the internal stream-event field listing the uuids of project_doc_reads rows a turn wrote before its first model request that give the text of an added claude.ai Project document, including what counts as added and when it is present"
ccVersion: "2.1.323"
-->
@internal The uuids of the `project_doc_reads` rows that this turn wrote ahead of its first model request and that give the text of an added document. Such a row records Claude Code's own read of a claude.ai Project's documents. A document counts as added when no earlier row of the conversation gives a text under its name, or a later one of them tells the document of that name as removed. A row with only replaced, edited or removed documents is not listed, and neither is a row from before the conversation's first reply. Empty when the turn wrote no row to list. A consumer that read the transcript at the turn's start can tell from it whether that read lacks such a row. The rows may not have reached the session server yet. Present exactly when user_message_uuid is, on the same stream events; absent from older producers, and then it states nothing.
