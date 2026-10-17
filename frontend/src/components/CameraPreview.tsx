import { useState } from 'react';
import { Camera, CameraOff, FlipHorizontal2, LockKeyhole, Video } from 'lucide-react';
import { useWebcam } from '../features/camera/useWebcam';
import { Button } from './ui';

export function CameraPreview() {
  const camera = useWebcam();
  const [mirrored, setMirrored] = useState(true);
  const playing = camera.status === 'playing';
  const requesting = camera.status === 'requesting';
  return (
    <section className="panel webcam-panel" aria-labelledby="webcam-title">
      <div className="section-heading">
        <div>
          <h2 id="webcam-title">내 카메라 화면</h2>
          <p>카메라를 켜고 현재 영상이 잘 보이는지 확인해 주세요.</p>
        </div>
        <span className={`badge ${playing ? 'success' : 'neutral'}`}>
          <span className={playing ? 'pulse-dot' : 'dot'} />
          {playing ? '카메라 켜짐' : requesting ? '권한 요청 중' : '카메라 꺼짐'}
        </span>
      </div>
      <div className={`webcam-stage ${playing ? 'is-playing' : ''}`}>
        <video
          ref={camera.videoRef}
          muted
          playsInline
          autoPlay
          className={mirrored ? 'mirrored' : ''}
          aria-label="실시간 웹캠 미리보기"
        />
        {!playing && (
          <div className="webcam-empty">
            <span className="webcam-empty-icon">
              {requesting ? <Video size={32} /> : <CameraOff size={32} />}
            </span>
            <strong>
              {requesting
                ? '카메라 권한을 기다리고 있어요.'
                : '카메라를 켜면 이곳에 영상이 표시돼요.'}
            </strong>
            <p>
              {requesting
                ? '브라우저 권한 창에서 허용을 선택해 주세요.'
                : '마이크는 켜지지 않아요.'}
            </p>
          </div>
        )}
        <span className="webcam-stage-label">
          <LockKeyhole size={12} />내 기기에서만 표시
        </span>
        {playing && camera.resolution && (
          <span className="webcam-resolution">{camera.resolution}</span>
        )}
      </div>
      <div className="webcam-controls">
        <div>
          <strong>{playing ? '웹캠 연결 완료' : requesting ? '연결 준비 중' : '웹캠 연결'}</strong>
          <p
            className={camera.status === 'error' ? 'field-error' : ''}
            aria-live="polite"
            role={camera.status === 'error' ? 'alert' : 'status'}
          >
            {camera.message}
          </p>
        </div>
        <div className="button-row">
          {playing && (
            <Button
              variant="ghost"
              onClick={() => setMirrored((value) => !value)}
              aria-pressed={mirrored}
            >
              <FlipHorizontal2 size={16} />
              좌우 반전
            </Button>
          )}
          {playing ? (
            <Button variant="secondary" onClick={() => camera.stop()}>
              <CameraOff size={16} />
              카메라 끄기
            </Button>
          ) : requesting ? (
            <Button variant="secondary" onClick={camera.cancel}>
              요청 취소
            </Button>
          ) : (
            <Button onClick={() => void camera.start()}>
              <Camera size={17} />
              {camera.status === 'error' ? '카메라 다시 켜기' : '카메라 켜기'}
            </Button>
          )}
        </div>
      </div>
      <p className="webcam-privacy-note">
        다른 페이지로 이동하거나 화면이 비활성화되면 카메라를 해제합니다. 영상·소리·사진을
        저장하거나 서버에 전송하지 않습니다.
      </p>
    </section>
  );
}
