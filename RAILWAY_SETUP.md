# Railway 배포 설정 가이드

## Railway에서 Supabase 연결하기

Railway에 배포한 앱에서 Supabase를 연결하려면 **환경 변수**를 설정해야 합니다.

### 1. Railway 대시보드 접속
1. https://railway.app 접속
2. 배포한 프로젝트 선택

### 2. 환경 변수 설정 (중요: 위치 확인!)

⚠️ **"Shared Variables"가 아닙니다!**

환경 변수는 **서비스(Service) 레벨**에서 설정해야 합니다:

1. 프로젝트 대시보드에서 배포된 **서비스(Service)** 클릭
   - 보통 "web" 또는 프로젝트 이름과 같은 서비스가 있습니다
2. 서비스 페이지에서 **"Variables"** 탭 클릭
   - 왼쪽 사이드바에 "Variables" 메뉴가 있습니다
   - 또는 상단 탭에서 "Variables" 선택

❌ **잘못된 위치**: Project Settings → Shared Variables (이건 여러 서비스 공유용)
✅ **올바른 위치**: Service → Variables (서비스별 환경 변수)

다음 3개의 환경 변수를 **각각 추가**하세요:

| 변수명 | 값 예시 | 설명 |
|--------|---------|------|
| `SUPABASE_URL` | `https://xxxxx.supabase.co` | Supabase 프로젝트 URL |
| `SUPABASE_KEY` | `eyJhbGci...` | Supabase Anon Key (공개 키) |
| `GEMINI_API_KEY` | `AIza...` | Google Gemini API 키 |

### 3. 환경 변수 추가 방법
1. "Variables" 탭에서 **"+ New Variable"** 클릭
2. 변수명 입력 (예: `SUPABASE_URL`)
3. 값 입력 (예: `https://sbwwmartlnxadktagwvx.supabase.co`)
4. "Add" 클릭
5. 나머지 2개도 동일하게 추가

### 4. 재배포
환경 변수를 추가한 후:
- **자동 재배포**: 코드를 GitHub에 푸시하면 자동으로 재배포됩니다
- **수동 재배포**: "Deployments" 탭 → 최신 배포 → "Redeploy" 클릭

### 5. 확인
재배포 후 앱을 새로고침하면 Supabase 연결이 정상적으로 작동합니다.

## Supabase 정보 확인 방법

### Supabase 프로젝트에서 URL과 Key 확인:
1. https://supabase.com 접속
2. 프로젝트 선택
3. **Settings** → **API** 메뉴
4. **Project URL**: `SUPABASE_URL`에 사용
5. **anon public** 키: `SUPABASE_KEY`에 사용

## 문제 해결

### 환경 변수가 적용되지 않을 때:
1. 환경 변수 이름이 정확한지 확인 (`SUPABASE_URL`, `SUPABASE_KEY`, `GEMINI_API_KEY`)
2. 값에 따옴표나 공백이 없는지 확인
3. 재배포가 완료되었는지 확인
4. Railway 로그 확인: "Deployments" → "View Logs"

### 여전히 연결이 안 될 때:
- Railway 로그에서 에러 메시지 확인
- Supabase URL과 Key가 올바른지 다시 확인
- Supabase 프로젝트가 활성화되어 있는지 확인

