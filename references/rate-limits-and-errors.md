# Coinone rate limits and errors

## Rate limits

### Public API

| Version | Limit | Scope |
|---|---|---|
| V2 | 1200/min | per IP |
| V1 | 600/min | per IP |

### Private API

| Version | Order APIs | Other APIs | Scope |
|---|---|---|---|
| V2.1 | 40/sec | 80/sec | per portfolio |
| V2 | 40/sec | 40/sec | per portfolio |

## Remaining quota headers

- Public: `Public-Ratelimit-Remaining`
- Private order APIs: `Private-Order-Ratelimit-Remaining`
- Private non-order APIs: `Private-Ratelimit-Remaining`

## Retry rules

- Safe to retry: idempotent public/private reads, websocket reconnect after disconnect, rate-limit after waiting
- Retry with caution: generic server-side failures like `405`, but only for idempotent reads
- Unsafe to blindly retry: order placement, order cancel, withdrawal, or any private state-changing call
- For uncertain private order submission, use `user_order_id` or follow-up lookup before retrying

## Common error payloads

### V2.1 / Public V2

```json
{
  "result": "error",
  "error_code": "105",
  "error_msg": "Price is not correct"
}
```

### V2 / Public V1

```json
{
  "result": "error",
  "errorCode": "105",
  "errorMsg": "Price is not correct"
}
```

## High-value error codes

| Code | Meaning | Typical action |
|---|---|---|
| 4 | Blocked user access | stop and escalate |
| 12 | Invalid access token | rotate/fix auth |
| 40 | Invalid API permission | check API key scopes |
| 50 / 52 | KYC or real-name verification missing | stop and escalate |
| 101 / 107 | Invalid format / parameter error | fix request |
| 103 / 157 | Insufficient balance | fix size or fund account |
| 104 | Order does not exist | verify identifiers |
| 105 | Price is not correct | validate tick size |
| 108 / 109 | Unknown currency / pair | fix symbols |
| 120-123 | Missing or invalid payload/signature | fix signing |
| 130 / 131 / 132 / 133 | Nonce invalid or reused | fix nonce strategy |
| 160 | Invalid transaction id | fix id |
| 161-167 | Order-type required field errors | fix order field matrix |
| 300 / 305 / 306 / 307 / 308 / 309 / 310 | Invalid order sizing or price unit | validate limits and range unit |
| 312 / 313 / 314 | `user_order_id` invalid or conflicting | fix idempotency strategy |
| 315 | API does not support portfolio | use supported key/context |
| 316 / 317 | Invalid range or size | fix pagination or query size |
| 1202 | Deprecated v2.1 order info only supports limit type | switch endpoint |
| 3001-3018 | Withdrawal restrictions | stop and inspect account/rules |

## WebSocket errors

- Error shape:

```json
{
  "response_type": "ERROR",
  "error_code": 160012,
  "message": "Invalid Topic"
}
```

- Known websocket close/error codes:
  - `4280`: private websocket auth failure
  - `4290`: too many websocket connections
  - `160010`: invalid request
  - `160011`: invalid type
  - `160012`: invalid topic
