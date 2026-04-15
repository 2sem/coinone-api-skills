# coinone-api-skills

Skill pack for Coinone Open API usage.

[한국어 README](./README.ko.md)

## Included

- `SKILL.md` — main reusable skill instructions
- `references/endpoint-index.md` — endpoint inventory
- `references/auth-signing.md` — REST and WebSocket auth/signing rules
- `references/rate-limits-and-errors.md` — limits, headers, retry rules, errors
- `references/order-safety.md` — safe order workflow
- `references/public-rest-v2.md` — Public API V2 guide
- `references/private-rest-v21.md` — Private API V2.1 guide
- `references/private-rest-v2-legacy.md` — legacy Private API V2 guide
- `references/public-rest-v1-deprecated.md` — deprecated Public API V1 fallback guide
- `references/websocket.md` — public/private websocket guide

## Scope

- Defaults to Public API V2 and Private API V2.1
- Includes WebSocket guidance
- Keeps deprecated endpoints available as fallback reference only

## Source docs

- https://docs.coinone.co.kr/docs
- https://docs.coinone.co.kr/reference/
- https://docs.coinone.co.kr/changelog

## Notes

- Private request signing uses `X-COINONE-PAYLOAD` and `X-COINONE-SIGNATURE`
- `V2.1` uses UUID nonce
- legacy `V2` uses increasing integer nonce
- order placement should validate price units before submit
