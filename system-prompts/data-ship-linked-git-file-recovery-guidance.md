<!--
name: "Data: Ship linked git file recovery guidance"
description: "Gives the user recovery steps when a git file or folder is a link, has multiple hard links or can't be read safely by /ship"
ccVersion: "2.1.331"
-->
Check what it is: ls -l shows where a link points, or a count above 1 for a hard link. Leave it where it is: git may need it. If you know what made it and trust it, commit your work on a branch of its own yourself, then run /ship again. For a hard link you can instead copy the file and move the copy over it; /ship then names the next, if there is one. If you can't tell what made it, run no git here until you know where it leads. If it's an ordinary folder, check that you can open it, then run /ship again.
