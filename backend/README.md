# PassCheckers Backend API

Flask 기반의 백엔드 API 서버입니다.

## 설치 및 실행

### 1. Python 가상환경 생성
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate  # Windows
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
```bash
cp env.example .env
# .env 파일을 편집하여 실제 값으로 변경
```

### 4. 데이터베이스 설정
- MySQL 설치 및 실행
- 데이터베이스 생성: `passcheckers`
- Redis 설치 및 실행

### 5. 서버 실행
```bash
python app.py
```

서버는 `http://localhost:5000`에서 실행됩니다.

## API 엔드포인트

### 인증 관련
- `POST /api/register` - 회원가입
- `POST /api/login` - 로그인
- `POST /api/refresh` - Access Token 재발급
- `POST /api/logout` - 로그아웃

### 사용자 관련
- `GET /api/profile` - 사용자 프로필 조회
- `GET /api/protected` - 인증 테스트

### 시스템
- `GET /api/health` - 서버 상태 확인

## 환경 변수

- `SECRET_KEY`: Flask 시크릿 키
- `JWT_SECRET_KEY`: JWT 시크릿 키
- `REDIS_URL`: Redis 연결 URL
- `DATABASE_URL`: MySQL 연결 URL

## 개발 환경

- Python 3.8+
- Flask 3.0.0
- MySQL
- Redis 