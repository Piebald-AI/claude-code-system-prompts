<!--
name: "Tool Description: NotebookEdit"
description: "Tool description for editing Jupyter notebook cells by replacing, inserting, or deleting a cell using cell IDs from the read tool"
ccVersion: "2.1.162"
variables:
  - "READ_TOOL_NAME"
-->
Replaces, inserts, or deletes a single cell in a Jupyter notebook (.ipynb file).

Usage:
- You must use the ${READ_TOOL_NAME} tool on the notebook in this conversation before editing — this tool will fail otherwise.
- `notebook_path` must be an absolute path.
- `cell_id` is the `id` attribute shown in the ${READ_TOOL_NAME} tool's `<cell id="...">` output. It is required for `replace` and `delete`.
- `edit_mode` defaults to `replace`. Use `insert` to add a new cell after the cell with the given `cell_id` (or at the beginning of the notebook if `cell_id` is omitted) — `cell_type` is required when inserting. Use `delete` to remove the cell.
