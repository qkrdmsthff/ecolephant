# 작은 문서로 구성한 개발 하네스

작업별로 필요한 짧은 문서를 찾아 설계·구현·검토하고, 같은 규칙을 독립 검사로 확인합니다. 구조는 [참고 저장소 적용 기록](docs/references/harness-pattern.md)에 정리했습니다.

## 시작

1. [작업 내비게이터](NAVIGATOR.md)를 고릅니다.
2. [하네스 지식 색인](docs/index.md)에서 관련 주제를 읽습니다.
3. [역할별 확인](docs/roles/index.md)과 [변경 절차](docs/workflows/change.md)를 적용합니다.
4. 검사하고 [검증 기록 템플릿](docs/templates/verification.md)에 결과를 남깁니다.

## 폴더

[구조 지도](ARCHITECTURE.md)는 각 폴더의 책임을, [생성 문서 지도](generated/document-map.md)는 전체 문서 위치를 보여줍니다. 제품 명세는 [루트 docs](../docs/index.md)에 연결됩니다.

## 실행

검사 환경 설치는 [루트 README](../README.md)를 따릅니다.

```powershell
.\harness\scripts\check.ps1 -PythonPath .\.venv\Scripts\python.exe
.\harness\scripts\doc-gardening.ps1 -PythonPath .\.venv\Scripts\python.exe
```

Python 진입점과 단일 검사 실행은 [검사 안내](scripts/README.md)를 참고합니다. GitHub에서는 [CI 정의](../.github/workflows/harness.yml)가 같은 검사와 회귀 사례를 실행하도록 구성됩니다.

문서·계약 검사와 실제 제품 검증의 범위는 [품질 게이트](docs/quality/gates.md)에 있습니다. 기록은 [최초 작성](reports/docs-bootstrap.md), [이번 구조 정리](reports/harness-restructure.md)에서 확인합니다.
