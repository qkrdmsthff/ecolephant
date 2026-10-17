# 프론트엔드

React 19 · TypeScript 5.9 · Vite 8 · npm workspace, Node 22 기준입니다.

## 현재 화면

기본 화면은 실제 카메라 권한 요청·켜기·끄기·영상 표시·좌우 반전입니다.
페이지 이동·탭 숨김·장치 종료 때 스트림을 정리합니다.
AI 모델 어댑터는 null이며 측정 시작은 준비 중입니다. 모델·WASM·가중치를 추가하지 않았습니다.

## 실행

루트 `npm ci`, `npm run dev:frontend`로 카메라 화면을 열 수 있습니다.
Flask와 함께 실행할 때는 `npm run setup`, `npm run dev`를 사용합니다.
주소는 `http://127.0.0.1:5173`입니다.

## 주요 위치

- `src/features/camera/useWebcam.ts`: 실제 MediaStream 수명주기.
- `src/components/CameraPreview.tsx`: 영상 표시·사용자 조작.
- `src/features/measurement/model-adapter.ts`: 후속 모델 연결 자리.
- `src/pages/PreparePage.tsx`: 현재 기본 화면.
- `src/pages/HistoryPage.tsx`: 기존 예시 기록 조회.

TanStack Router/Query, Zustand, RHF/Zod, Tailwind 4, Radix, CVA, dnd kit, Motion, Axios, API 생성 타입,
Vitest/Testing Library, ESLint/Prettier/Husky/lint-staged 설정은 기존 구성에 있습니다.
개인 디자인 시스템 패키지는 이름·버전·권한이 전달되지 않아 미연결입니다.

[카메라 안내](../docs/development/camera-preview.md) · [현재 상태](../docs/development/mvp-status.md).
