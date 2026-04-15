# Coinone order safety

## Use this guide before any private order or cancel request

## Preferred endpoints

- Place order: `POST /v2.1/order`
- Cancel single order: `POST /v2.1/order/cancel`
- Cancel all for market: `POST /v2.1/order/cancel/all`
- Inspect fills/order detail: `POST /v2.1/order/detail`

## Order field matrix

| Type | Required fields | Notes |
|---|---|---|
| `LIMIT` | `side`, `quote_currency`, `target_currency`, `type`, `price`, `qty`, `post_only` | validate price unit first |
| `MARKET` buy | `side`, `quote_currency`, `target_currency`, `type`, `amount` | `amount` is total spend |
| `MARKET` sell | `side`, `quote_currency`, `target_currency`, `type`, `qty` | validate qty range |
| `STOP_LIMIT` | `side`, `quote_currency`, `target_currency`, `type`, `price`, `qty`, `trigger_price` | trigger price cannot equal current price |

## Preflight checklist

1. Confirm market exists with public market endpoints.
2. Fetch range units with `/public/v2/range_units/{quote_currency}/{target_currency}`.
3. Validate order price against the returned `price_unit`.
4. Validate `qty` / `amount` against market minimum and maximum constraints if available from response metadata.
5. Use uppercase enums: `BUY`, `SELL`, `LIMIT`, `MARKET`, `STOP_LIMIT`.
6. Prefer a lowercase `user_order_id` for recovery-safe flows.
7. Never send both `order_id` and `user_order_id` together for lookup/cancel endpoints.

## Common failures

- `161`: missing `price` for `LIMIT` or `STOP_LIMIT`
- `162`: missing `qty` for `LIMIT`, `STOP_LIMIT`, or `MARKET` sell
- `163`: missing `post_only` for `LIMIT`
- `164`: missing `trigger_price` for `STOP_LIMIT`
- `165`: missing `amount` for `MARKET` buy
- `166`: unsupported order type or wrong casing
- `167`: trigger price equals current price
- `310`: invalid price unit
- `312`: duplicated `user_order_id`
- `314`: invalid `user_order_id`, must be lowercase and valid length/charset

## Recovery plan for uncertain order submission

1. Do not immediately retry.
2. If `user_order_id` was sent, query by that identifier where supported.
3. Otherwise query order detail or active/open orders for the market.
4. Retry only after proving the original order was not accepted.
