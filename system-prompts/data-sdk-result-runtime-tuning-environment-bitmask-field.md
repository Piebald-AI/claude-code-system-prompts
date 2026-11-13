<!--
name: "Data: SDK result runtime tuning environment bitmask field"
description: "Documents the startup runtime-tuning environment-variable bitmask reported by eligible cloud workers"
ccVersion: "2.1.323"
-->
@internal Which runtime tuning variables the CLI process was started with, one bit for each that was set and not empty: 1 BUN_GC_TIMER_INTERVAL, 2 MIMALLOC_PURGE_HOLES_MIN_INTERVAL, 4 BUN_IDLE_GC_SECONDS, 8 MIMALLOC_PURGE_DELAY, 16 BUN_JSC_useFTLJIT, 32 BUN_JSC_percentCPUPerMBForEdenTimer, 64 BUN_JSC_percentCPUPerMBForFullTimer. It says that a name was set, never to what. It is taken once, as the process starts, because that is when the runtime reads them: a worker adopted from a warm spare reports the spare's own variables, not the ones its claim brought. Sent only by the workers named under process_rss_mib_turn_start, unless the session runs in claude-code-server. They put it on a session's results as they write them, whatever the subtype and whether or not the turn sent a request. A result that reports a failed start or a fatal error is written raw and has none.
