<!--
name: "Tool Parameter: set_cwd rejection reasons unsafe_path and remote_origin"
description: "Explains two set_cwd rejection reasons: unsafe_path for a target or repository root whose path contains characters that do not render as visible glyphs, and remote_origin for a request that reached a Remote Control session from a remote client"
ccVersion: "2.1.323"
-->
unsafe_path: the target's canonical path, or the canonical root of the repository it belongs to (the key a trust grant would be written under), contains characters that do not render as visible, space-distinguishable glyphs — control (Cc), format (Cf), default-ignorable, line/paragraph-separator (Zl/Zp), non-ASCII-space Zs, braille-blank or lone-surrogate code points; rejected fail-closed before the trust round-trip, and the offending path is never echoed back. A root already trusted from a terminal session is not re-judged. remote_origin: the request reached a Remote Control session (claude remote-control) from a remote client rather than from the process that owns the CLI's stdin; such a session keeps the working directory it was started in, and nothing was resolved or recorded.
