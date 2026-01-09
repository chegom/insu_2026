"""
Supabase 데이터 삽입 테스트 스크립트
"""

import sys
from supabase import create_client
import json

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Supabase 연결 정보
SUPABASE_URL = "https://sbwwmartlnxadktagwvx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNid3dtYXJ0bG54YWRrdGFnd3Z4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njc3NjM1MTgsImV4cCI6MjA4MzMzOTUxOH0.8EC0zI5p-xzTa0LKL2n7ICbUC2exvJaRYa5IkR4usEs"

def test_insert():
    """데이터 삽입 테스트"""
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        print("Supabase 연결 성공!")
        print("\n데이터 삽입 테스트 중...")
        
        # 테스트 데이터
        test_data = {
            "product_name": "테스트 보험 상품",
            "company": "테스트 보험사",
            "analysis_data": {
                "meta_info": {
                    "product_name": "테스트 보험 상품",
                    "company": "테스트 보험사"
                },
                "test": True
            },
            "user_id": "admin-temp-id"
        }
        
        print(f"\n삽입할 데이터:")
        print(json.dumps(test_data, ensure_ascii=False, indent=2))
        
        # 삽입 시도
        result = supabase.table("insurance_products").insert(test_data).execute()
        
        print("\n✅ 데이터 삽입 성공!")
        print(f"응답 데이터: {result.data}")
        
        if result.data:
            inserted_id = result.data[0]['id']
            print(f"\n삽입된 ID: {inserted_id}")
            
            # 삽입 확인
            check = supabase.table("insurance_products").select("*").eq("id", inserted_id).execute()
            print(f"\n확인 결과: {len(check.data)}개 발견")
            if check.data:
                print(f"상품명: {check.data[0].get('product_name')}")
            
            # 테스트 데이터 삭제
            print("\n테스트 데이터 삭제 중...")
            supabase.table("insurance_products").delete().eq("id", inserted_id).execute()
            print("✅ 테스트 데이터 삭제 완료")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {str(e)}")
        import traceback
        print("\n상세 에러:")
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    test_insert()

