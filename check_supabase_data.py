"""
Supabase 데이터 확인 스크립트
실제로 데이터가 있는지, SELECT 권한이 있는지 확인합니다.
"""
import sys
import os
from supabase import create_client

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Streamlit secrets에서 설정 가져오기
try:
    import streamlit as st
    SUPABASE_URL = st.secrets.get("supabase", {}).get("url")
    SUPABASE_KEY = st.secrets.get("supabase", {}).get("key")
except:
    # Streamlit 없이 실행하는 경우
    import toml
    secrets_path = os.path.join(".streamlit", "secrets.toml")
    if os.path.exists(secrets_path):
        secrets = toml.load(secrets_path)
        SUPABASE_URL = secrets.get("supabase", {}).get("url")
        SUPABASE_KEY = secrets.get("supabase", {}).get("key")
    else:
        print("❌ secrets.toml 파일을 찾을 수 없습니다.")
        sys.exit(1)

print("=" * 60)
print("Supabase 데이터 확인")
print("=" * 60)
print(f"URL: {SUPABASE_URL}")
print(f"Key (처음 20자): {SUPABASE_KEY[:20] if SUPABASE_KEY else 'None'}...")
print()

# Supabase 클라이언트 생성
try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("✅ Supabase 클라이언트 생성 성공")
except Exception as e:
    print(f"❌ Supabase 클라이언트 생성 실패: {e}")
    sys.exit(1)

# 1. SELECT 테스트 (RLS 정책 확인)
print("\n1. SELECT 쿼리 테스트 (RLS 정책 확인)...")
try:
    result = supabase.table("insurance_products").select("*").execute()
    print(f"✅ SELECT 쿼리 성공")
    print(f"   - result.data 타입: {type(result.data)}")
    print(f"   - result.data 길이: {len(result.data) if result.data else 0}")
    
    if result.data and len(result.data) > 0:
        print(f"   - 발견된 상품 수: {len(result.data)}")
        for idx, product in enumerate(result.data[:5], 1):  # 최대 5개만 표시
            print(f"   {idx}. ID: {product.get('id')}, 상품명: {product.get('product_name')}")
    else:
        print("   ⚠️ 데이터가 없습니다 (빈 리스트)")
        print("   → RLS 정책에서 SELECT 권한이 없거나, 실제로 데이터가 없을 수 있습니다.")
        
except Exception as e:
    error_str = str(e)
    print(f"❌ SELECT 쿼리 실패: {error_str}")
    
    if "permission" in error_str.lower() or "policy" in error_str.lower() or "row level security" in error_str.lower():
        print("\n💡 RLS 정책 문제로 보입니다!")
        print("   Supabase 대시보드에서 다음을 확인하세요:")
        print("   1. Authentication → Policies")
        print("   2. insurance_products 테이블 선택")
        print("   3. SELECT 정책이 'anon' 역할에 대해 활성화되어 있는지 확인")
        print("   4. supabase_rls_policies.sql 파일의 SQL을 실행하세요")

# 2. INSERT 후 즉시 SELECT 테스트
print("\n2. INSERT 후 즉시 SELECT 테스트...")
try:
    import time
    test_data = {
        "product_name": f"테스트_확인_{int(time.time())}",
        "company": "테스트 보험사",
        "analysis_data": {"test": True},
        "user_id": "admin-temp-id"
    }
    
    print(f"   INSERT 실행 중...")
    insert_result = supabase.table("insurance_products").insert(test_data).execute()
    
    if insert_result.data and len(insert_result.data) > 0:
        inserted_id = insert_result.data[0].get('id')
        print(f"   ✅ INSERT 성공 (ID: {inserted_id})")
        
        # 즉시 SELECT로 확인
        print(f"   SELECT로 확인 중...")
        select_result = supabase.table("insurance_products").select("*").eq("id", inserted_id).execute()
        
        if select_result.data and len(select_result.data) > 0:
            print(f"   ✅ SELECT 성공! 데이터 확인됨")
            print(f"      상품명: {select_result.data[0].get('product_name')}")
            
            # 테스트 데이터 삭제
            print(f"   테스트 데이터 삭제 중...")
            supabase.table("insurance_products").delete().eq("id", inserted_id).execute()
            print(f"   ✅ 테스트 데이터 삭제 완료")
        else:
            print(f"   ❌ SELECT 실패: 데이터를 찾을 수 없습니다")
            print(f"   → INSERT는 성공했지만 SELECT 권한이 없을 수 있습니다")
            print(f"   → RLS 정책에서 SELECT 권한을 확인하세요")
    else:
        print(f"   ❌ INSERT 실패: 응답 데이터가 없습니다")
        
except Exception as e:
    print(f"   ❌ 테스트 실패: {e}")
    import traceback
    traceback.print_exc()

# 3. 전체 데이터 개수 확인
print("\n3. 전체 데이터 개수 확인...")
try:
    count_result = supabase.table("insurance_products").select("id", count="exact").execute()
    print(f"   전체 레코드 수: {count_result.count if hasattr(count_result, 'count') else 'N/A'}")
except Exception as e:
    print(f"   ⚠️ 개수 조회 실패: {e}")

print("\n" + "=" * 60)
print("확인 완료")
print("=" * 60)
print("\n💡 해결 방법:")
print("1. Supabase 대시보드 → Authentication → Policies")
print("2. insurance_products 테이블 선택")
print("3. SELECT 정책이 'anon' 역할에 대해 활성화되어 있는지 확인")
print("4. supabase_rls_policies.sql 파일의 SQL을 실행하세요")

