<!--
name: "Data: SDK UI attach draws field"
description: "Documents the per-client optional UI component list for Backdrop rendering, including repeated attachments, unknown names, limits and empty-list behavior"
ccVersion: "2.1.317"
-->
@internal The components this client draws beyond those every client of its surface draws: `Backdrop` (the session's backdrop, full window behind the conversation). Held per client like `answers`: a later `ui_attach` under the same id that names it replaces it, and it leaves with the client. A name this version does not know, or one said twice, is ignored, so a newer client keeps its attach; a list of more than 16 names, or a name of more than 64 characters, is refused with the attach. Absent: a client still attached, or one put back, keeps what it said, and a first attach draws none. Empty, or nothing known in it: none, and `$.ui.backdrop` answers that nothing draws it.
