<!--
name: "Tool Description: ReadFile compact"
description: "Compact file-read tool description served to newer models — absolute path, default line cap, and image/PDF/notebook handling"
ccVersion: "2.1.178"
variables:
  - "MAX_LINES_CONSTANT"
  - "CONDITIONAL_LENGTH_NOTE"
  - "CAT_DASH_N_NOTE"
  - "READ_FULL_FILE_NOTE"
  - "CAN_READ_PDF_FILES_FN"
  - "ADDITIONAL_READ_NOTE"
-->
Reads a file from the local filesystem.

- `file_path` must be an absolute path.
- Reads up to ${MAX_LINES_CONSTANT} lines by default${CONDITIONAL_LENGTH_NOTE}.
${CAT_DASH_N_NOTE}
${READ_FULL_FILE_NOTE}
- Reads images (PNG, JPG, …) and presents them visually.${CAN_READ_PDF_FILES_FN()?' Reads PDFs via the `pages` parameter (e.g. "1-5", max 20 pages/request; required for PDFs over 10 pages).':""} Reads Jupyter notebooks (.ipynb) as cells with outputs.
- Reading a directory, a missing file, or an empty file returns an error or system reminder rather than content.${ADDITIONAL_READ_NOTE}
