# Ecolephant 자세 측정 웹 MVP

노트북 웹캠과 선택적인 AirPods 모션 입력으로 자세 습관을 확인하는 웹 MVP입니다. 이 저장소에는 구현을 시작하기 위한 제품 문서, API 계약, 작업 하네스가 있습니다. 애플리케이션과 센서 연동은 아직 구현되지 않았습니다.

## 읽는 순서

1. [제품 범위와 완료 기준](PRD.md)
2. [시스템 구조와 폴더 책임](ARCHITECTURE.md)
3. [전체 문서 색인](docs/index.md)
4. [작업별 문서 안내](harness/NAVIGATOR.md)
5. [미확정 결정](docs/decisions/open-decisions.md)과 [구현 순서](harness/docs/plans/mvp-roadmap.md)

## 저장소 구성

| 경로 | 책임 |
|---|---|
| [frontend](frontend/README.md) | 준비·측정·기록 화면, 카메라 수명주기, 브라우저 내 분석 실행 |
| [ai](ai/README.md) | 관측값 정규화, 보정, 판정, 시간 조건을 다루는 분석 모듈 |
| [backend](backend/README.md) | 소유자별 세션·측정 결과 저장, 집계, 조회·삭제 API |
| [docs](docs/index.md) | 요구사항, 화면, 판정, 통신, 데이터, 보안, 검증 기준 |
| [harness](harness/README.md) | 작업 절차, 요구사항 추적, 샘플 데이터, 문서·계약 검사 |

## 문서 상태

초안 0.1 · 기준일 2026-10-17. 요구사항은 [사용자 제공 PDF](docs/references/README.md)에서 추출했습니다. 추가한 구현 규칙은 **설계 제안**, 미정 사항은 `DEC-xxx`, 실측이 필요한 항목은 **검증 대기**로 표시합니다. 초안 수치가 정확도 검증이나 팀 승인을 의미하지 않습니다.

## 문서와 계약 검사

Python 3.10 이상과 PowerShell에서 실행합니다. 이 환경은 문서 검사만 수행합니다.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r harness/requirements-check.txt
.\harness\scripts\check.ps1 -PythonPath .\.venv\Scripts\python.exe
```

다른 운영체제에서는 가상환경의 Python으로 `python harness/scripts/check.py`를 실행합니다. 검사 범위와 해석은 [하네스 안내](harness/README.md)를 따릅니다.
