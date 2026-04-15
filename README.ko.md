# coinone-api-skills

코인원 Open API 사용을 위한 스킬 모음입니다.

[English README](./README.md)

## 빠른 사용법

`SKILL.md` 와 `references/` 폴더를 스킬 디렉터리에 복사한 뒤, 코인원 API 작업 시 해당 스킬을 불러 사용하면 됩니다.

예시 프롬프트:

- `coinone-openapi 스킬을 사용해서 /v2.1/account/balance/all 서명 요청 예시를 만들어줘.`
- `coinone-openapi 스킬을 사용해서 KRW-BTC 지정가 매수 주문을 안전하게 넣는 방법을 설명해줘.`
- `coinone-openapi 스킬을 사용해서 MYORDER용 private websocket 재연결 전략을 설계해줘.`

## 포함된 파일

- `SKILL.md` — 메인 스킬 안내
- `references/endpoint-index.md` — 전체 엔드포인트 목록
- `references/auth-signing.md` — REST / WebSocket 인증 및 서명 규칙
- `references/rate-limits-and-errors.md` — 요청 제한, 헤더, 재시도 규칙, 에러 코드
- `references/order-safety.md` — 안전한 주문 처리 가이드
- `references/public-rest-v2.md` — Public API V2 가이드
- `references/private-rest-v21.md` — Private API V2.1 가이드
- `references/private-rest-v2-legacy.md` — 레거시 Private API V2 가이드
- `references/public-rest-v1-deprecated.md` — Deprecated Public API V1 참고 가이드
- `references/websocket.md` — Public / Private WebSocket 가이드

## 범위

- 기본 대상은 Public API V2 와 Private API V2.1 입니다.
- WebSocket 가이드를 포함합니다.
- Deprecated API 는 참고용으로만 유지합니다.

## 원문 문서

- https://docs.coinone.co.kr/docs
- https://docs.coinone.co.kr/reference/
- https://docs.coinone.co.kr/changelog

## 라이선스

MIT
