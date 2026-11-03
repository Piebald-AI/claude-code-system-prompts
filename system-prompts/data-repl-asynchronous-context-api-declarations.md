<!--
name: "Data: REPL asynchronous context API declarations"
description: "Defines asynchronous REPL context spawning, release, status, cost, result and messaging APIs with optional conversation forking"
ccVersion: "2.1.318"
-->
/** Starts a context: a full agent with the session's tools, called name (a-z, 0-9 and '-', never reused) and briefed with initialPrompt. With fork: true it starts from this session's conversation instead of from its brief alone, and carries all of it on every later step. Throws when the spawn is refused, with the reason. */
declare function spawnContext(opts: {
    name: string;
    role?: string;
    initialPrompt: string;
    fork?: boolean;
}): Promise<{
    name: string;
    role: string;
}>;
/** Stops a context you spawned. */
declare function releaseContext(opts: {
    name: string;
} | string): Promise<{
    name: string;
}>;
/** Every context: status 'ready' (not started), 'stepping' (working), 'idle' (waiting for a message), 'failed' or 'released'; cost once it has finished a turn. */
declare function listContexts(): Promise<{
    name: string;
    role: string;
    parent: string;
    status: ContextStatus;
    cost?: ContextCost;
}[]>;
type ContextStatus = 'ready' | 'stepping' | 'idle' | 'failed' | 'released';
type ContextCost = {
    inputTokens: number;
    outputTokens: number;
};
/** A handle on any context by name; inside a context, contexts.lead is the main thread. */
declare var contexts: {
    [name: string]: ContextHandle;
};
interface ContextHandle {
    name: string;
    readonly status: ContextStatus;
    readonly role?: string;
    readonly parent?: string;
    state: {
        readonly lastText: string;
        readonly cost?: ContextCost;
    };
    /** its last n turns, oldest first */
    tail(n?: number): Promise<{
        name: string;
        at: string;
        text: string;
    }[]>;
    /** once idle, failed or released */
    result(): Promise<{
        status: ContextStatus;
        text: string;
        cost?: ContextCost;
    }>;
    /** sends it a message */
    log(text: string): Promise<true>;
}
