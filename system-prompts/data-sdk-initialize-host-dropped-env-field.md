<!--
name: "Data: SDK initialize host_dropped_env field"
description: "Lists managed provider or gateway environment variable names that Claude Desktop stripped at launch, without their values"
ccVersion: "2.1.327"
-->
@internal Only in a session that Claude Desktop itself started: the variables by which an administrator's managed settings choose a provider or a gateway, where this start dropped them and requests go straight to Anthropic instead. `source` is 'policySettings'; ignore any other value. `names` are upper-case variable names, never values. Worked out anew for every init. Omitted when there is nothing to list, on any transport that stores its frames, from the init sent over the Remote Control bridge, and on CLIs that predate the field.
