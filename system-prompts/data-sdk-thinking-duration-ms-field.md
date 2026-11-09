<!--
name: "Data: SDK thinking_duration_ms field"
description: "Schema description for the display-only thinking_duration_ms wrapper field giving how long a streamed thinking block took, excluding the wait for the first token, and when it is absent or not replayed to the model"
ccVersion: "2.1.321"
-->
@internal How long the thinking block in this frame took to stream, in whole milliseconds (at least 1): from its content_block_start to its content_block_stop, or to the interrupt that cut it, so the wait for the response's first token is not counted. For display only. Sent only on a frame whose one content block is a thinking block that was streamed. Older CLI versions never send it, and a CLI that rebuilt its history from SDK frames does not send it when it replays that history, so be ready to show the block without a duration. Wrapper-level sibling — never inside `message.content` — so it is not replayed to the model.
