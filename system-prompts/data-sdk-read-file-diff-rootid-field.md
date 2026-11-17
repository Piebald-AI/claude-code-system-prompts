<!--
name: "Data: SDK read_file diff rootId field"
description: "Explains how to tie a diff-root file read to the workspace diff that supplied its path"
ccVersion: "2.1.327"
-->
The `rootId` of the get_workspace_diff answer that `path` came from, sent back unchanged. If the directory the session would diff now is not the one that answer's paths are relative to, or there is none, the read is refused with `read denied: <path>` and the error_code stale_root_id: the directory has changed, or the session's process has restarted. Ask for the diff again rather than resending. Otherwise the read is served as a diff_root read without `rootId` would be. Leave it out when the answer had none: null is refused as a malformed anchor, with no error_code. A CLI that has `anchor` but predates `rootId` ignores it.
