<!--
name: "Data: SDK workspace diff root ID field"
description: "Explains how a diff client can use the returned root ID to open paths relative to the same directory"
ccVersion: "2.1.331"
-->
An opaque value that stands for the directory this diff's paths are relative to. To open one of those paths, send it back unchanged as the `rootId` of read_file's diff_root anchor, and keep it with any file view opened that way, so that reloading the view sends the same value. It reveals no path, and only the process that made it accepts it. A Claude Code version that predates it sends none and checks none: it reads a diff_root path against the directory it finds at the time of the read, or refuses it where its diff follows the shell's cwd between several repositories.
