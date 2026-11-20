<!--
name: "Tool Description: Artifact publish edits action"
description: "Describes ordered text replacements for publishing a small artifact update and recovery when the live version changed"
ccVersion: "2.1.329"
-->
- **publish** with `edits`: Publish a new version of an artifact you own, or of one in your organization that you can edit, by replacing text in its current document: use it for a small change instead of editing the file and publishing after. The call reads the file at `file_path`, applies every edit in order, and publishes the result as one new version; if any edit cannot be applied, nothing is published. Each old_str must occur exactly once in the file as it stands when that edit is applied: include enough surrounding text to make it unique. If the version you last read or published is no longer live the call is rejected with a conflict that names the live version: read what you are changing again and retry. An artifact made from a type is edited only in one of its own data files, never its page or its type's files.
