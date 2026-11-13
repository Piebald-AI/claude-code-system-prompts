<!--
name: "Data: SDK user message retracted_message_uuids field"
description: "Describes the internal output-only field on the synthetic re-ask message after an unparseable tool call, listing the uuids of the dropped response messages that a client should remove, and when it is absent"
ccVersion: "2.1.323"
-->
@internal Output only, and to be read only on a message the CLI wrote: on a session event, only where its `source` is `worker`. Only on the synthetic message that asks the model again after a response whose tool call could not be parsed: the uuids of that response's messages, which the CLI has dropped from the conversation. Remove them on receipt; an unknown uuid is a no-op. If another assistant message follows in the turn, it names them again in `supersedes`. Absent if none of the response's messages was sent, on a subagent's messages, over Remote Control, and from older CLIs.
