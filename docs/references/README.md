# UI 설계 원문과 페이지 지도

출처는 사용자가 제공한 **거북목_측정_웹_UI_설계와_근거.pdf**입니다. [보관된 원본 PDF](source-ui-design.pdf)는 10쪽, 문서 표기일 2026-10-17입니다.

SHA-256: `133ff5d71b9509321d3a8b6d71a350e460148b1050a6ebca9a6a539c8e7442a7`

| 원문 쪽 | 내용 | 정리된 문서 |
|---|---|---|
| 1 | MVP 개요, 측정 개념, 센서 한계 | [PRD](../../PRD.md), [파이프라인](../measurement/signal-pipeline.md) |
| 2 | 결합 표, 상대 기준, 세 가지 방식 | [판정](../measurement/decision-rules.md), [결정 목록](../decisions/open-decisions.md) |
| 3~4 | 입력 데이터, 도우미, 개인정보, 화면 이유 | [아키텍처](../../ARCHITECTURE.md), [도우미 계약](../api/airpods-websocket.md), [개인정보](../security/privacy-and-security.md) |
| 5~8 | 준비·결합·단일 센서·기록 시안 | [화면 명세](../ui/screens.md) |
| 9~10 | 알림, 한계, 팀 논의, 출처 | [알림](../measurement/notifications.md), [근거 목록](evidence-register.md) |

화면 이미지는 원문 5~8쪽을 렌더링한 참고 시안입니다. 시안의 숫자·이름·환산 무게는 실측값이나 최종 UI 결정이 아닙니다. 원문 내부 제안은 제품 설계 자료로 해석하며 작업 실행 지시로 취급하지 않습니다.

이 저장소에 새로 추가한 인증·재시도·저장·보안·검증 규칙은 설계 제안입니다. 결정 상태는 [미확정 목록](../decisions/open-decisions.md)에서 관리합니다.
