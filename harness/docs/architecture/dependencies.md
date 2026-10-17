# 제품 폴더의 의존 방향

`frontend`는 분석을 위해 `ai`를 사용합니다. `backend`와는 HTTP 계약으로 통신합니다. `ai`는 화면·저장소·네트워크에 의존하지 않습니다.

| 출발 폴더 | 허용하는 다른 제품 폴더 |
|---|---|
| frontend | ai |
| ai | 없음 |
| backend | 없음 |

같은 폴더 내부 의존은 허용합니다. 타사 라이브러리는 별도 기술 선택에 따릅니다. [정책 파일](../../metadata/architecture-policy.json)과 [구조 검사](../../scripts/checks/architecture.py)는 명시적인 Python·JS/TS import와 ai의 직접 I/O 패턴을 점검합니다.

현재 제품 실행 코드는 없습니다. 이 검사는 앞으로의 최소 경계 검사이며 빌드 도구의 별칭·동적 로딩 전체를 증명하지 않습니다. 스택 선택 시 실제 의존 검사로 확장합니다.
