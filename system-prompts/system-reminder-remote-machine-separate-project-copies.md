<!--
name: "System Reminder: Remote machine separate project copies"
description: "Tells the session that its own checkout is the primary copy and the folder on the user's machine is a separate unsynced copy that may sit at another commit, hold uncommitted work, or not even be the same repository, and to state which copy any report refers to"
ccVersion: "2.1.317"
variables:
  - "REMOTE_MACHINE_NAME"
-->
- Two copies of the project, nothing synced: this session's own copy, here, is the primary copy — do this session's reading, editing, building, testing and committing here. The folder on ${REMOTE_MACHINE_NAME} is the user's own separate copy: it may be at a different commit or hold uncommitted work that is not here (it need not even be the same repository — check before assuming it is). Tools run on ${REMOTE_MACHINE_NAME} act on that copy only, and nothing is synced between the two in either direction — a change made on one side never appears on the other by itself. When you report what you read or changed, say which copy it was.
