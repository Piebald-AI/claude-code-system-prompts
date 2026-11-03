<!--
name: "Data: SDK system init ultrathink_typed_raises field"
description: "Documents when clients may highlight typed ultrathink and assert ultrathink_typed, including effort-change invalidation and Remote Control bridge limitations"
ccVersion: "2.1.317"
-->
@internal True when a user message that carries `ultrathink_typed: true` and passes the checks listed on that field runs its turn at xhigh effort on this frame's `model`, and when the session is already at xhigh or max, where the turn stays as it is. A client colors the word and sends the statement only while this is true. After system/per_turn_effort_changed, treat this as false until the next init; a terminal session under Remote Control does not forward that event, so this can stay true after the raise has stopped. Absent means unknown: color nothing and send no statement. Sent by the stream-json (Agent SDK) host and on Remote Control bridge init frames.
