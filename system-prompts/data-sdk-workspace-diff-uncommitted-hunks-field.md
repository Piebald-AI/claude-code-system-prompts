<!--
name: "Data: SDK workspace diff uncommitted hunks field"
description: "Describes the uncommitted changes against HEAD returned with a cloud branch diff"
ccVersion: "2.1.331"
-->
Only when source.kind is 'branch', and only for a request with uncommitted_hunks in an Anthropic cloud container: how files differ from HEAD, by their row's path. It lists each tracked row whose uncommittedStatus is known and not 'none', unless the file is found to be the same at HEAD and at the merge-base, or in neither: then the row's own counts and hunks serve. hunks is empty when no line differs, and when the text is not sent: as on hunks and restricted, for a side that is too large, a link or unreadable, for lack of room or time after hunks, for some renamed or copied files, and for a removed file that the merge-base lacks. A path in skippedLarge can have hunks here. A file renamed since HEAD has its counts under its new name, and zeros under its old one. Absent from Claude Code versions that predate it.
