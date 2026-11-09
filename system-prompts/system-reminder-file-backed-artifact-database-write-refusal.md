<!--
name: "System Reminder: File-backed artifact database write refusal"
description: "Redirects artifact database writes to project/ files and requires carrying over all earlier content before the first file publication"
ccVersion: "2.1.321"
-->
This artifact keeps its content in files under project/, not in its database, so do not retry the write. read_db still works, but its rows are not what the artifact shows now. Publish the content as files under project/ instead. If project/ has no index file yet (project/deck.json, project/canvas.json or project/design-system.json) and the database already holds earlier content, read ALL of that content first and include it in the files you publish; never publish only part of it or only new content onto such an artifact. If you cannot carry all of it over, publish nothing and tell the user their earlier content is still in the artifact's database
