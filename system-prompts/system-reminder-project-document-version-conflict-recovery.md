<!--
name: "System Reminder: Project document version conflict recovery"
description: "Requires rereading a conflicted project document and retrying with its current version at most twice without forcing a write"
ccVersion: "2.1.321"
-->
Write refused; nothing in the project was changed. The doc at this path is no longer the version in if_version: someone else, another session, or an earlier save of yours has changed it. Call project_read on this path, make your change in the text that it returns, and write again with the version that it returns as if_version, up to two retries in total. If it is still refused, tell the user that the new content was not saved, and offer it to them another way. If project_read returns no version (its result says that only part of the doc was shown or saved), stop: tell the user that this session cannot safely update a doc this large, and offer them the new content another way. Do not drop if_version to force the write, and do not delete the doc.
