<!--
name: "Tool Description: Project local_file read-only workflow"
description: "Explains how to read and search a project document local_file, copy it into a new working file for edits, and save changes through project_write"
ccVersion: "2.1.319"
variables:
  - "READ_TOOL_NAME"
  - "CONTENT_SEARCH_TOOL_OR_COMMAND"
-->
local_file is for reading only: read the parts you need with ${READ_TOOL_NAME}'s offset and limit, or search it with ${CONTENT_SEARCH_TOOL_OR_COMMAND}. Edits to it never reach the project, and project_write rejects it as local_path. To change the document or make a file from it, run `cat /path/of/local_file > new-name` in the working directory, where new-name is a name that no file there has, and work on that file. To save a change, call project_write with the document's path and that file as local_path. If the document is an upload such as a PDF, that saves a new text document and leaves the upload as it is.
