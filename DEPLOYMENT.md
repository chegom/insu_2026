# 배포 가이드

## Railway 배포 방법 (추천)

Railway는 무료 티어를 제공하며, 더 많은 제어권과 유연성을 제공합니다.

### 1. Railway 계정 생성 및 GitHub 연결
1. https://railway.app 접속
2. GitHub 계정으로 로그인
3. **중요**: GitHub 권한 요청 시 저장소 접근 권한을 허용해야 합니다
   - Railway가 저장소를 읽을 수 있도록 권한 부여 필요

### 2. 새 프로젝트 생성
1. Railway 대시보드에서 "New Project" 클릭
2. "Deploy from GitHub repo" 선택
3. 저장소 목록에서 `chegom/insu_2026` 찾기
   - **만약 저장소가 안 보이면**:
     - Railway 대시보드 우측 상단 프로필 아이콘 클릭
     - "Settings" → "Connected Accounts" → GitHub 확인
     - "Configure GitHub App" 클릭하여 권한 재설정
     - 저장소 접근 권한을 "All repositories" 또는 "Selected repositories"로 설정
     - `chegom/insu_2026` 저장소 선택
4. 저장소 선택 후 "Deploy Now" 클릭

### 3. 환경 변수 설정
Railway 대시보드에서 "Variables" 탭에 다음 환경 변수를 추가:

```
SUPABASE_URL=여기에_SUPABASE_URL
SUPABASE_KEY=여기에_SUPABASE_ANON_KEY
GEMINI_API_KEY=여기에_GEMINI_API_KEY
```

또는 Streamlit Secrets 형식으로 설정하려면:

```
STREAMLIT_SECRETS={"supabase":{"url":"여기에_SUPABASE_URL","key":"여기에_SUPABASE_ANON_KEY"},"google":{"api_key":"여기에_GEMINI_API_KEY"}}
```

### 4. 배포 설정
- Railway가 자동으로 `requirements.txt`를 인식합니다
- `Procfile` 또는 `railway.json`이 있으면 자동으로 사용됩니다
- 포트는 Railway가 자동으로 할당합니다 (`$PORT` 환경 변수 사용)

### 5. 배포 완료
- 배포가 완료되면 Railway가 자동으로 URL을 생성합니다
- "Settings" → "Generate Domain"에서 커스텀 도메인 설정 가능

### Railway 장점
- ✅ 무료 티어 제공 (월 $5 크레딧)
- ✅ 자동 HTTPS
- ✅ 커스텀 도메인 지원
- ✅ 더 많은 제어권
- ✅ 로그 확인 용이

## Streamlit Cloud 배포 방법

### 1. GitHub 저장소 준비
- 코드를 GitHub에 푸시합니다
- 저장소는 Public 또는 Private 모두 가능합니다

### 2. Streamlit Cloud에서 배포
1. https://streamlit.io/cloud 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 저장소 선택: `chegom/insu_2026`
5. Branch: `main`
6. Main file: `app.py`

### 3. 환경 변수 설정 (Secrets)
Streamlit Cloud 대시보드에서 "Secrets" 탭에 다음을 추가:

```toml
[supabase]
url = "여기에_SUPABASE_URL"
key = "여기에_SUPABASE_ANON_KEY"

[google]
api_key = "여기에_GEMINI_API_KEY"
```

### 4. 배포 완료
- 배포가 완료되면 `https://your-app-name.streamlit.app` 형태의 URL이 생성됩니다
- 이 URL을 공유하면 다른 사람도 사용할 수 있습니다

## 로컬 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/chegom/insu_2026.git
cd insu_2026
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
```bash
# .streamlit 폴더 생성
mkdir .streamlit

# secrets.toml 파일 생성 (예시 파일 복사)
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# 실제 값으로 수정
# Windows: notepad .streamlit/secrets.toml
# Mac/Linux: nano .streamlit/secrets.toml
```

### 4. 실행
```bash
streamlit run app.py
```

## Supabase 설정

### 1. Supabase 프로젝트 생성
1. https://supabase.com 접속
2. 새 프로젝트 생성
3. Project URL과 Anon Key 확인

### 2. 데이터베이스 테이블 생성
Supabase 대시보드 → SQL Editor에서 다음 SQL 실행:

```sql
-- supabase_setup.sql 파일의 내용 실행
```

### 3. RLS 정책 설정
```sql
-- supabase_rls_policies.sql 파일의 내용 실행
```

## Google Gemini API 설정

1. https://ai.google.dev 접속
2. API 키 생성
3. 무료 할당량 확인 (일일 제한 있음)

## 주의사항

⚠️ **테스트 버전**: 현재는 로그인 기능이 없어 누구나 접근 가능합니다.
- 나중에 로그인 기능을 추가하여 접근을 제한할 예정입니다.
- 민감한 데이터는 사용하지 마세요.

⚠️ **API 사용량**: 
- Gemini API는 무료 티어가 있지만 일일 사용량 제한이 있습니다.
- Supabase는 무료 티어에서도 충분히 사용 가능합니다.

