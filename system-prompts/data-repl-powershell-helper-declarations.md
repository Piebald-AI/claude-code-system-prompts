<!--
name: "Data: REPL PowerShell helper declarations"
description: "Describes the synchronous PowerShell runner and shared REPL helpers for shell calls, files, previews, and tool discovery"
ccVersion: "2.1.328"
-->
/** The shell. The template text goes to the shell as written, except that ` and ${ lose their backslash, so a backtick or ${ the shell should see literally goes in as a ${} value. $ single-quotes each string ${} value itself as one argument (an array: one per item; ${{raw: s}} splices s unquoted), so write ${x} bare: inside quote marks of your own, the quotes $ added no longer protect the value, and shell syntax in it can run. $(cmd, ms) runs a command given as a plain string, with an optional timeout in ms. Resolves to a ShellOutput; .nothrow() hands it back whatever the exit code. A non-zero exit throws a ShellError. The whole output of a command that would not throw even without .nothrow() is yours even when large: file names the spill file, which holds the first 64 MiB, and truncated means stdout holds only the start of the output, the rest being in that file. A failing command's output (with or without .nothrow()) has no file and can come back with its middle cut out; the end of a very long failing output can be missing too. Then truncated is true, on the ShellError too, and a line on this REPL call's stderr (not in .stderr) says what is missing. Timeouts cap at 600000 ms: past that the command keeps running in the background, and running names the task and the file its output streams to, so that file can be read instead of running the command again. */
declare function $(strings: TemplateStringsArray, ...values: unknown[]): ShellPromise;
declare function $(cmd: string, timeoutMs?: number): ShellPromise;
declare namespace $ {
    function escape(s: string): string;
    const ShellError: new (out: ShellOutput) => ShellError;
}
interface ShellPromise extends Promise<ShellOutput> {
    nothrow(): ShellPromise;
    throws(on: boolean): ShellPromise;
    quiet(): ShellPromise;
    timeout(ms: number): ShellPromise;
    cwd(dir: string): ShellPromise;
    env(vars: Record<string, string>): ShellPromise;
    /** called right after $ with no await in between, as in await $`cmd`.text(), they read the whole output, up to 64 MiB, when Claude Code could read it */
    text(): Promise<string>;
    lines(): Promise<string[]>;
    json(): Promise<unknown>;
    /** once the command has ended: true when none of Claude Code's checks found that these readers return less than the command printed */
    whole?: boolean;
}
interface ShellOutput {
    /** the command's stderr is merged into stdout, so 2>&1 adds nothing; stderr holds the shell tool's own notices, or else the same text as error */
    stdout: string;
    stderr: string;
    /** null while it runs on in the background (running) */
    exitCode: number | null;
    /** they read stdout; each throws a ShellError while the command is still running */
    text(): string;
    lines(): string[];
    json(): unknown;
    /** the text the result shows: stdout, then [stderr], [error] and [exit N] when there are any */
    output: string;
    /** file: the spill file; truncated: stdout holds only part of the output; whole: none of Claude Code's checks found that the readers return less than the command printed */
    truncated: boolean;
    whole: boolean;
    file?: string;
    bytes?: number;
    /** a PostToolUse hook rewrote the start of a saved output and gave no path to the rest; stdout holds only the hook's text */
    withheld?: true;
    /** outlived its timeout; runs on, output streaming to outputPath */
    running?: {
        taskId: string;
        outputPath: string;
    };
    /** why the call failed outside the command (a denial, a refusal, an interruption); the shell tool's reading of its exit */
    error?: string;
    note?: string;
    /** the sandbox blocked the command, so this is its retry outside the sandbox; violation: what the first run's output reported as blocked */
    unsandboxedRetry?: {
        violation: string;
    };
}
interface ShellError extends Error {
    stdout: string;
    stderr: string;
    exitCode: number | null;
    running?: {
        taskId: string;
        outputPath: string;
    };
    unsandboxedRetry?: {
        violation: string;
    };
    /** stdout holds only part of the command's output */
    truncated?: boolean;
}
/** An exact-string edit (next inserted literally; a replacement string given to String.prototype.replace is not, since it expands $&, $`, $', $$ and $1, so s.replace(a, () => b) passes a function, which inserts b as it is); throws on zero or several matches, {all} replaces every match, {soft} resolves {ok: false, error} instead. The batch form checks every anchor, in order, before it writes, so an anchor not found, or found more than once without {all}, leaves the file untouched; a failure after that (a permission denial, say) leaves the edits before it applied. */
declare function edit(path: string, old: string, next: string, opts?: {
    all?: boolean;
    soft?: boolean;
}): Promise<{
    ok: boolean;
    replacements: number;
    error?: string;
}>;
declare function edit(path: string, edits: [old: string, next: string][], opts?: {
    all?: boolean;
    soft?: boolean;
}): Promise<{
    ok: boolean;
    replacements: number;
    error?: string;
}>;
/** Writes a whole file (directories created); resolves the byte count. */
declare function write(path: string, content: string): Promise<number>;
/** One file, read when a method is called; a relative path is from the working directory. */
declare function file(path: string): {
    name: string;
    text(): Promise<string>;
    json(): Promise<unknown>;
    lines(): Promise<string[]>;
    exists(): Promise<boolean>;
    /** lines from the 1-based line offset, at most limit */
    slice(offset?: number, limit?: number): Promise<string>;
};
/** Resolves after ms. */
declare function sleep(ms: number): Promise<void>;
/** The first n chars (200 by default) of String(value), with a marker when it cuts; for a $ result that was saved to a file, its size and path first. */
declare function preview(output: ShellOutput | string, n?: number): string;
declare function preview(value: unknown, n?: number): string;
/** The output channel: each call is a line delivered with the result. */
declare function log(...args: unknown[]): void;
/** globalThis, so self.log is log. */
declare const self: typeof globalThis;
/** Not delivered with the result; tail(n) reads the last n lines back. */
declare var console: {
    log(...args: unknown[]): void;
    info(...args: unknown[]): void;
    debug(...args: unknown[]): void;
    warn(...args: unknown[]): void;
    error(...args: unknown[]): void;
    tail(n?: number): string;
    buffer(): string;
    dropped(): number;
};
/** Timers are cleared when the script that set them ends. */
declare function setTimeout(fn: () => void, ms?: number): number;
declare function clearTimeout(id: number): void;
declare function setInterval(fn: () => void, ms?: number): number;
declare function clearInterval(id: number): void;
declare function atob(data: string): string;
declare function btoa(data: string): string;
type JSONSchema = Record<string, unknown>;
/** The tools a script can call, by words from their name or description; input is the tool's parameters written as a TypeScript type, such as {query: string, limit?: number}. Resolves {error} for an empty query. */
declare function searchTools(query: string, max?: number): Promise<{
    name: string;
    about: string;
    input: string;
}[] | {
    error: string;
}>;
/** One tool's description and input schema; {error} for a name no tool has. */
declare function describeTool(name: string): Promise<{
    name: string;
    description: string;
    inputSchema: JSONSchema;
} | {
    error: string;
}>;
