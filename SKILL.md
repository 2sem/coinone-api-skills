---
name: coinone-openapi
description: Use when building or debugging integrations against Coinone Open API REST or WebSocket endpoints. Covers Public API V2, Private API V2.1, legacy Private API V2, authentication, signing, rate limits, error handling, and endpoint selection.
---

# Coinone OpenAPI Skill

Use this skill for Coinone Open API work.

## Default scope

- Prefer `Public API V2`
- Prefer `Private API V2.1`
- Use `Public WebSocket` and `Private WebSocket` when streaming is needed
- Treat `PUBLIC API V1 (Deprecated)` and legacy `Private API V2` as fallback-only

## Source of truth

- Docs home: `https://docs.coinone.co.kr/docs`
- API reference: `https://docs.coinone.co.kr/reference/`
- Changelog: `https://docs.coinone.co.kr/changelog`
- REST base: `https://api.coinone.co.kr`
- Public WS: `wss://stream.coinone.co.kr`
- Private WS: `wss://stream.coinone.co.kr/v1/private`

## Operating procedure

1. Pick the API family from `references/endpoint-index.md`.
2. Read the matching guide:
   - `references/public-rest-v2.md`
   - `references/private-rest-v21.md`
   - `references/private-rest-v2-legacy.md`
   - `references/public-rest-v1-deprecated.md`
   - `references/websocket.md`
3. Apply auth/signing rules from `references/auth-signing.md`.
4. Validate rate limit and error handling from `references/rate-limits-and-errors.md`.
5. For order placement, follow `references/order-safety.md` before sending any private order request.
6. Check changelog if using recent features like reward APIs or websocket chart/private websocket.

## Hard rules

- Never default to deprecated APIs if a V2/V2.1/WebSocket equivalent exists.
- Never log raw secrets, signatures, or full private auth payloads.
- Preserve numeric precision for prices, qty, and amount as strings unless the caller explicitly needs numeric parsing.
- Private REST requires `X-COINONE-PAYLOAD` and `X-COINONE-SIGNATURE`.
- `V2.1` nonce must be UUID v4.
- Legacy `V2` nonce must be a strictly increasing positive integer.
- Request enums are case-sensitive. Do not lowercase values like `LIMIT`, `MARKET`, `STOP_LIMIT`, `SUBSCRIBE`, `PING`, `SHORT`.
- Do not blindly retry order placement. Use `user_order_id` or follow-up order lookup first.
- Validate price units with the range-unit API before limit-style order submission.

## Output contract

When using this skill, always output:

1. Chosen endpoint and why
2. API version and auth mode
3. Required params, optional params, and validation notes
4. Exact headers to send with secrets redacted
5. Safe request example
6. Expected success shape and key response fields
7. Error handling plan
8. Rate-limit/retry plan

## Local references

- `references/endpoint-index.md`
- `references/auth-signing.md`
- `references/rate-limits-and-errors.md`
- `references/order-safety.md`
- `references/public-rest-v2.md`
- `references/private-rest-v21.md`
- `references/private-rest-v2-legacy.md`
- `references/public-rest-v1-deprecated.md`
- `references/websocket.md`
