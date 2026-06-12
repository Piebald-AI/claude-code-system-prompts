<!--
name: 'Data: Claude API reference — Ruby'
description: Ruby SDK reference including installation, client initialization, basic requests, streaming, and beta tool runner
ccVersion: 2.1.176
-->
# Claude API — Ruby

> **Note:** The Ruby SDK supports the Claude API. A tool runner is available in beta via `client.beta.messages.tool_runner()`. Agent SDK is not yet available for Ruby.

## Installation

```bash
gem install anthropic
```

## Client Initialization

```ruby
require "anthropic"

# Default (uses ANTHROPIC_API_KEY env var)
client = Anthropic::Client.new

# Explicit API key
client = Anthropic::Client.new(api_key: "your-api-key")
```

---

## Basic Message Request

```ruby
message = client.messages.create(
  model: :"{{OPUS_ID}}",
  max_tokens: 16000,
  messages: [
    { role: "user", content: "What is the capital of France?" }
  ]
)
# content is an array of polymorphic block objects (TextBlock, ThinkingBlock,
# ToolUseBlock, ...). .type is a Symbol — compare with :text, not "text".
# .text raises NoMethodError on non-TextBlock entries.
message.content.each do |block|
  puts block.text if block.type == :text
end
```

---

## Streaming

```ruby
stream = client.messages.stream(
  model: :"{{OPUS_ID}}",
  max_tokens: 64000,
  messages: [{ role: "user", content: "Write a haiku" }]
)

stream.text.each { |text| print(text) }
```

---

## Tool Use

The Ruby SDK supports tool use via raw JSON schema definitions and also provides a beta tool runner for automatic tool execution.

### Tool Runner (Beta)

```ruby
class GetWeatherInput < Anthropic::BaseModel
  required :location, String, doc: "City and state, e.g. San Francisco, CA"
end

class GetWeather < Anthropic::BaseTool
  doc "Get the current weather for a location"

  input_schema GetWeatherInput

  def call(input)
    "The weather in #{input.location} is sunny and 72°F."
  end
end

client.beta.messages.tool_runner(
  model: :"{{OPUS_ID}}",
  max_tokens: 16000,
  tools: [GetWeather.new],
  messages: [{ role: "user", content: "What's the weather in San Francisco?" }]
).each_message do |message|
  puts message.content
end
```

### Manual Loop

See the [shared tool use concepts](../shared/tool-use-concepts.md) for the tool definition format and agentic loop pattern.

---

## Prompt Caching

`system_:` (trailing underscore — avoids shadowing `Kernel#system`) takes an array of text blocks; set `cache_control` on the last block. Plain hashes work via the `OrHash` type alias. For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.

```ruby
message = client.messages.create(
  model: :"{{OPUS_ID}}",
  max_tokens: 16000,
  system_: [
    { type: "text", text: long_system_prompt, cache_control: { type: "ephemeral" } }
  ],
  messages: [{ role: "user", content: "Summarize the key points" }]
)
```

For 1-hour TTL: `cache_control: { type: "ephemeral", ttl: "1h" }`. There's also a top-level `cache_control:` on `messages.create` that auto-places on the last cacheable block.

Verify hits via `message.usage.cache_creation_input_tokens` / `message.usage.cache_read_input_tokens`.

---

## Stop Details

When `stop_reason` is `:refusal`, the response includes structured `stop_details`:

```ruby
if message.stop_reason == :refusal && message.stop_details
  puts "Category: #{message.stop_details.category}"     # e.g. :cyber, :bio, :reasoning_extraction, :frontier_llm, or nil — see docs for the full set
  puts "Explanation: #{message.stop_details.explanation}"
end
```

**Refusal fallbacks ({{FABLE_NAME}}) — opt in by default.** Fallbacks are opt-in: without them a refused request simply stops. New `{{FABLE_ID}}` code should include the server-side `fallbacks` parameter (beta header `server-side-fallback-2026-06-01`, `fallbacks: [{model: "{{OPUS_ID}}"}]` on the beta messages call) by default. The exact Ruby binding (and the client-side middleware for providers without server-side support) is not documented here — WebFetch the Ruby SDK repo's `examples/` from `shared/live-sources.md`; full semantics in `shared/model-migration.md` → Migrating to {{FABLE_NAME}} → `refusal` stop reason.

---

## Error Type

`APIStatusError` exposes a `.type` field for programmatic error classification:

```ruby
begin
  client.messages.create(...)
rescue Anthropic::APIStatusError => e
  puts e.type  # :rate_limit_error, :overloaded_error, etc.
end
```
