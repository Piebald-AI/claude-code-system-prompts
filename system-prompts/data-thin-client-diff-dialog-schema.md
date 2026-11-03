<!--
name: "Data: Thin-client diff dialog schema"
description: "Internal data description for workspace git diff payloads used by the thin-client diff dialog"
ccVersion: "2.1.318"
-->
@internal Workspace diff for the thin-client /diff dialog. diff is null when no diff could be made; noDiffReason says why. Paths in skippedLarge carry no hunks entry at all — membership alone marks them as too large. An entirely empty hunks array with non-empty perFileStats is not by itself a failure signal: it is the normal shape when all changes are untracked (stats only: untracked files never carry hunks) or every file was withheld, and can also occur when the hunks fetch transiently failed and only stats are available.
