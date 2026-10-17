# HTTP 계약의 유효값과 거부값

[contract-cases.json](contract-cases.json)의 valid는 Schema 기대 결과, semantics_valid는 추가 불변식 기대 결과입니다. 형식이 맞아도 비율·시간·중복·종료 상태가 잘못되면 의미 검사에서 거부합니다.

각 case는 합성 입력입니다. 정책 승인·인증·실제 서버 실행을 뜻하지 않습니다. 기준은 [OpenAPI](../../../docs/api/openapi.json)입니다.
