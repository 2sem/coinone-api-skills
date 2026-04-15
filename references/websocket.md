# Coinone WebSocket

## Endpoints

- Public: `wss://stream.coinone.co.kr`
- Private: `wss://stream.coinone.co.kr/v1/private`

## Important doc note

- One private websocket example shows `/private`.
- Prefer `/v1/private`, which is the primary documented endpoint.

## Shared rules

- All messages are JSON
- `request_type`, `channel`, and `format` must be uppercase
- `format` can be omitted, `DEFAULT`, or `SHORT`
- Send app-level `PING` regularly; do not rely only on websocket control frames

## Generic request shapes

### Ping

```json
{
  "request_type": "PING"
}
```

### Public subscribe

```json
{
  "request_type": "SUBSCRIBE",
  "channel": "ORDERBOOK",
  "topic": {
    "quote_currency": "KRW",
    "target_currency": "BTC"
  },
  "format": "SHORT"
}
```

### Private subscribe (MYORDER)

```json
{
  "request_type": "SUBSCRIBE",
  "channel": "MYORDER",
  "topic": [
    {
      "quote_currency": "KRW",
      "target_currency": "BTC"
    }
  ]
}
```

### Private subscribe (MYASSET)

```json
{
  "request_type": "SUBSCRIBE",
  "channel": "MYASSET"
}
```

## Public channels

### public-websocket
- Auth: none
- Limit: max 20 connections per IP
- Idle close: 30 minutes without PING

### public-websocket-ping
- Request: `PING`
- Response: `PONG`

### public-websocket-orderbook
- Channel: `ORDERBOOK`
- Topic: `quote_currency`, `target_currency`
- Note: first message is current snapshot, then updates
- Core fields: ask/bid levels, each with price and qty; `SHORT` format abbreviates field names

### public-websocket-ticker
- Channel: `TICKER`
- Topic: `quote_currency`, `target_currency`
- Core fields: `quote_currency`, `target_currency`, last price, high, low, volume, value, best ask, best bid, UTC timestamps

### public-websocket-trade
- Channel: `TRADE`
- Topic: `quote_currency`, `target_currency`
- Core fields: trade id, price, qty, timestamp, `is_seller_maker`

### public-websocket-chart
- Channel: `CHART`
- Topic: `quote_currency`, `target_currency`, `interval`
- Intervals: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `1d`, `1w`
- Core fields: interval, open/high/low/close, volume, quote volume, start/end timestamps

## Private channels

### private-websocket
- Auth: handshake headers required
- Limit: max 20 connections per account
- Idle close: 30 minutes without PING

### private-websocket-ping
- Request: `PING`
- Response: `PONG`

### private-websocket-myorder
- Channel: `MYORDER`
- Topic: array of `{ quote_currency, target_currency }`
- Note: status values documented as `wait`, `watch`, `not_triggered`, `trade`, `trade_done`, `cancel`, `cancel_post_only`
- Side enum: `BID` or `ASK`
- Common fields: `order_id`, `user_order_id`, `type`, `side`, `status`, `price`, `qty`, `filled_qty`, `remain_qty`, `avg_price`, timestamps

### private-websocket-myasset
- Channel: `MYASSET`
- Topic: none
- Common fields: asset list with `currency`, `available`, `limit`; event payload also includes change `type` and `timestamp`

## Connection lifecycle

- Connected message includes a `session_id`
- Subscribe acknowledgment uses `SUBSCRIBED`
- Data frames use `DATA`
- `SHORT` format uses short keys like `r`, `c`, `d`
- Reconnect and resubscribe after disconnects or planned updates

## Error and close codes

- `4280`: private auth failure
- `4290`: too many connections
- `160010`: invalid request
- `160011`: invalid type
- `160012`: invalid topic
