# 원문에 수록된 연구와 기술 근거

아래는 제공 PDF의 출처 목록과 사용 의도를 정리한 것입니다. 외부 원논문·공식 문서를 새로 대조한 목록이 아니며 모두 **원문 대조 대기**입니다. 원문 밖의 링크·DOI·실험 조건을 추정해서 추가하지 않았습니다.

| ID | PDF의 서지 | 관련 설계 | 적용 한계 |
|---|---|---|---|
| REF-01 | Hansraj KK. Assessment of stresses in the cervical spine caused by posture and position of the head. Surg Technol Int. 2014;25:277–9. | 각도별 목 하중 설명 | 모델 계산값. 15°/30°의 제품 임계값을 직접 검증한 근거로 쓰지 않음 |
| REF-02 | Titcomb DA 외. Evaluation of the Craniovertebral Angle in Standing versus Sitting Positions in Young Adults with and without Severe Forward Head Posture. Int J Exerc Sci. 2024;17(1):73–85. | CVA·자세별 기준 차이 | CVA와 전면 웹캠 특징·상대 pitch를 같은 지표로 취급하지 않음 |
| REF-03 | Trygub I 외. NeckWatcher: A Real-time Monitoring Tool for the Assessment of the Neck Posture. PETRA 2023. | 웹캠 자세 분류 사례 | 84% 정확도·66% 재현율과 조건은 원논문 대조 필요 |
| REF-04 | Watanabe K, Nakamura S. Can We Prevent “Text Neck” Using Only a Smartphone? Real-Time Neck Angle Estimation and a Serious Game as a Case Study. 발표 자료. | 정면 영상 각도 추정 사례 | 약 8.5° 오차의 측정 조건·서지 확인 필요 |
| REF-05 | Kim AR 외. The Validity of Wireless Earbud-Type Wearable Sensors for Head Angle Estimation and the Relationships of Head with Trunk, Pelvis, Hip, and Knee during Workouts. Sensors. 2022;22(2):597. | 이어버드 머리 자세 측정 | 실험 센서·과제 결과를 AirPods 전체 모델 성능으로 일반화하지 않음 |
| REF-06 | Tuken D, Silva I, Vitali RV. Assessing Vibrotactile Feedback Effects on Posture, Muscle Recruitment, and Cognitive Performance. Sensors. 2025;25(8):2416. | 피드백 효과와 작업 방해 | 진동 실험 결과를 이 웹 알림 효과로 단정하지 않음 |
| REF-07 | Marco-Ahulló A 외. Effect of Reduced Feedback Frequencies on Motor Learning in a Postural Control Task in Young Adults. Sensors. 2024;24(5):1404. | 알림 빈도 감소 아이디어 | 100%/67% 조건을 이 제품의 최적 빈도로 고정하지 않음 |
| REF-08 | Mehrotra A 외. My Phone and Me: Understanding People’s Receptivity to Mobile Notifications. CHI 2016. | 알림 타이밍 고려 | 모바일 알림 연구와 웹 자세 알림의 적용 차이 확인 |
| REF-09 | Li I, Dey AK, Forlizzi J. A stage-based model of personal informatics systems. CHI 2010. | 준비·수집·돌아보기·행동 화면 흐름 | UI 설계 근거로 추출 |
| REF-10 | Apple. CMHeadphoneMotionManager, CMDeviceMotion, WWDC23 Core Motion. | 도우미 경로·모션 API | 공식 문서·실제 모델·OS 호환성과 권한을 구현 시 확인 |
| REF-11 | Google. MediaPipe Pose Landmarker. | 관절점과 브라우저 분석 | 선택 버전의 좌표·confidence 의미·라이선스 확인 |
| REF-12 | MDN Notifications API, W3C Understanding WCAG 1.4.1 Use of Color. | 알림 권한·접근성 | 지원 브라우저와 접근성 기준을 구현 시 확인 |
| REF-13 | Physio Network의 목 굽힘과 통증 관련 리뷰. | 통증 예방 효과를 단정하지 않는 표현 | 원문 PDF도 원논문 서지 미확인으로 표시. 효과 근거로 채택하지 않음 |

원문 대조 후 URL, 정확한 서지, 대상·표본 수, 측정 방법, 핵심 결과와 제품 적용 범위를 추가합니다. 검증된 외부 연구도 현재 구현의 실측 결과와 별도로 관리합니다.
