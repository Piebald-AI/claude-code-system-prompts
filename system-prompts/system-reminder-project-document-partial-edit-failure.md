<!--
name: "System Reminder: Project document partial edit failure"
description: "Explains why a search-and-replace edit failed and how to retry without losing other document changes"
ccVersion: "2.1.328"
variables:
  - "PROJECT_WRITE_REFUSAL_PREFIX"
  - "MAX_EDIT_BLOCKS"
  - "PROJECT_FULL_TEXT_WRITE_GUIDANCE"
  - "FAILED_BLOCK_SEARCH_TEXT_LABEL"
  - "EDIT_FAILURE"
-->
${PROJECT_WRITE_REFUSAL_PREFIX} ${{malformed:`edits must be 1 to ${MAX_EDIT_BLOCKS} complete SEARCH/REPLACE blocks and nothing else, each with a search text and with each marker once, on its own line. Send them again in that form. If the doc's own text has such a line, or there are more changes, ${PROJECT_FULL_TEXT_WRITE_GUIDANCE}`,too_large:`The blocks are too long for a doc of this size. Send fewer in each call, or ${PROJECT_FULL_TEXT_WRITE_GUIDANCE}`,mixed_line_ends:`This doc mixes CRLF and LF line ends, so edits cannot be matched safely. Instead, ${PROJECT_FULL_TEXT_WRITE_GUIDANCE}`,not_found:`${FAILED_BLOCK_SEARCH_TEXT_LABEL} is not in the doc. Copy it exactly from the doc, then send all the blocks again.`,not_unique:`${FAILED_BLOCK_SEARCH_TEXT_LABEL} is in the doc more than once. Add the words around it so that it is found once, then send all the blocks again.`,overlap:`${FAILED_BLOCK_SEARCH_TEXT_LABEL} overlaps that of an earlier block. Join the two blocks, then send all the blocks again.`}[EDIT_FAILURE.failure]}
