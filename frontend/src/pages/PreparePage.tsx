import { Camera, CheckCircle2, Cpu, LockKeyhole, ShieldCheck } from 'lucide-react';
import { motion } from 'motion/react';
import { CameraPreview } from '../components/CameraPreview';
import { Button } from '../components/ui';
import { postureModelAdapter } from '../features/measurement/model-adapter';

export function PreparePage() {
  return (
    <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}>
      <div className="page-heading">
        <div>
          <span className="eyebrow">웹캠 연결부터 차근차근</span>
          <h1>먼저, 카메라를 연결해요.</h1>
          <p>내 영상이 잘 보이는지 확인하고 다음 단계를 준비해 주세요.</p>
        </div>
        <span className="badge outline">
          <Camera size={14} />
          카메라 미리보기
        </span>
      </div>
      <div className="camera-preparation-layout">
        <div>
          <CameraPreview />
          <section className="panel camera-guide">
            <div className="section-heading">
              <h2>이렇게 준비해 주세요</h2>
            </div>
            <ol>
              <li>
                <span>01</span>
                <div>
                  <strong>카메라 권한 허용</strong>
                  <p>‘카메라 켜기’를 누른 뒤 브라우저에서 허용해 주세요.</p>
                </div>
              </li>
              <li>
                <span>02</span>
                <div>
                  <strong>얼굴과 어깨가 보이도록</strong>
                  <p>카메라를 정면에 두고 영상이 잘 나오는지 확인해 주세요.</p>
                </div>
              </li>
              <li>
                <span>03</span>
                <div>
                  <strong>사용이 끝나면 카메라 끄기</strong>
                  <p>버튼을 누르거나 다른 페이지로 이동하면 연결을 해제합니다.</p>
                </div>
              </li>
            </ol>
          </section>
        </div>
        <aside className="camera-preparation-aside">
          <section className="panel model-placeholder">
            <span className="model-placeholder-icon">
              <Cpu size={28} />
            </span>
            <span className="eyebrow">NEXT STEP</span>
            <h2>자세 측정 AI 모델</h2>
            <span className="badge neutral">
              {postureModelAdapter ? '어댑터 준비' : '연결 대기'}
            </span>
            <p id="model-pending-description">
              이곳에 자세를 분석하는 AI 모델을 연결할 예정이에요. 현재는 카메라 화면 확인까지 사용할
              수 있습니다.
            </p>
            <div className="model-placeholder-steps">
              <span>
                <CheckCircle2 size={15} />
                실제 카메라 연결
              </span>
              <span className="pending">
                <Cpu size={15} />
                AI 모델 연결 예정
              </span>
              <span className="pending">
                <Camera size={15} />
                측정·판정 연결 예정
              </span>
            </div>
            <Button
              disabled
              aria-describedby="model-pending-description"
              className="model-pending-button"
            >
              측정 시작 · 준비 중
            </Button>
          </section>
          <div className="privacy-card">
            <ShieldCheck size={23} />
            <div>
              <strong>내 영상은 내 기기에만</strong>
              <p>
                이번 단계에서는 영상을 화면에 표시합니다. 영상 분석과 결과 저장은 모델 연결 후
                진행합니다.
              </p>
            </div>
          </div>
          <div className="camera-local-note">
            <LockKeyhole size={16} />
            <p>녹화·사진 촬영·마이크 수집 기능은 켜지지 않습니다.</p>
          </div>
        </aside>
      </div>
    </motion.div>
  );
}
