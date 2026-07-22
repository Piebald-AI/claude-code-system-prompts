<!--
name: "Data: /auto-mode-setup usage"
description: "Defines /auto-mode-setup proposal and reviewed-apply command syntax, request ID ordering, save-target validation, and integrity requirements"
ccVersion: "2.1.217"
-->
Usage:
  /auto-mode-setup [--request-id <uuid>] --wizard posture=<personal|open-source|enterprise|mixed> scope=<all|project> depth=<both|shell|repos|here> --propose
  /auto-mode-setup [--request-id <uuid>] [--apply-target <user|project>] --expect-sha256 <64-hex> --apply-file <absolute-path>   (reads a proposal JSON from a file under the system temp dir or the Claude config dir — the caller must have shown it to the user first; --expect-sha256 is required and the apply refuses unless the file’s exact bytes hash to the given sha256)

--request-id must come first when used. The token must be a UUID (canonical 8-4-4-4-12 hex-and-dash form, either case) and is echoed verbatim as "requestId" on the command's JSON result, so a host with several commands in flight can match replies to requests.

--apply-target doesn’t change where the config is written — entries always land in the user settings file. It refuses a proposal whose scope answer doesn’t match the save choice (user ↔ scope=all, project ↔ scope=project). Flags ride in the order shown; everything after --apply-file is the path.
