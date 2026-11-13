<!--
name: "Tool Description: Artifact preflight.js reserved file"
description: "Notes that preflight.js at the artifact root is reserved, runs against open pages when updates are published, and must be an ES module of at most 8 KiB with a default-exported function or the publish is refused"
ccVersion: "2.1.323"
-->
 `preflight.js` at the artifact root is reserved — it runs against open pages when you publish updates; it must be a ≤ 8 KiB ES module whose default export is a function, or the publish is refused.
