<!--
name: 'System Reminder: Agent mention'
description: Notification that user wants to invoke an agent
ccVersion: 2.1.18
variables:
  - ATTACHMENT_OBJECT
-->
The user has expressed a desire to invoke the agent "${ATTACHMENT_OBJECT.agentType}". Please invoke the agent appropriately, passing in the required context to it. 
