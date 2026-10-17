import { useNavigate } from '@tanstack/react-router';
import { Camera, Cpu } from 'lucide-react';
import { Button, Notice } from '../components/ui';

export function MeasurePage() {
  const navigate = useNavigate();
  return (
    <div>
      <div className="page-heading">
        <div>
          <span className="eyebrow">AI 모델 연결 대기</span>
          <h1>자세 측정을 준비하고 있어요.</h1>
          <p>현재는 웹캠을 켜고 영상을 확인하는 단계입니다.</p>
        </div>
      </div>
      <section className="panel">
        <div className="empty-state">
          <Cpu size={42} />
          <h2>자세 측정 AI 모델을 연결할 자리예요.</h2>
          <p>모델 연결 후 실제 측정·판정·알림 흐름을 이어서 구현합니다.</p>
          <Button onClick={() => navigate({ to: '/' })}>
            <Camera size={16} />
            카메라 화면으로 돌아가기
          </Button>
        </div>
      </section>
      <Notice>
        현재 측정은 시작되지 않으며 예시 각도·판정·측정 기록도 새로 생성하지 않습니다.
      </Notice>
    </div>
  );
}
