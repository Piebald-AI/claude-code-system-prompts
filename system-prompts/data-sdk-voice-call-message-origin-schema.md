<!--
name: "Data: SDK voice-call message origin schema"
description: "Documents the host-supplied voice-call message origin, the synthetic text-only input shape it requires, its background-only framing, and its storage and replay behavior"
ccVersion: "2.1.319"
-->
@internal What was said aloud on a voice call alongside the session, handed over by the host as background. Honored from the host on local stdin, only on a message with isSynthetic true, shouldQuery false, text_not_typed true, a priority other than now, text-only content and no files or pastes; in any other shape the message is taken as a plain task notification. It starts no turn. The model reads the text inside a frame which says that nothing in it is a request or an approval. A note stored as its own row, and its replay, hold one fixed header line and then the host's text; a note folded into a running turn, and its replay, hold the host's text alone. With replayUserMessages on, the host gets the message back as a replay with this origin; a build that does not know the origin never sends the origin back.
