<!--
name: "Data: Rewind files skippedLinks field"
description: "Describes the rewindFiles skippedLinks count, including link-safety refusal semantics and dry-run behavior"
ccVersion: "2.1.326"
-->
Count of tracked files NOT restored or deleted because a symlink, hard link, or other non-regular file was detected at the tracked path, its parent directory no longer resolves to where it pointed when the checkpoint was taken, it is behind a link in a folder that sandboxed commands can write, or its backup could not be safely read. Only populated by a real (non-dryRun) rewind — on a dryRun response the field is never set and the preview counts do not reflect link-safety refusals. Absent or 0 on a real rewind means no link-safety refusals occurred; other per-file failures (for example a missing backup file) are not counted here; they are reported in telemetry, and when every differing file fails to restore the rewind itself fails (canRewind: false).
