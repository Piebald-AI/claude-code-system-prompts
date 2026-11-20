<!--
name: "Data: SDK read_file requested_path field"
description: "Describes the internal read_file reply field echoing the request's path exactly as sent, so a client can drop a reply that answers another request under the same request_id, and when the field is absent"
ccVersion: "2.1.330"
-->
@internal The request's `path`, exactly as sent. It is on every success reply whose `absPath` is what that path resolved to, and on every success reply of a session that reads through a tool container, where `absPath` is also the path as sent. If it differs from the path you sent, the reply answers another request under the same request_id: drop it and keep waiting. Compare the reply's `anchor` with your anchor's kind as well. Both can still match for another file where what the path is resolved against changes between requests (the live cwd, an as_written look-up) or isn't in the reply (which repository, for the anchor kind repo). Absent under Remote Control, whose `absPath` is itself the path as sent, from the engine's readFile, and in replies of an older CLI. It does not prove who wrote the reply.
