<!--
name: 'System Reminder: New diagnostics detected'
description: Notification about new diagnostic issues
ccVersion: 2.1.122
variables:
  - DIAGNOSTICS_SUMMARY
  - DIAGNOSTICS_LIST
-->
<new-diagnostics>The following new diagnostic issues were detected:

${DIAGNOSTICS_SUMMARY.formatDiagnosticsSummary(DIAGNOSTICS_LIST)}</new-diagnostics>
