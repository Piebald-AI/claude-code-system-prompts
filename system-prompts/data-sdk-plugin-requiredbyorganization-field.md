<!--
name: "Data: SDK plugin requiredByOrganization field"
description: "Documents how an SDK host marks an organization-required plugin without granting it permissions"
ccVersion: "2.1.327"
-->
@internal States that the person's organization requires or auto-installs this plugin. Mods see it on plugin.register, which judges it in the organization's tier when it has no hooks module and is shown to be outside every dev-mods folder, and an unmarked copy of its name does not load beside it; it grants no permission (docs/desktop-host-contract.md, D109a). The Agent SDK sends a marked entry in the initialize request under --await-initialize (Claude Code 2.1.261 or newer) whatever pluginDelivery says.
