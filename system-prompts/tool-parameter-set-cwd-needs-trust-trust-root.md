<!--
name: "Tool Parameter: set_cwd needs_trust trust root"
description: "Describes the set_cwd needs_trust field naming the resolved git repository root when it differs from the directory, since accepting trust grants the whole repository, and that a root with unsafe characters rejects the request"
ccVersion: "2.1.323"
-->
Present when `directory` sits inside a git repository whose canonical root differs from it (a subdirectory or a linked worktree). Accepting trust grants that whole repository — every subdirectory and linked worktree of the root — so the trust dialog should name this root alongside `directory`. Informational only: the attestation echo still pins `trusted_directory` to `directory`. Vetted by the same visible-glyph rule as `directory`: a canonical root that fails it rejects the request (reason: unsafe_path), since accepting would record trust under that root.
