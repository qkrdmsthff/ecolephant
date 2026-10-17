# 로컬 실행 안내

## 기본 실행

Node 22.12+ · npm · Python 3.12+가 필요합니다. 저장소 루트에서 실행합니다.

```sh
npm ci
npm run setup
npm run dev
```

Python을 못 찾으면 `npm run setup -- --python "Python 실행 파일의 절대 경로"`를 사용합니다.
setup은 `.venv`, `.data`, `backend/.env`, `frontend/.env.local`을 만들고 API 타입을 생성합니다.
기존 환경 파일과 저장 기록을 덮어쓰지 않습니다. 로컬 토큰이 달라졌다면 두 환경 파일을 같은 값으로 맞춘 뒤 재시작합니다.
이 파일과 디렉터리는 Git에서 제외되며 개인 장치에서만 사용합니다.

- 화면: `http://127.0.0.1:5173`
- 백엔드: `http://127.0.0.1:5000`
- Windows 실행: 설치 후 [start-mvp.cmd](../../start-mvp.cmd)를 더블클릭할 수 있습니다.
- 중지: 실행한 터미널의 Ctrl+C.
- SQLite: `.data/ecolephant.sqlite3`, 서버를 재시작해도 승인된 기록은 유지됩니다.
- 새로고침·탭 강제 종료: 아직 전송하지 않은 메모리 큐는 복원되지 않습니다. 먼저 종료·저장하세요.

## 현재 카메라 화면

프론트만 사용할 때는 `npm ci`, `npm run dev:frontend`로 실행합니다. Python·백엔드 연결은 필요하지 않습니다.
준비 화면에서 카메라를 켜고 브라우저 권한을 허용합니다. 끄기·좌우 반전을 사용할 수 있습니다.
AI 모델과 측정 시작은 비워 두었습니다. 이전의 데모 시작·3초 가상 기준 설정은 기본 화면에서 제거했습니다.
자세한 [카메라 안내](camera-preview.md)를 확인하세요.

## 선택: DynamoDB Local

기본 SQLite 실행과 동시에 포트 5000을 사용하지 않습니다. Docker가 설치된 경우:

```sh
docker compose -f compose.yml up --build
npm run dev:frontend
```

Compose는 DynamoDB Local 초기화 후 Flask를 시작합니다. 로컬 데이터는 별도 Docker 볼륨에 남습니다.
이 경로와 AWS 어댑터는 아직 실행 검증하지 않았습니다.

## 개발 도구

- `npm run build`: ai 타입 확인과 프론트 배포 빌드.
- `npm run lint`: 프론트·분석 모듈 정적 검사.
- `.venv/Scripts/ruff.exe check backend`: 백엔드 정적 검사.
- `npm run contracts:sync` / `contracts:check`: 정식 명세와 생성 복사본·타입 동기화.
- `npm run format`: 코드 포맷. Vitest/Testing Library는 설정만 준비했습니다.

루트 `package-lock.json`을 기준으로 설치합니다. frontend 폴더에 별도 잠금 파일을 만들지 않습니다.
