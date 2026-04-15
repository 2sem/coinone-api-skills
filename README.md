# coinone-api-skills

Skill pack for Coinone Open API usage.

[한국어 README](./README.ko.md)

## Install

Install with `npx skills`:

```bash
npx skills install 2sem/coinone-api-skills
```

If your setup prefers a GitHub URL:

```bash
npx skills install https://github.com/2sem/coinone-api-skills
```

If your local `skills` CLI uses a slightly different install syntax, use the equivalent repo install command for this repository.

## Use when

- You need Coinone Public API V2 guidance
- You need Coinone Private API V2.1 auth/signing help
- You need safe order placement rules
- You need Public or Private WebSocket integration guidance

## Quick use

After install, load the `coinone-openapi` skill when working with Coinone APIs.

Manual fallback: copy `SKILL.md` and the `references/` folder into your skill directory.

Example prompts:

- `Use the coinone-openapi skill and build a signed request for /v2.1/account/balance/all.`
- `Use the coinone-openapi skill and explain how to place a safe LIMIT BUY order for KRW-BTC.`
- `Use the coinone-openapi skill and design a reconnect-safe private websocket client for MYORDER.`

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

## License

MIT

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
