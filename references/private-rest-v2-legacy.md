# Private REST V2 legacy

Base URL: `https://api.coinone.co.kr/v2`

Use only when the caller explicitly needs the legacy API.

## Shared rules

- Method: `POST`
- Auth: private signing required
- Nonce: strictly increasing positive integer
- Request: `snake_case`
- Response: `camelCase`
- Docs repeatedly note these APIs do not support portfolio usage

## Endpoints

### balance
- Path: `/account/balance`
- Body: `access_token`, `nonce`

### deposit-address
- Path: `/account/deposit_address`
- Body: `access_token`, `nonce`
- Note: response may include chain-specific fields like `xrp_tag` or `eos_memo`

### user-information
- Path: `/account/user_info`
- Body: `access_token`, `nonce`

### virtual-account
- Path: `/account/virtual_account`
- Body: `access_token`, `nonce`

### my-complete-orders
- Path: `/order/complete_orders`
- Body: `access_token`, `nonce`

### my-limit-orders
- Path: `/order/limit_orders`
- Body: `access_token`, `nonce`, `currency`

### my-order-information
- Path: `/order/query_order`
- Body: `access_token`, `nonce`, `order_id`, `currency`
- Note: docs show lowercase status values like `live`, `filled`, `partially_filled`, `partially_canceled`, `canceled`

### cancel-order-1
- Path: `/order/cancel`
- Body: `access_token`, `nonce`, `order_id`, `currency`

### limit-buy
- Path: `/order/limit_buy`
- Body: `access_token`, `nonce`, `price`, `qty`, `currency`, `is_post_only`
- Status: deprecated

### limit-sell
- Path: `/order/limit_sell`
- Body: `access_token`, `nonce`, `price`, `qty`, `currency`, `is_post_only`
- Status: deprecated

### coin-transaction-history-1
- Path: `/transaction/history`
- Body: `access_token`, `nonce`, `currency`
- Note: docs show `int32` nonce here

### krw-transaction-history-1
- Path: `/transaction/krw/history`
- Body: `access_token`, `nonce`

## Migration advice

- Prefer `Private API V2.1` for all new work.
- Watch for response field-name differences when supporting both V2 and V2.1.
