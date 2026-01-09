"""
Supabase 저장 테스트 스크립트
이 스크립트를 실행하여 실제로 데이터가 저장되는지 확인하세요.
"""
import sys
import os
from supabase import create_client
import json

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
print("Supabase 저장 테스트")
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

# 1. 테이블 존재 확인
print("\n1. 테이블 존재 확인 중...")
try:
    result = supabase.table("insurance_products").select("id").limit(1).execute()
    print(f"✅ 테이블 존재 확인: {len(result.data)}개 레코드 조회 성공")
except Exception as e:
    print(f"❌ 테이블 조회 실패: {e}")
    print("   → 테이블이 존재하지 않거나 RLS 정책 문제일 수 있습니다.")
    sys.exit(1)

# 2. INSERT 테스트
print("\n2. INSERT 테스트 중...")
test_data = {
    "product_name": "테스트 상품_" + str(int(__import__('time').time())),
    "company": "테스트 보험사",
    "analysis_data": {
        "meta_info": {
            "product_name": "테스트 상품",
            "company": "테스트 보험사"
        },
        "test": True
    },
    "user_id": "admin-temp-id"
}

print(f"저장할 데이터:")
print(json.dumps(test_data, ensure_ascii=False, indent=2))

try:
    result = supabase.table("insurance_products").insert(test_data).execute()
    
    print("\n응답 결과:")
    print(f"- result 타입: {type(result)}")
    print(f"- result.data 존재: {hasattr(result, 'data')}")
    
    if hasattr(result, 'data'):
        print(f"- d result.data: {result.data}")
        if result.data and len(result.data) > 0:
            inserted_id = result.data[0].get('id')
            print(f"\n✅ INSERT 성공! 삽입된 ID: {inserted_id}")
            
            # 3. 저장 확인
            print("\n3. 저장 확인 중...")
            check_result = supabase.table("insurance_products").select("*").eq("id", inserted_id).execute()
            if check_result.data:
                print(f"✅ 저장 확인 완료! {len(check_result.data)}개 레코드 발견")
                print(f"   상품명: {check_result.data[0].get('product_name')}")
                
                # 테스트 데이터 삭제
                print("\n4. 테스트 데이터 삭제 중...")
                try:
                    supabase.table("insurance_products").delete().eq("id", inserted_id).execute()
                    print("✅ 테스트 데이터 삭제 완료")
                except Exception as e:
                    print(f"⚠️ 테스트 데이터 삭제 실패 (무시 가능): {e}")
            else:
                print("❌ 저장 확인 실패: 데이터를 찾을 수 없습니다.")
        else:
            print("❌ INSERT 실패: 응답 데이터가 없습니다.")
            print(f"   전체 응답: {result}")
    else:
        print("❌ INSERT 실패: result.data 속성이 없습니다.")
        print(f"   전체 응답: {result}")
        print(f"   result 속성: {dir(result)}")
        
except Exception as e:
    print(f"\n❌ INSERT 실패: {e}")
    import traceback
    print("\n상세 에러:")
    traceback.print_exc()
    
    # 에러 타입별 안내
    error_str = str(e)
    if "permission" in error_str.lower() or "policy" in error_str.lower() or "row level security" in error_str.lower():
        print("\n💡 RLS 정책 문제로 보입니다.")
        print("   Supabase 대시보드에서 다음을 확인하세요:")
        print("   1. Authentication → Policies")
        print("   2. insurance_products 테이블에 INSERT 정책이 있는지 확인")
        print("   3. 정책이 'anon' 역할에 대해 활성화되어 있는지 확인")
    elif "relation" in error_str.lower() or "does not exist" in error_str.lower():
        print("\n💡 테이블이 존재하지 않는 것 같습니다.")
        print("   supabase_setup.sql 파일을 실행하여 테이블을 생성하세요.")
    elif "column" in error_str.lower():
        print("\n💡 컬럼 문제가 있는 것 같습니다.")
        print("   테이블 구조를 확인하세요.")

print("\n" + "=" * 60)
print("테스트 완료")
print("=" * 60)

