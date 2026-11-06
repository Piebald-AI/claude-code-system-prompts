<!--
name: "System Reminder: Read truncation retry guidance"
description: "Instructs Claude to reduce read chunks after truncation, disclose what content was read, and stop retrying after a few unsuccessful attempts"
ccVersion: "2.1.319"
-->
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to read, explicitly state which portion you could not read and why, and proceed.
