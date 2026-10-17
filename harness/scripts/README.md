# 독립 검사 실행 안내

환경 설치는 [루트 README](../../README.md)를 따릅니다. 전체 검사는 check.ps1 또는 check.py로 실행합니다.

```powershell
.\harness\scripts\check.ps1 -PythonPath .\.venv\Scripts\python.exe
```

```text
python harness/scripts/check.py --only map
python harness/scripts/check.py --only contracts
python harness/scripts/check.py --only architecture
python harness/scripts/check.py --only secrets
python harness/scripts/doc_gardening.py --as-of 2026-10-17
python harness/scripts/build_catalog.py
```

| 모듈 | 확인 내용 |
|---|---|
| manifest·map·links | 파일·주제·짧은 문서·경로 |
| traceability·policy | 요구·시나리오·API 연결과 예시 정책 |
| contracts·semantics | 표준 형식과 합성 입력의 수락·거부 |
| architecture | 명시적 import·분석 모듈 직접 I/O |
| secrets | 커밋 후보 텍스트의 강한 비밀정보 패턴 |
| ci | GitHub 검사 정의의 기본 형식·권한 |
| freshness | 검토일 누락·기간 초과 안내 |
| self-tests | 검사기의 결함 탐지 회귀 사례 |

build_catalog는 검토 날짜를 자동 갱신하지 않습니다. 새 문서는 reviewed_on=null로 등록하고 실제 검토 후 metadata/documents.json에 날짜를 기록합니다. [지도 생성물](../generated/README.md)과 [문서 정비](../docs/quality/freshness.md)를 함께 참고합니다.
