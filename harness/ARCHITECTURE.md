# 하네스 지식과 검사 구조

| 경로 | 책임 |
|---|---|
| AGENTS.md·NAVIGATOR.md | 짧은 규칙과 작업별 진입점 |
| docs | 주제별 지식과 역할·작업 규칙 |
| metadata | 필수 파일·문서 검토일·요구사항 추적 |
| fixtures | 정책·HTTP·도우미·인수 계획의 합성 데이터 |
| scripts/checks | 지도·링크·계약·구조·비밀정보·신선도 검사 |
| tests | 검사기가 실제 결함을 거부하는 회귀 사례 |
| reports | 실행한 검사의 범위와 결과 |
| generated | 문서 지도 생성물 |

흐름은 작업 지도 → 주제 문서 → 정식 계약·fixture → 검사 → 실행 기록입니다. [제품 아키텍처](../ARCHITECTURE.md)의 센서·저장 경계는 해당 정식 문서를 기준으로 합니다.

검사 모듈은 [common](scripts/checks/common.py)을 통해 저장소 경로·파일 조회를 공유합니다. 진입점은 검사 실패를 모아 반환하며 제품 코드나 네트워크를 실행하지 않습니다. [구조 정책](metadata/architecture-policy.json)은 제품 폴더 간 의존과 분석 모듈의 I/O 경계를 표현합니다.
