<!--
name: 'System Reminder: Memory file contents'
description: Contents of a memory file by path
ccVersion: 2.1.18
variables:
  - MEMORY_ITEM
  - MEMORY_TYPE_DESCRIPTION
-->
Contents of ${MEMORY_ITEM.path}${MEMORY_TYPE_DESCRIPTION}:

${MEMORY_ITEM.content}
