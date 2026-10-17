# 하네스 작업 안내

- [NAVIGATOR](NAVIGATOR.md)에서 작업을 선택하고 [지식 색인](docs/index.md)에서 한 주제씩 읽습니다.
- 제품 요구는 [루트 PRD](../PRD.md), HTTP 필드는 [OpenAPI](../docs/api/openapi.json), 작업 규칙은 이 하네스가 안내합니다.
- 역할은 [역할별 점검](docs/roles/index.md)에서 선택합니다. 한 작업자가 순서대로 수행할 수 있습니다.
- 여러 경계가 바뀌면 [계획 규칙](docs/plans/index.md)과 [작업 템플릿](docs/templates/task.md)을 사용합니다.
- 문서 한 개에는 한 주제를 두고 80줄 이내로 유지합니다. 긴 목록·계약은 metadata·fixture·정식 명세로 연결합니다.
- 새 Markdown은 상위 색인과 [문서 목록](metadata/documents.json)에 등록합니다.
- 경로 변경 시 링크·추적표·manifest·문서 목록을 함께 갱신합니다.
- [검사 안내](scripts/README.md)에 따라 `scripts/check.ps1`을 실행합니다.
- 반복되는 규칙은 독립 검사 모듈과 회귀 사례로 관리합니다.
- 별도 에이전트 실행·메시지·커밋·푸시·배포의 권한은 사용자의 해당 작업 지시를 따릅니다.
