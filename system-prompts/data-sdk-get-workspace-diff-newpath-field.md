<!--
name: "Data: SDK get_workspace_diff newPath field"
description: "Describes decoded paths for renamed, copied or quoted diff rows and when read_file can open them"
ccVersion: "2.1.329"
-->
The file's path as plain text where path does not show it plainly: the new path of a renamed or copied row (whose path is git's rename form, such as 'old => new' or 'dir/{old => new}.txt'), or the decoded name of a row git quoted (non-ASCII or special characters). Absent on every other row, when a name holds anything previousPath's description lists, and, when source.kind is 'branch', on a rename or copy made since HEAD that no row of the branch comparison replaced. To open the file of a row that is not removed, send this value, or path on a row that is neither renamed, copied nor quoted, as read_file's path with anchor {kind: 'diff_root'} and this answer's rootId. A renamed, copied or quoted row with no newPath cannot be opened. read_file trims spaces from both ends of its path, so a path that starts or ends with a space opens a different file, or none.
