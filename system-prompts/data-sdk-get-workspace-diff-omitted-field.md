<!--
name: "Data: SDK get_workspace_diff omitted field"
description: "Describes the workspace diff field counting changed files that have no per-file stats row, whether the count is whole or a floor, the causes of omitted rows, and which files are never counted"
ccVersion: "2.1.323"
-->
Changed files with no perFileStats row. Use it in place of stats.filesCount minus the number of rows, which misses new files that got no row and can be wrong when source.kind is 'branch'. exact true: files is the whole count (0: every changed file has a row). exact false: files is a floor; show 'at least', or 'there may be more' for 0. Causes include a failed listing, more than 500 changed files or untracked paths, and 50 uncommitted changes to tracked files filling the rows (untracked files are then not looked for). Never counted: files git ignores, untracked files older than the session or outside the session's folder, changes inside submodules. files is 0 whenever stats.filesCount is 0. Absent from Claude Code versions that predate it: subtract instead.
