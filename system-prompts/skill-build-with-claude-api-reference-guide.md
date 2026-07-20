<!--
name: "Skill: Build with Claude API (reference guide)"
description: "Template for presenting language-specific reference documentation with quick task navigation"
ccVersion: "2.1.182"
-->
## Reference Documentation

The relevant documentation for your detected language is included below in `<doc>` tags. Each tag has a `path` attribute showing its original file path. Use this to find the right section:

### Quick Task Reference

> All SDK languages use the same per-language `claude-api/` directory layout (cURL: `curl/examples.md`). Not every language has every file — if a file is absent, that feature's example is not yet documented for that language; fall back to the cURL shape or WebFetch the SDK repo.

**Single text classification/summarization/extraction/Q&A:**
→ Refer to `{lang}/claude-api/README.md`

**Chat UI or real-time response display:**
→ Refer to `{lang}/claude-api/README.md` + `{lang}/claude-api/streaming.md`

**Long-running conversations (may exceed context window):**
→ Refer to `{lang}/claude-api/README.md` — see Compaction section

**Migrating to a newer model or replacing a retired model:**
→ Refer to `shared/model-migration.md`

**Prompt caching / optimize caching / "why is my cache hit rate low":**
→ Refer to `shared/prompt-caching.md` + `{lang}/claude-api/README.md` (Prompt Caching section)

**Count tokens in a file / prompt / diff ("how many tokens is X"):**
→ Refer to `shared/token-counting.md` — use `messages.count_tokens`, never `tiktoken`

**Function calling / tool use / agents:**
→ Refer to `{lang}/claude-api/README.md` + `shared/tool-use-concepts.md` + `{lang}/claude-api/tool-use.md`

**Batch processing (non-latency-sensitive):**
→ Refer to `{lang}/claude-api/README.md` + `{lang}/claude-api/batches.md`

**File uploads across multiple requests:**
→ Refer to `{lang}/claude-api/README.md` + `{lang}/claude-api/files-api.md`

**Agent design (tool surface, context management, caching strategy):**
→ Refer to `shared/agent-design.md`

**Anthropic CLI (`ant`) — terminal access, version-controlled agent/environment YAML, scripting:**
→ Refer to `shared/anthropic-cli.md`

**Managed Agents (server-managed stateful agents):**
→ Refer to `shared/managed-agents-overview.md` and the rest of the `shared/managed-agents-*.md` files. For Python, TypeScript, Go, Ruby, PHP, and Java, read the `managed-agents/README.md` in the language folder for code examples. For cURL, read `curl/managed-agents.md`. C# has beta Managed Agents support — use `curl/managed-agents.md` as the wire-level reference (the C# SDK mirrors it via `client.Beta.Agents`; see `csharp/claude-api/README.md`).

**Error handling:**
→ Refer to `shared/error-codes.md`

**Latest docs via WebFetch:**
→ Refer to `shared/live-sources.md` for URLs
