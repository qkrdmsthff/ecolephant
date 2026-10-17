# 참고 하네스의 적용 범위

참고: [maxoverpro/harness](https://github.com/maxoverpro/harness/tree/3fb79f98c0b4f6b2843df55c82ea020a06f3b3b2), 확인일 2026-10-17.

짧은 진입점, 주제별 지식, 역할별 검토, active/completed 계획, 기술 부채, 독립 검사, 문서 정비 구조를 참고했습니다. 설명과 검사 코드는 이 제품의 브라우저 분석·결과 저장 경계에 맞게 작성했습니다.

| 참고 요소 | 이 저장소 적용 |
|---|---|
| 짧은 AGENTS와 지식 색인 | harness/AGENTS, NAVIGATOR, docs/index |
| 역할별 책임 | docs/roles의 도구 중립 점검 문서 |
| 계획과 품질 추적 | docs/plans, docs/quality |
| 독립 검사와 문서 정비 | scripts/checks, doc gardening, tests |
| GitHub 검사 | 루트 .github/workflows/harness.yml |

GitHub Actions 구성은 [checkout](https://github.com/actions/checkout)과 [setup-python](https://github.com/actions/setup-python)의 공식 사용법도 확인했습니다. 현재 제품에는 범용 계층 전체를 일괄 강제하지 않고 실제 폴더 의존을 [구조 정책](../../metadata/architecture-policy.json)으로 표현합니다.
