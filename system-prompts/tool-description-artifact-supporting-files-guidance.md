<!--
name: "Tool Description: Artifact supporting files guidance"
description: "Explains how Artifact supporting-file maps, source paths, content types, and root directory resolution work"
ccVersion: "2.1.216"
-->
**Supporting files**: To publish a multi-file artifact (separate CSS/JS/data/images), pass `files` as a map of published path → source file: `{"app.js": "dist/app.js", "data/points.json": "build/points.json"}`. The published path (the key) is what the HTML references (`<script src="app.js">`); the source (the value) is where the bytes come from on disk — a path string, or `{from, contentType}` when the type can't be inferred from the published extension. Pass `root` to resolve all relative sources against one base directory instead of retyping a long build prefix (`root: "dist"` + `{"app.js": "app.js"}`) — `root` never changes published paths, only where sources are read from. A plain list of paths still works when each file should be published at its own on-disk spelling. Sources must lie under the working directory; list every file explicitly.

