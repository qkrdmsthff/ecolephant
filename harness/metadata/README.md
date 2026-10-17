# 파일과 문서와 요구사항 지도

| 파일 | 관리하는 것 |
|---|---|
| manifest.json | 필수 파일과 원본 PDF 해시 |
| documents.json | 문서 경로·상태·담당 역할·실제 검토일·내용 해시 |
| traceability.json | REQ·명세·AC·API 동작의 연결 |
| docs-policy.json | 짧은 문서·주제 색인·검토 간격 |
| architecture-policy.json | 제품 폴더 의존과 분석 모듈 I/O 경계 |
| migration.json | 이번 경로 변경과 참고 저장소 버전 |

manifest와 문서 목록은 [생성기](../scripts/build_catalog.py)로 갱신합니다. 검토일은 실제 검토한 날짜를 사용합니다. 내용 해시 변화는 문서 재검토 안내로 표시합니다.
