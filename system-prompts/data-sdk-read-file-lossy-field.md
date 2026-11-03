<!--
name: "Data: SDK read_file lossy field"
description: "Documents whether UTF-8 file-read output replaced invalid bytes, distinguishes literal replacement characters from lossy decoding, and explains base64 and older-client absence"
ccVersion: "2.1.317"
-->
Present on every utf-8 answer. True when the bytes read were not all valid UTF-8, so `contents` has U+FFFD where bytes were replaced and is not the file's own text: a binary file, text in another encoding, or a read cut inside a character when `truncated` is set. False when `contents` is exactly the bytes read, decoded, even if the file itself contains U+FFFD. Absent on a base64 answer, which is exact, and from an older CLI or tool container: a client that sees neither this nor `encoding: 'base64'` cannot tell whether `contents` is exact.
