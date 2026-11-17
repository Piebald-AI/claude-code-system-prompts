<!--
name: "Tool Description: Gmail attachment file references"
description: "Tells Claude to attach local files by reference in Gmail draft creation and send calls, and recreate drafts when their attachments must be kept"
ccVersion: "2.1.327"
variables:
  - "FILE_REFERENCES_HEADING"
-->
${FILE_REFERENCES_HEADING} to attach a local file in Gmail's create_draft or send_message, don't type its base64, even if the tool's description or earlier calls in this conversation show base64. Set the attachment's content to a file reference, sha256:<the file's SHA-256, as 64 lowercase hex>:<its absolute path, with / between folders>, and set filename to the file's name. The app fills in the file's content when the call runs. This works only in those two Gmail tools: other connectors can't read a file reference. An update_draft call removes a draft's files, so to change a draft that has files, make a new draft with the same files. If a reference is refused, do what the refusal says.
