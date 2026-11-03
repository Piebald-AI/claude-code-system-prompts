<!--
name: "Tool Description: Poll Code Mode idle and event waiting"
description: "Describes Code Mode Poll waiting, immediate event delivery, user-message arrival, cache-aware wait limits and the meaning of an empty delivery"
ccVersion: "2.1.318"
variables:
  - "NO_PENDING_EVENTS_MESSAGE"
  - "NO_PENDING_EVENTS_GUIDANCE"
-->
Calling this tool with nothing else to do signals that you are idle. If events are pending, they are returned immediately as this call's result. Otherwise the call waits until something arrives: a script ending, another event, or a message from the user. Events come back as the result. When the user sends a message, usually the call returns (with the literal result "${NO_PENDING_EVENTS_MESSAGE}" if no event came with it) and the message follows the result in the same turn, as user text; nothing ends your turn for you. The wait also ends shortly before the prompt cache would expire, with a line saying what is still running; if something is queued for the end of your turn, it ends by then with "${NO_PENDING_EVENTS_MESSAGE}" instead. ${NO_PENDING_EVENTS_GUIDANCE}
