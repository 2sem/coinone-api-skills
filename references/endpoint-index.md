# Coinone endpoint index

## Docs pages

- Docs home: `https://docs.coinone.co.kr/docs`
- Reference: `https://docs.coinone.co.kr/reference/`
- Changelog: `https://docs.coinone.co.kr/changelog`

## Public REST V2

| Guide | Method | Path | Purpose |
|---|---|---|---|
| range-unit | GET | `/public/v2/range_units/{quote_currency}/{target_currency}` | Price tick units for a market |
| markets | GET | `/public/v2/markets/{quote_currency}` | All markets under a quote currency |
| market | GET | `/public/v2/markets/{quote_currency}/{target_currency}` | Single market info |
| orderbook | GET | `/public/v2/orderbook/{quote_currency}/{target_currency}` | Orderbook snapshot |
| recent-completed-orders | GET | `/public/v2/trades/{quote_currency}/{target_currency}` | Recent public trades |
| tickers | GET | `/public/v2/ticker_new/{quote_currency}` | All tickers |
| ticker | GET | `/public/v2/ticker_new/{quote_currency}/{target_currency}` | Single ticker |
| utc-tickers | GET | `/public/v2/ticker_utc_new/{quote_currency}` | All tickers in UTC view |
| utc-ticker | GET | `/public/v2/ticker_utc_new/{quote_currency}/{target_currency}` | Single UTC ticker |
| currencies | GET | `/public/v2/currencies` | All asset metadata |
| currency | GET | `/public/v2/currencies/{currency}` | Single asset metadata |
| chart | GET | `/public/v2/chart/{quote_currency}/{target_currency}` | Candle chart data |

## Private REST V2.1

| Guide | Method | Path | Purpose |
|---|---|---|---|
| find-balance | POST | `/v2.1/account/balance/all` | All balances |
| find-balance-by-currencies | POST | `/v2.1/account/balance` | Balance by selected currencies |
| find-all-trade-fees | POST | `/v2.1/account/trade_fee` | All trade fees |
| find-trade-fee-by-pair | POST | `/v2.1/account/trade_fee/{quote_currency}/{target_currency}` | Fee for one market |
| find-active-orders | POST | `/v2.1/order/active_orders` | Active orders by market |
| order-detail | POST | `/v2.1/order/detail` | Order detail with fills |
| find-all-completed-orders | POST | `/v2.1/order/completed_orders/all` | Completed orders across all markets |
| find-completed-orders | POST | `/v2.1/order/completed_orders` | Completed orders by market |
| find-all-open-orders | POST | `/v2.1/order/open_orders/all` | Deprecated open-order lookup; no portfolio support |
| find-open-orders | POST | `/v2.1/order/open_orders` | Deprecated market open-order lookup; no portfolio support |
| find-order-info | POST | `/v2.1/order/info` | Deprecated specific order info; no portfolio support |
| place-order | POST | `/v2.1/order` | Unified order placement |
| cancel-orders | POST | `/v2.1/order/cancel/all` | Cancel all orders for a market |
| cancel-order | POST | `/v2.1/order/cancel` | Cancel one order |
| order-place-limit-order | POST | `/v2.1/order/limit` | Deprecated limit-only placement |
| krw-transaction-history | POST | `/v2.1/transaction/krw/history` | KRW deposit/withdraw history |
| coin-transaction-history | POST | `/v2.1/transaction/coin/history` | Coin deposit/withdraw history |
| single-coin-transaction-history | POST | `/v2.1/transaction/coin/history/detail` | Single coin transaction lookup |
| coin-withdrawal-limit | POST | `/v2.1/transaction/coin/withdrawal/limit` | Coin withdrawal limits |
| coin-withdrawal-address-book | POST | `/v2.1/transaction/coin/withdrawal/address_book` | Coin withdrawal address book |
| coin-withdrawal | POST | `/v2.1/transaction/coin/withdrawal` | Coin withdrawal; no portfolio support |
| order-reward-programs | POST | `/v2.1/event/order-reward/programs` | Reward-eligible markets |
| order-reward-history | POST | `/v2.1/event/order-reward/history` | Reward history |

## WebSocket

| Guide | Transport | Endpoint | Purpose |
|---|---|---|---|
| public-websocket | WS | `wss://stream.coinone.co.kr` | Public streaming overview |
| public-websocket-ping | WS | `wss://stream.coinone.co.kr` | Keepalive |
| public-websocket-orderbook | WS | `wss://stream.coinone.co.kr` | Orderbook stream |
| public-websocket-ticker | WS | `wss://stream.coinone.co.kr` | Ticker stream |
| public-websocket-trade | WS | `wss://stream.coinone.co.kr` | Trade stream |
| public-websocket-chart | WS | `wss://stream.coinone.co.kr` | Chart stream |
| private-websocket | WS | `wss://stream.coinone.co.kr/v1/private` | Private streaming overview |
| private-websocket-ping | WS | `wss://stream.coinone.co.kr/v1/private` | Keepalive |
| private-websocket-myorder | WS | `wss://stream.coinone.co.kr/v1/private` | Order update stream |
| private-websocket-myasset | WS | `wss://stream.coinone.co.kr/v1/private` | Asset update stream |

## Legacy Private REST V2

| Guide | Method | Path | Purpose |
|---|---|---|---|
| balance | POST | `/v2/account/balance` | All balances |
| deposit-address | POST | `/v2/account/deposit_address` | Deposit addresses |
| user-information | POST | `/v2/account/user_info` | User info |
| virtual-account | POST | `/v2/account/virtual_account` | Virtual account info |
| my-complete-orders | POST | `/v2/order/complete_orders` | Completed orders |
| my-limit-orders | POST | `/v2/order/limit_orders` | Open limit orders |
| my-order-information | POST | `/v2/order/query_order` | Specific order info |
| cancel-order-1 | POST | `/v2/order/cancel` | Cancel one order |
| limit-buy | POST | `/v2/order/limit_buy` | Deprecated limit buy |
| limit-sell | POST | `/v2/order/limit_sell` | Deprecated limit sell |
| coin-transaction-history-1 | POST | `/v2/transaction/history` | Coin deposit/withdraw history |
| krw-transaction-history-1 | POST | `/v2/transaction/krw/history` | KRW deposit/withdraw history |

## Deprecated Public REST V1

- Guide: `references/public-rest-v1-deprecated.md`
- `/orderbook`
- `/ticker`
- `/ticker_utc`
- `/trades`

Use only when the caller explicitly asks for deprecated behavior.
