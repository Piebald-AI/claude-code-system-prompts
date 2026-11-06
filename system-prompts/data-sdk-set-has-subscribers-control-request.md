<!--
name: "Data: SDK set_has_subscribers control request"
description: "Documents the set_has_subscribers control request that adjusts stream-json output batching when nobody is watching without dropping events"
ccVersion: "2.1.319"
-->
Tells the CLI whether anybody is watching the output that the host reads from stream-json stdout and passes on. It matters only in a CLI started with CLAUDE_CODE_STREAM_EVENT_HOLD_MS, which holds most content_block_delta and thinking_tokens lines on stdout to join them, and with CLAUDE_CODE_STREAM_EVENT_NO_SUBSCRIBER_HOLD_MS: after false, each new wait of that hold lasts the second variable's time, if longer; after true or null, the first variable's time again. No line is dropped. The reply is an empty success, also where nothing changes, and like any other line it comes after the lines held so far, so each request ends the wait that is running: send one only when the answer changes, not after each message from your server. A new CLI process starts as watched, so send the answer again to each new process. An older CLI answers with the unsupported-subtype error, and a CLI that drives a cloud-hosted session refuses the request.
