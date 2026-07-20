<!--
name: "Data: Claude Code gateway protocol"
description: "Markdown reference documenting the Claude Code gateway wire contract, including OAuth 2.0 device flow, RFC 8414 discovery, Messages API inference, managed settings, model discovery, OTLP telemetry, error envelopes, TLS certificate pinning, and proxying to Bedrock, Vertex, and Foundry"
ccVersion: "2.1.211"
-->
# Claude Code gateway protocol

This is the wire contract the Claude Code CLI uses to talk to this gateway:
sign-in, inference, managed settings, and telemetry. It's served from the
gateway itself so it always matches the version you're running.

> **Stability:** this protocol exists to give you a more stable target than
> proxying raw CLI traffic. Auth is standard OAuth 2.0, inference is the
> Messages API, and headers are the lowest common denominator across
> backends. We keep it backwards compatible within reason to support older
> clients, but not forever — expect changes, managed settings in particular,
> with notice.

A developer points Claude Code at your gateway's base URL via `/login` and
the client does the rest. All paths below are relative to that base URL, and
the client does not follow cross-origin redirects.

## Flow

1. Client fetches `GET {base}/.well-known/oauth-authorization-server`.
2. On first contact, client fingerprints your TLS certificate and asks the
   user to trust it.
3. Client runs the RFC 8628 device flow: `POST device_authorization_endpoint`
   -> user approves in a browser at `verification_uri` -> client polls
   `token_endpoint` until it gets a bearer token.
4. Client sends `Authorization: Bearer <token>` on every subsequent request.
5. Client uses fixed paths under `{base}` for inference (`/v1/messages`),
   policy (`/managed/settings`), model discovery (`/v1/models`), and
   telemetry (`/v1/{metrics,logs,traces}`).
6. Before the token expires, client silently calls `token_endpoint` with
   `grant_type=refresh_token`. If you didn't issue a refresh token, the user
   is sent back through the browser flow instead.

## Discovery — required

`GET /.well-known/oauth-authorization-server` (unauthenticated)

RFC 8414 authorization server metadata. The client reads
`device_authorization_endpoint` and `token_endpoint` and ignores the rest;
both must be same-origin with `{base}`. `authorization_endpoint` is
intentionally absent.

    {
      "issuer": "https://gw.corp.example.com",
      "device_authorization_endpoint": "https://gw.corp.example.com/oauth/device_authorization",
      "token_endpoint": "https://gw.corp.example.com/oauth/token",
      "grant_types_supported": ["urn:ietf:params:oauth:grant-type:device_code", "refresh_token"]
    }

## Device authorization — required

`POST {device_authorization_endpoint}` (unauthenticated)

RFC 8628 §3.2. The client opens `verification_uri_complete` in the user's
browser and polls `token_endpoint` every `interval` seconds.

    {
      "device_code": "AbK9-s3n4C8H...",
      "user_code": "WDJB-MJHT",
      "verification_uri": "https://gw.corp.example.com/device",
      "verification_uri_complete": "https://gw.corp.example.com/device?user_code=WDJB-MJHT",
      "expires_in": 600,
      "interval": 5
    }

`device_code` should be >=256 bits, opaque, single-use. `user_code` should
use a base-20 charset (RFC 8628 §6.1).

## Verification page — required

`GET/POST {verification_uri}` (browser-facing; the client never calls this)

Accept the user code, authenticate the user against your IdP, and mark the
matching `device_code` approved so the next token poll succeeds. Apply a
per-IP rate limit (RFC 8628 §5.1) and don't auto-submit a pre-filled code
(§5.4).

## Token — required

`POST {token_endpoint}` (unauthenticated,
`application/x-www-form-urlencoded`)

**Device grant** (`grant_type=urn:ietf:params:oauth:grant-type:device_code`):

| Status | Body | Client reaction |
|---|---|---|
| 200 | `{"access_token","token_type":"Bearer","expires_in","refresh_token"?}` | Login complete. `refresh_token` is optional; omit it and the client re-runs the device flow on expiry. |
| 400 | `{"error":"authorization_pending"}` | Keep polling. |
| 400/429 | `{"error":"slow_down"}` | Add 5s to the poll interval. |
| 400 | `{"error":"access_denied"}` | Stop. |
| 400 | `{"error":"expired_token"}` | Stop. |

**Refresh grant** (`grant_type=refresh_token`): return a fresh
`{"access_token","token_type","expires_in","refresh_token"}` on 200. Return
`401 {"error":"invalid_grant"}` to force re-login — this is your
deprovisioning hook.

## Messages — required

`POST /v1/messages` and `POST /v1/messages/count_tokens` (bearer)

The Anthropic Messages API (https://platform.claude.com/docs/en/api/messages),
unchanged. Proxy to your upstream and stream the response back. Enforce your
model allowlist here, returning `400 invalid_request_error` for a denied
model. Don't buffer SSE on the `stream: true` path. The client always sets
`Content-Length`, so you may reject chunked-without-CL (`411`) and cap body
size (`413`). The client doesn't assume server-side tools are available. The
client also sends `x-app` and `x-stainless-*` headers — pass them through or
drop them, but don't reject the request because of them.

## Managed settings — optional

`GET /managed/settings` (bearer)

The authenticated user's Claude Code `managed-settings.json`; see
https://code.claude.com/docs/en/settings for the key reference. The client
polls about once an hour; support `ETag`/`If-None-Match` -> `304` to keep
that cheap. Return `404` for "no managed policy"; `200 {}` means "this user
has an empty policy" — they're not the same. **This is the endpoint most
likely to change.**

## Models — optional

`GET /v1/models` (bearer)

Anthropic models-list shape: `{"data":[{"id","display_name"},...]}`. Use
Anthropic-style IDs (`claude-{family}-{major}-{minor}`) — the client's
model-family logic keys on that shape. The client only calls this when
`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` is set on the client, which you
can push via the `env` block in `/managed/settings`. Return `404` to fall
back to the client's built-in list.

## Telemetry — optional

`POST /v1/metrics`, `/v1/logs`, `/v1/traces` (bearer)

OTLP/HTTP (protobuf or JSON). When connected to a gateway the client sends
telemetry here and ignores `OTEL_EXPORTER_OTLP_*` env vars. Return `200`
whether you forward or discard — `404` makes the client's exporter log an
error on every flush.

## Errors

OAuth endpoints use `{"error":"...","error_description":"..."}`
(RFC 6749/8628). Bearer-authenticated endpoints use the Anthropic envelope so
the SDK surfaces the message to the user:

    {"type":"error","error":{"type":"authentication_error","message":"..."}}

| HTTP | error.type | Use for |
|---|---|---|
| 400 | `invalid_request_error` | Denied model, malformed body, policy violation |
| 401 | `authentication_error` | Missing/expired/invalid bearer; client prompts re-login |
| 403 | `permission_error` | Authenticated but not allowed |
| 413 | `request_too_large` | Body over your cap |
| 429 | `rate_limit_error` | Throttling; include `Retry-After` |
| 501 | `not_supported` | Endpoint not available on this backend |
| 529 | `overloaded_error` | Upstream at capacity; client backs off and retries |
| 5xx | `api_error` | Anything else |

## Bearer token

Your `access_token` is opaque to the client — it stores it, sends it, and
refreshes it before `expires_in`, but never inspects the payload. Encode the
user's identity and groups in the token (or in server-side state keyed by it)
so you can apply per-user RBAC at `/v1/messages` and per-group policy at
`/managed/settings`. The same token must work across every
bearer-authenticated endpoint.

## TLS

`https://` is required; `http://` is accepted only for loopback during
development. The client pins the SHA-256 fingerprint of your TLS leaf
certificate per-hostname after the user confirms it on first connect, and
re-prompts on mismatch — rotating your certificate costs every user one
confirmation prompt.

## Client guarantees

- OAuth endpoint paths come from your discovery document; the client never
  hard-codes `/oauth/token`.
- Fixed-path endpoints are resolved against `{base}`, never a redirect.
- Every request body carries `Content-Length`.
- The OTLP exporter is locked to `{base}/v1/{signal}` regardless of the
  user's environment.
- `404` from `/v1/models` or `/managed/settings` is a clean "not
  implemented", with no retry storm.

## Proxying to Bedrock, Vertex, or Foundry

Proxying to `api.anthropic.com` is pass-through. Proxying to a cloud
provider's Claude endpoint needs translation:

- **Model IDs.** The client sends Anthropic-style IDs like
  `claude-sonnet-4-5`; translate to the upstream's form (Bedrock model ID or
  inference-profile ARN; Vertex `@`-versioned ID), or advertise
  upstream-native IDs from `/v1/models`.
- **`anthropic-beta`.** Bedrock rejects some betas in the *header*; move them
  into the request body as `"anthropic_beta": [...]`. Vertex and Foundry
  accept the header.
- **Streaming.** Bedrock's native stream is AWS binary event-stream, not SSE;
  decode and re-emit Anthropic-shaped `text/event-stream`. The provider SDKs
  handle this.
- **`count_tokens`.** Bedrock has no count-tokens API. Return
  `501 not_supported`; the client falls back to a Haiku `max_tokens:1` probe.
- **Headers.** Forward `content-type`, `accept`, `accept-encoding`,
  `anthropic-version`, `anthropic-beta`, `user-agent`, and `x-stainless-*`;
  strip the client's `Authorization` and apply the upstream's own
  credentials. On the response, strip hop-by-hop headers
  (`content-encoding`, `content-length`, `transfer-encoding`, `connection`).
- **Errors.** Upstream error messages can carry your cloud account
  IDs/ARNs/project IDs — log them for the operator, return a generic
  message, but keep `error.type` so the client's retry logic still works.

## References

RFC 6749 (OAuth 2.0), RFC 8414 (AS metadata), RFC 8628 (device grant),
Anthropic Messages API, Claude Code settings reference, OTLP spec.
