<!--
name: "Data: SDK user message ultrathink_typed field"
description: "Documents the sender's claim that ultrathink was typed without pasted or suggested text, the capability required to send it, and the additional checks before raising turn effort"
ccVersion: "2.1.317"
-->
@internal The sender's statement that the person typed `ultrathink` in this prompt and was shown the word colored before sending, and that nothing in the prompt arrived whole as far as the sender saw: no paste, no share, no prompt it suggested. Send it only as `true`, and only while the session's newest system/init carried `ultrathink_typed_raises: true`; leave it out otherwise. The turn then runs at xhigh effort if the CLI also finds the word in the text, the text holds no paste block, the frame lists no paste in `inline_pastes` or `pasted_content`, its `client_platform`, when present, is a person's keyboard or a thin client's, it bears no other mark of untyped text, and the session takes the sender for a person. It is the sender's claim, not proof.
