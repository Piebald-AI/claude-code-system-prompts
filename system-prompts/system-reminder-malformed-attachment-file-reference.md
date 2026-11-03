<!--
name: "System Reminder: Malformed attachment file reference"
description: "Rejects an invalid attachment file reference and specifies the SHA-256 and absolute-path syntax, path restrictions and base64 fallback needed to correct it"
ccVersion: "2.1.317"
variables:
  - "ATTACHMENT_CONTENT_FIELD_NAME"
  - "ATTACHMENT_ORDINAL"
  - "NOT_SENT_TO_SERVICE_NOTE"
-->
The file reference in the ${ATTACHMENT_CONTENT_FIELD_NAME} of the ${ATTACHMENT_ORDINAL} attachment is not valid, ${NOT_SENT_TO_SERVICE_NOTE} Write it as sha256:<64 lowercase hex digits>:<absolute path>, with / between folders, also on Windows (C:/Users/...). No folder or file name in the path may be empty, be made only of dots and spaces (such as . or ..), or contain ':'. The path may not end in '/', contain backslashes, escapes like %20, or unusual characters, be over 1,024 bytes, or have more than 32 parts. Fix it, or put the file's base64 in that attachment's ${ATTACHMENT_CONTENT_FIELD_NAME}.
