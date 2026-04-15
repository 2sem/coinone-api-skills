# Private REST V2.1

Base URL: `https://api.coinone.co.kr/v2.1`

## Shared rules

- Method: `POST`
- Auth: private signing required
- Nonce: UUID v4
- Request and response: `snake_case`

## Account and fee APIs

### find-balance
- Path: `/account/balance/all`
- Body: `access_token`, `nonce`
- Use for: all balances

### find-balance-by-currencies
- Path: `/account/balance`
- Body: `access_token`, `nonce`, `currencies`
- Use for: selected asset balances

### find-all-trade-fees
- Path: `/account/trade_fee`
- Body: `access_token`, `nonce`
- Use for: all fee rates

### find-trade-fee-by-pair
- Path: `/account/trade_fee/{quote_currency}/{target_currency}`
- Body: `access_token`, `nonce`
- Use for: fee rate for one market

## Order query APIs

### find-active-orders
- Path: `/order/active_orders`
- Body: `access_token`, `nonce`
- Optional: `quote_currency`, `target_currency`, `order_type`
- `order_type`: array of `LIMIT`, `STOP_LIMIT`; omit or send empty array for all supported types
- Use for: market-scoped active orders

### order-detail
- Path: `/order/detail`
- Body: `access_token`, `nonce`, `order_id`, `quote_currency`, `target_currency`, `user_order_id`
- Use for: order detail and fills
- Rule: send exactly one of `order_id` or `user_order_id`

### find-all-completed-orders
- Path: `/order/completed_orders/all`
- Body: `access_token`, `nonce`, `to_trade_id`, `size`, `from_ts`, `to_ts`
- Use for: completed orders across all markets

### find-completed-orders
- Path: `/order/completed_orders`
- Body: `access_token`, `nonce`, `to_trade_id`, `size`, `from_ts`, `to_ts`, `quote_currency`, `target_currency`
- Use for: completed orders by market

### find-all-open-orders
- Path: `/order/open_orders/all`
- Body: `access_token`, `nonce`
- Use for: all open orders
- Status: deprecated
- Note: docs provide only auth fields
- Limitation: docs say this endpoint does not support portfolio API usage

### find-open-orders
- Path: `/order/open_orders`
- Body: `access_token`, `nonce`, `quote_currency`, `target_currency`
- Use for: market-scoped open orders
- Status: deprecated
- Limitation: docs say this endpoint does not support portfolio API usage

### find-order-info
- Path: `/order/info`
- Body: `access_token`, `nonce`, `order_id`, `quote_currency`, `target_currency`
- Use for: specific order info
- Note: this endpoint is more limited than `order-detail`
- Status: deprecated
- Limitation: docs say this endpoint does not support portfolio API usage

## Order action APIs

### place-order
- Path: `/order`
- Body: `access_token`, `nonce`, `side`, `quote_currency`, `target_currency`, `type`, `price`, `qty`, `amount`, `post_only`, `limit_price`, `trigger_price`, `user_order_id`
- Use for: unified order placement
- Rule: only send fields required by the chosen order type

### cancel-orders
- Path: `/order/cancel/all`
- Body: `access_token`, `nonce`, `quote_currency`, `target_currency`
- Use for: cancel all orders for a market

### cancel-order
- Path: `/order/cancel`
- Body: `access_token`, `nonce`, `order_id`, `quote_currency`, `target_currency`, `user_order_id`
- Use for: cancel one order

### order-place-limit-order
- Path: `/order/limit`
- Body: `access_token`, `nonce`, `quote_currency`, `target_currency`, `side`, `price`, `qty`, `limit_order_type`
- Use for: deprecated limit-only placement
- Prefer: `place-order`

## Transaction APIs

### krw-transaction-history
- Path: `/transaction/krw/history`
- Body: `access_token`, `nonce`, `to_id`, `is_deposit`, `size`, `from_ts`, `to_ts`
- Use for: KRW transaction history

### coin-transaction-history
- Path: `/transaction/coin/history`
- Body: `access_token`, `nonce`, `currency`, `to_id`, `is_deposit`, `size`, `from_ts`, `to_ts`
- Use for: coin transaction history

### single-coin-transaction-history
- Path: `/transaction/coin/history/detail`
- Body: `access_token`, `nonce`, `id`
- Use for: single transaction lookup

### coin-withdrawal-limit
- Path: `/transaction/coin/withdrawal/limit`
- Body: `access_token`, `nonce`, `currency`
- Use for: withdrawal limits

### coin-withdrawal-address-book
- Path: `/transaction/coin/withdrawal/address_book`
- Body: `access_token`, `nonce`, `currency`
- Use for: withdrawal address book

### coin-withdrawal
- Path: `/transaction/coin/withdrawal`
- Body: `access_token`, `nonce`, `currency`, `amount`, `address`, `secondary_address`
- Use for: coin withdrawal
- Note: memo/tag-style chains may require `secondary_address`
- Safety: only whitelisted and verified withdrawal addresses are supported by the docs
- Limitation: docs say this endpoint does not support portfolio API usage

## Reward APIs

### order-reward-programs
- Path: `/event/order-reward/programs`
- Body: `access_token`, `nonce`
- Use for: reward-eligible markets

### order-reward-history
- Path: `/event/order-reward/history`
- Body: `access_token`, `nonce`, `from_ts`, `to_ts`
- Use for: reward history

## Notes

- Recent changelog entries added reward APIs, private websocket, and chart websocket support.
- Use UTC timestamps where docs require `from_ts` and `to_ts`.
