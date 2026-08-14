<!--
name: "Tool Description: ToolSearch (input validation note)"
description: "Explains the InputValidationError failure for unfetched deferred tools and requires selecting named deferred tools before calling them"
ccVersion: "2.1.231"
-->
 Until fetched, only the name is known — there is no parameter schema, so calling the tool fails with InputValidationError. When any instruction, system reminder, or other tool's description names a deferred tool, fetch it with query "select:<name>" before calling it.
