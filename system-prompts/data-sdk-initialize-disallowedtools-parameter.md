<!--
name: "Data: SDK initialize disallowedTools parameter"
description: "Documents passing denied tools and rules through the SDK initialize request at launch"
ccVersion: "2.1.327"
-->
@internal The tools and rules to deny, in the same shape as the SDK `disallowedTools` option, so that the launch command line does not grow with them. Read only by a CLI launched with --await-initialize and --initialize-fields=disallowedTools. It applies them as it applies --disallowedTools with the entries joined by commas, and exits with code 1 when it cannot, as for `settings`. Without those flags, on a repeated initialize, or over a remote session transport the field sets nothing; disallowed_tools_applied in the response reports whether this list is the one taken at launch.
