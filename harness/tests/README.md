# 검사기 회귀 사례

의존 역류·분석 I/O·비밀정보 패턴·너무 긴 문서·검토일·깨진 Schema 참조를 실제로 주입해 탐지 여부를 확인합니다. 임시 폴더의 합성 코드만 정적으로 검사하며 해당 코드를 실행하지 않습니다.

임시 입력은 저장소의 무시된 tmp/harness-tests 아래 고유 폴더에 생성합니다. 정리 전 경로가 이 저장소 안에 있는지 확인합니다.

전체 검사의 self-tests 항목 또는 다음 명령으로 실행합니다.

```text
python -m unittest discover -s harness/tests -p "test_*.py"
```

제품 판정·장치·정확도 검증은 [인수 시나리오](../../docs/quality/acceptance.md)에 있습니다.
