import { Link, Outlet, useRouterState } from '@tanstack/react-router';
import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import {
  Activity,
  ArrowUpRight,
  ClipboardList,
  Leaf,
  LayoutDashboard,
  LockKeyhole,
  Settings2,
  ShieldCheck,
} from 'lucide-react';
import { api } from '../api/client';
import { usePreferences } from '../state/preferences';
import { Modal, Toggle } from './ui';

export function Shell() {
  const pathname = useRouterState({ select: (state) => state.location.pathname });
  const muted = usePreferences((s) => s.muted),
    setMuted = usePreferences((s) => s.setMuted);
  const [settings, setSettings] = useState(false);
  const health = useQuery({ queryKey: ['health'], queryFn: api.health, refetchInterval: 15000 });
  const navigation = [
    { to: '/', icon: LayoutDashboard, label: '카메라 준비' },
    { to: '/measure', icon: Activity, label: '측정 준비 중' },
    { to: '/history', icon: ClipboardList, label: '자세 기록' },
  ] as const;
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <Link to="/" className="brand">
          <span className="brand-mark">
            <Leaf size={24} />
          </span>
          <span>
            ecolephant<small>좋은 자세의 작은 시작</small>
          </span>
        </Link>
        <span className="nav-caption">MY POSTURE</span>
        <nav aria-label="주요 메뉴">
          {navigation.map(({ to, icon: Icon, label }) => {
            const disabled = to === '/measure';
            return (
              <Link
                key={to}
                to={to}
                className={`nav-item ${(to === '/' ? pathname === '/' : pathname.startsWith(to)) ? 'selected' : ''} ${disabled ? 'disabled' : ''}`}
                aria-disabled={disabled}
                onClick={(event) => {
                  if (disabled) event.preventDefault();
                }}
              >
                <Icon size={19} />
                {label}
              </Link>
            );
          })}
        </nav>
        <div className="sidebar-bottom">
          <div className="sidebar-tip">
            <Leaf size={22} />
            <strong>작은 변화부터 시작해요.</strong>
            <p>
              잠깐 어깨를 내리고
              <br />
              편안하게 숨을 쉬어보세요.
            </p>
            <span>
              오늘의 작은 루틴
              <ArrowUpRight size={13} />
            </span>
          </div>
          <button className="nav-item" onClick={() => setSettings(true)}>
            <Settings2 size={19} />
            알림 설정
          </button>
          <div className="sidebar-footer">
            ecolephant · MVP 01<small>Posture, at your pace.</small>
          </div>
        </div>
      </aside>
      <div className="main-shell">
        <header className="topbar">
          <div className="breadcrumb">
            나의 공간<span>/</span>
            {pathname.startsWith('/history')
              ? '자세 기록'
              : pathname === '/measure'
                ? '측정 준비 중'
                : '카메라 준비'}
          </div>
          <div className="topbar-right">
            <span className={`connection ${health.isSuccess ? 'online' : 'offline'}`}>
              <i />
              {health.isSuccess ? '로컬 서버 연결됨' : '서버 연결 확인 중'}
            </span>
            <span className="avatar">E</span>
          </div>
        </header>
        <main id="main-content">
          <div className="workspace-content">
            <Outlet />
          </div>
        </main>
        <footer className="app-footer">
          <span>
            <ShieldCheck size={14} />
            영상은 업로드하지 않아요.
          </span>
          <span>카메라 미리보기 · AI 모델 연결 대기</span>
        </footer>
      </div>
      <Modal
        open={settings}
        onOpenChange={setSettings}
        title="알림 설정"
        description="AI 모델과 측정 기능 연결 후 사용할 알림 설정입니다. 현재는 알림을 실행하지 않습니다."
      >
        <Toggle label="화면 알림 받기" checked={!muted} onChange={(value) => setMuted(!value)} />
        <p className="settings-help">
          <LockKeyhole size={16} />
          브라우저에는 알림·화면 순서 설정만 보관합니다.
        </p>
      </Modal>
    </div>
  );
}
