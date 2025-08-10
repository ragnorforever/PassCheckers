# 🎯 PassCheckers

> **AI 이미지 분석 기반 수하물 분류 및 여행 도우미 웹 애플리케이션**  
> 2025 캡스톤디자인 팀 프로젝트

![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/flask-3.1-black?logo=flask)
![MySQL](https://img.shields.io/badge/mysql-8.0-orange?logo=mysql)
![YOLOv11](https://img.shields.io/badge/YOLO-v11-yellow)
![Vue](https://img.shields.io/badge/vue.js-3-brightgreen?logo=vue.js)
![Redis](https://img.shields.io/badge/redis-7-red?logo=redis)
![PyTorch](https://img.shields.io/badge/pytorch-2.3.1-orange?logo=pytorch)

---

## 📌 프로젝트 소개

**PassCheckers**는 사용자가 업로드한 수하물 이미지를 분석하여  
YOLOv11 기반 **커스텀 객체 탐지 모델**로 수하물 항목을 자동 인식하고,  
무게 추정, 패킹 추천, 다중 분류 기능 등을 제공하는 **웹 기반 여행 도우미 시스템**입니다.

---

## ✨ 주요 기능

- 📤 **이미지 업로드 및 YOLO 추론 요청**
- 🧠 **YOLOv11 기반 수하물 분류** (단일/다중)
- ⚖️ **무게 추정** (클래스별 평균 무게 기반)
- 🧳 **패킹 도우미** (필수 품목 추천)
- 🏷️ **미탐지 항목 수동 태그 기능** (외부 API 예정)

---

## 📁 프로젝트 구조

```bash
PassCheckers/
 ├── backend/                # Flask 백엔드 서버
 │   ├── models/             # YOLOv11 커스텀 학습 모델
 │   ├── repository/         # DB 접근 계층
 │   ├── service/            # 서비스 로직
 │   ├── venv/               # 가상환경
 │   ├── app.py               # Flask 앱 실행 엔트리포인트
 │   ├── config.py            # 환경 설정 (CORS, DB, Redis 등)
 │   ├── env.example          # 환경변수 예시 파일
 │   ├── requirements.txt     # Python 패키지 목록
 │   └── README.md
 │
 ├── images/                 # 리소스 이미지
 ├── layouts/                # Vue 레이아웃 템플릿
 ├── pages/                  # Vue 페이지 컴포넌트
 ├── plugins/                # Vue 플러그인
 │
 ├── public/                 # 정적 리소스
 │   ├── images/              # 공개 이미지
 │   ├── favicon/             # 파비콘 리소스
 │   ├── favicon.ico
 │   └── robots.txt
 │
 ├── server/                 # 서버사이드 렌더링 관련 코드
 │
 ├── app.vue                  # Nuxt 메인 Vue 컴포넌트
 ├── app.config.ts            # 앱 설정 파일
 ├── nuxt.config.ts           # Nuxt 설정 파일
 ├── package.json
 ├── package-lock.json
 ├── tsconfig.json            # TypeScript 설정
 ├── .gitignore
 ├── .gitattributes
 └── README.md
```

---

## 🧪 실행 방법

1️⃣ 프론트엔드 실행

```bash
cd frontend
npm install
npm run dev -- --host
```

2️⃣ 백엔드 실행

```bash
cd backend
source venv/bin/activate
python3 app.py
```

- ⚠️ `config.py`의 CORS 설정에서 실제 서버 IP를 적용하세요.

3️⃣ Redis 확인

```bash
redis-cli
keys *
keys refresh_token:*
get refresh_token:1
```

4️⃣ MySQL 설정

```bash
(세부 설정은 추후 업데이트 예정)
```

---

## 🔧 기술 스택

|  분류   | 기술 |
|:--------:|:-----:|
| 백엔드 | Python 3.10, Falsk 3.1 |
| 모델 | YOLOv11 (커스텀 학습) |
| 데이터베이스 | MySQL 8.0 |
| 인프라 | Nginx |
| 기타 | OpenCV, Numpy, Pillow, Redis, PyTorch, TensorRT |

---

## 🧭 시스템 흐름도

```bash
(시스템 다이어그램 이미지 추가 예정)
```

---

## 📸 샘플 예시 (시각화)

- 입력 이미지

- 분류 결과

---

## 👥 팀원 소개

|  이름   | 역할 |
|:--------:|-----|
| 김민한 | 🧠 **YOLOv11 커스텀 모델 설계·학습**<br>· 학습 데이터셋 전처리 및 어노테이션 설계<br>· 하이퍼파라미터 튜닝 및 성능 최적화<br>· 프론트엔드 UI/UX 시안 설계 |
| 이상민 | ⚙️ **모델 고도화 및 알고리즘 개발**<br>· YOLOv11 다중 객체 분류 로직 구현<br>· 수하물 무게 예측 알고리즘 개발 (클래스별 평균 무게 기반)<br>· 패킹 추천 알고리즘 설계 |
| 이상호 | 💻 **풀스택 및 시스템 아키텍처 개발**<br>· Flask 기반 REST API 서버 구현<br>· Vue/Nuxt 프론트엔드 연동 및 상태관리<br>· Redis 세션 관리, MySQL DB 설계 및 쿼리 최적화<br>· 전체 시스템 설계 및 배포 환경 구성 |

