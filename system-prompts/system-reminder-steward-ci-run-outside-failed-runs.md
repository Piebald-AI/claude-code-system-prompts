<!--
name: "System Reminder: Steward CI run outside failed runs"
description: "Explains why a pass can't rerun or inspect a CI run outside the failed runs it found for the pull request"
ccVersion: "2.1.330"
variables:
  - "RUN_ID"
-->
run ${RUN_ID} isn't among the failed runs that Claude Code found on this pull request's head when this pass began, nor on a fresh look just now, and it lets a pass read or run again only those. A run that is still going is found once it has ended, and one that ended a moment ago a little later: leave that check to a later pass, and don't tell the user that you can't read it. If a later pass is refused the same run again with no check pending any more, name the check to the user once. No other spelling will do
