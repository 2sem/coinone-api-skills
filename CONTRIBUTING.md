# Contributing

Thanks for contributing to `coinone-api-skills`.

## Scope

This repository maintains a reusable skill pack for Coinone Open API usage.

Please keep contributions:

- concise
- accurate to the official Coinone docs
- safe for real trading and withdrawal workflows
- biased toward Public API V2 and Private API V2.1

## Before submitting changes

Check updates against:

- https://docs.coinone.co.kr/docs
- https://docs.coinone.co.kr/reference/
- https://docs.coinone.co.kr/changelog

## Contribution rules

- Prefer current APIs over deprecated ones
- Clearly mark deprecated or no-portfolio endpoints
- Do not add speculative parameters or undocumented behavior
- Keep security guidance strict: never encourage exposing secrets or blindly retrying state-changing calls
- Keep examples minimal and reusable

## Recommended pull request checklist

- [ ] Endpoint list is still complete
- [ ] Parameters and enums match the live docs
- [ ] Auth/signing guidance is still correct
- [ ] Rate limits and error handling are still correct
- [ ] Deprecated endpoint warnings are still explicit
- [ ] README is updated if installation or usage changed

## Release notes

If Coinone changes the docs materially, include a short summary of what changed and which reference files were updated.
