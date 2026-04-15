# Public REST V2

Base URL: `https://api.coinone.co.kr/public/v2`

## Shared rules

- Method: `GET`
- Auth: none
- Response uses `snake_case`

## Endpoints

### range-unit
- Path: `/range_units/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Use for: tick-size validation before limit-style orders

### markets
- Path: `/markets/{quote_currency}`
- Params: `quote_currency`
- Use for: list all markets under one quote currency

### market
- Path: `/markets/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Use for: single market info

### orderbook
- Path: `/orderbook/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Query: `size`, `order_book_unit`
- `size`: `5`, `10`, `15`, `16` (default `15`)
- Use for: orderbook snapshot with configurable depth/unit

### recent-completed-orders
- Path: `/trades/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Query: `size`
- `size`: `10`, `50`, `100`, `150`, `200` (default `200`)
- Use for: recent public trades

### tickers
- Path: `/ticker_new/{quote_currency}`
- Params: `quote_currency`
- Query: `additional_data`
- Use for: all tickers in a quote currency market

### ticker
- Path: `/ticker_new/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Query: `additional_data`
- Use for: one ticker

### utc-tickers
- Path: `/ticker_utc_new/{quote_currency}`
- Params: `quote_currency`
- Query: `additional_data`
- Use for: all tickers with UTC-based view

### utc-ticker
- Path: `/ticker_utc_new/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Query: `additional_data`
- Use for: one UTC ticker

### currencies
- Path: `/currencies`
- Params: none
- Use for: full asset metadata set

### currency
- Path: `/currencies/{currency}`
- Params: `currency`
- Use for: one asset metadata record

### chart
- Path: `/chart/{quote_currency}/{target_currency}`
- Params: `quote_currency`, `target_currency`
- Query: `interval`, `timestamp`, `size`
- `interval`: `1m`, `3m`, `5m`, `10m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `1d`, `1w`, `1mon`
- `size`: `1...500` (default `200`)
- Use for: candle chart data

## Response notes

- Success envelope commonly includes `result` and `error_code`
- Prices and sizes may be numeric strings; preserve precision
