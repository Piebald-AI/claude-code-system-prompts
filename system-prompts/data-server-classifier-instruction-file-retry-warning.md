<!--
name: "Data: Server classifier instruction file retry warning"
description: "Log message explaining why the server safety check drops the full instruction files and retries after a 400 or 413 response"
ccVersion: "2.1.327"
variables:
  - "IS_INVALID_REQUEST"
-->
[server-classifier] The API answered HTTP ${IS_INVALID_REQUEST?"400 (invalid request)":"413 (body too large)"} to a request with claude_md, the whole text of the instruction files (CLAUDE.md, rules) that the model sees only in part. ${IS_INVALID_REQUEST?"A server that does not accept claude_md answers this way, but other faults do too. Sending the request again without claude_md. For this reply, the permission check reads only the start of those files.":"Sending the request again without claude_md. Until the next turn or compaction, the permission check reads only the start of those files."}
