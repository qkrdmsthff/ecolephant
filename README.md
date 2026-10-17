# ecolephant

현재 단계는 **실제 웹캠을 켜고 영상을 확인하는 화면**입니다.
사용자 요청에 따라 자세 측정 AI 모델 연결은 비워 두었고, 측정 시작 버튼은 준비 중으로 표시합니다.

## 실행

Node 22.12+ · npm이 필요합니다. 저장소 루트에서 프론트만 실행할 수 있습니다.

```sh
npm ci
npm run dev:frontend
```

화면: `http://127.0.0.1:5173` → **카메라 켜기** → 브라우저 권한 허용.
Flask도 함께 실행하려면 Python 3.12+ 환경에서 `npm run setup`, `npm run dev`를 사용합니다.
설치된 Windows 환경은 [start-mvp.cmd](start-mvp.cmd)를 더블클릭해 실행할 수 있습니다.

## 현재 사용할 수 있는 기능

- 카메라 권한 요청, 실제 영상 표시, 켜기·끄기, 표시 좌우 반전.
- 권한 거부·장치 없음·사용 중 오류 안내와 재시도.
- 페이지 이동·탭 비활성화·장치 연결 종료 때 카메라 해제.
- AI 모델 연결 대기 화면. 미리보기에서는 측정·알림·결과 저장을 시작하지 않습니다.

영상·사진·음성을 저장하거나 서버에 전송하지 않습니다. 마이크 권한은 요청하지 않습니다.
기존 데모 분석·세션 API·기록 코드는 남아 있으며 현재 카메라 화면과는 연결하지 않았습니다.

## 안내

- [카메라 사용 안내](docs/development/camera-preview.md)
- [완료·미완료 현황](docs/development/mvp-status.md)
- [실행 안내](docs/development/local.md)
- [작업 하네스](harness/NAVIGATOR.md)
- [제품 요구](PRD.md) · [아키텍처](ARCHITECTURE.md)
