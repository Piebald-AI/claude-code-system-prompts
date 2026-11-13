<!--
name: "Tool Parameter: Artifact supporting files (local sources only)"
description: "Describes Artifact supporting-file maps and lists without cross-artifact sources, including typed sources, update preservation and removal, and the restriction of sources to the working or scratchpad directory"
ccVersion: "2.1.323"
-->
Supporting files to publish alongside the page. Map form {"published/path": "source/path" | {from, contentType} | null} publishes each source at the key (what the HTML references); when updating an existing artifact, files left out of the map are kept and null removes that path. List form publishes each file at its own spelling. Sources must lie under the working directory or your scratchpad directory (as your system prompt names it).
