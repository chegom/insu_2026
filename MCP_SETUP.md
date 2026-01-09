# MCP Supabase 연결 가이드

## 현재 상태
- ✅ 설정 파일 생성 완료 (`.streamlit/secrets.toml`)
- ✅ Gemini API 키 설정 가능
- ⚠️ Supabase는 MCP를 통해 연결 예정

## MCP 연결 방법

Supabase를 MCP로 연결하려면 다음 단계를 따르세요:

### 1. MCP 서버 설정
MCP 서버를 통해 Supabase에 연결하도록 설정해야 합니다.

### 2. 코드 수정
`app.py`의 `init_supabase()` 함수에서 MCP 클라이언트를 통해 Supabase에 접근하도록 구현하세요.

예시:
```python
def init_supabase():
    """Supabase 클라이언트 초기화 - MCP를 통해 연결"""
    try:
        # MCP 클라이언트를 통해 Supabase 연결
        # mcp_client = get_mcp_client()
        # return mcp_client.get_supabase()
        pass
    except Exception as e:
        st.warning(f"⚠️ Supabase MCP 연결 실패: {str(e)}")
        return None
```

### 3. 현재 동작
- Gemini API는 정상 작동합니다 (API 키 설정 시)
- Supabase 기능은 MCP 연결이 완료되면 사용 가능합니다

## 다음 단계
1. MCP 서버 설정
2. `app.py`의 `init_supabase()` 함수에 MCP 연결 코드 추가
3. 테스트 실행

