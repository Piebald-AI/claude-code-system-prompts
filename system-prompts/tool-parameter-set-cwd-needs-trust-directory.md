<!--
name: "Tool Parameter: set_cwd needs_trust directory"
description: "Describes the canonical target directory returned by a set_cwd needs_trust response, which the SDK host must show in a trust dialog and echo back verbatim on accept"
ccVersion: "2.1.323"
-->
Canonical target directory. Nothing changed; show a trust dialog for exactly this string and, on accept, re-send with trust_accepted: true and trusted_directory echoing it verbatim. Safe to render verbatim in the dialog, by construction: every character is a visible, space-distinguishable glyph. Targets whose canonical path, or the canonical root of the repository they belong to, contains control (Cc), format (Cf), default-ignorable, line/paragraph-separator (Zl/Zp), non-ASCII-space Zs, braille-blank or lone-surrogate code points are rejected (reason: unsafe_path) before this arm can carry them.
