<!--
name: 'Data: Thin-client diff dialog schema'
description: Internal data description for workspace git diff payloads used by the thin-client diff dialog
ccVersion: 2.1.198
-->
@internal Workspace git diff for the thin-client /diff dialog. diff is null when the workspace is not a git repo or is in a transient git state (merge/rebase/cherry-pick). Paths in skippedLarge carry no hunks entry at all — membership alone marks them as too large. An entirely empty hunks array with non-empty perFileStats is not by itself a failure signal: it is the normal shape when all changes are untracked (stats only — git diff emits no hunks for untracked files) or every file was withheld, and can also occur when the hunks fetch transiently failed and only stats are available.
