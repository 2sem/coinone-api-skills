# Coinone auth and signing

## Public REST

- No auth
- `GET`
- Send `accept: application/json`

## Private REST

### Common rules

- Method: `POST`
- Content-Type: `application/json`
- Required headers:
  - `X-COINONE-PAYLOAD`
  - `X-COINONE-SIGNATURE`
- Signing algorithm: `HMAC-SHA512`
- Signature input: Base64-encoded JSON payload bytes

### Payload creation

1. Build a JSON object including `access_token` and request fields.
2. Add `nonce`.
3. JSON-encode the object.
4. Base64-encode the JSON string.
5. Put the Base64 result in `X-COINONE-PAYLOAD`.
6. Sign that Base64 value with the raw secret key bytes using HMAC-SHA512.
7. Put the lowercase hex digest in `X-COINONE-SIGNATURE`.

### Nonce rules

- `Private API V2.1`: UUID v4 string
- `Private API V2`: strictly increasing positive integer

### Minimal private REST example

```json
{
  "access_token": "<redacted>",
  "nonce": "550e8400-e29b-41d4-a716-446655440000",
  "quote_currency": "KRW",
  "target_currency": "BTC"
}
```

## Private WebSocket auth

- Connect to: `wss://stream.coinone.co.kr/v1/private`
- Send auth during handshake with:
  - `X-COINONE-PAYLOAD`
  - `X-COINONE-SIGNATURE`
- Payload uses the same HMAC-SHA512 flow as private REST
- Private WS auth payload must include:
  - `access_token`
  - `nonce` as UUID v4
  - `timestamp` in milliseconds

## Security policy

### IP registration requirement

- API calls only allowed from pre-registered IP addresses
- Maximum 5 IP addresses can be registered per API key
- Unregistered IP addresses will be blocked

### API Key expiration

- All API keys have 1-year validity period
- Expired keys cannot be extended and must be deleted
- New key generation required after expiration

## Safety rules

- Never print the secret key
- Never print full signed headers in logs
- Mask `access_token`, payload, and signature in examples
- If auth fails, check: nonce format, secret bytes, payload base64, header names, and version mismatch
