<!--
name: "Data: SDK set_message_waiting control request"
description: "Internal SDK control request where the host says it is holding a person's message until the running turn ends, so a Claude Desktop Code turn ends without waiting for its post-turn summary model call"
ccVersion: "2.1.326"
-->
@internal Says that the host holds a person's message until the running turn's result (true), or no longer does (false). While true, in a Claude Desktop Code session (elsewhere it changes nothing), the turn's end does not wait for the model call behind its post_turn_summary, so the result comes sooner and the summary is written without the model. The turn's end, or the next user message that the host sends, sets it back to false. Acknowledged with an empty success; an older CLI answers an unknown-subtype error.
