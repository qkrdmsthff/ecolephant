# 계약 변경의 검증 항목

HTTP 필드의 기준은 [OpenAPI](../../../docs/api/openapi.json), 도우미 메시지는 [Schema](../../../docs/api/helper-message.schema.json)입니다.

필수값·범위·null·추가 필드·인증·오류와 함께 중복·순번·연속성·종료·집계의 불변식을 확인합니다. 유효 예시뿐 아니라 원본 필드·단위 혼동·시간 겹침·비율 오류의 거부 예시도 갱신합니다.

[계약 검사](../../scripts/checks/contracts.py)와 [의미 검사](../../scripts/checks/semantics.py)는 합성 fixture를 검증합니다. 실제 DB 원자성·인증·네트워크 실행은 제품 인수 시나리오에 남깁니다.
