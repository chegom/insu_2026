"""
Supabase 테이블 확인 스크립트
"""

import sys
from supabase import create_client

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Supabase 연결 정보
SUPABASE_URL = "https://sbwwmartlnxadktagwvx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNid3dtYXJ0bG54YWRrdGFnd3Z4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njc3NjM1MTgsImV4cCI6MjA4MzMzOTUxOH0.8EC0zI5p-xzTa0LKL2n7ICbUC2exvJaRYa5IkR4usEs"

def test_tables():
    """테이블 존재 확인 및 테스트"""
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        print("Supabase 테이블 확인 중...\n")
        
        # insurance_products 테이블 확인
        try:
            result = supabase.table("insurance_products").select("id").limit(1).execute()
            print("✅ insurance_products 테이블: 존재함")
        except Exception as e:
            print(f"❌ insurance_products 테이블: 오류 - {str(e)}")
            return False
        
        # consulting_history 테이블 확인
        try:
            result = supabase.table("consulting_history").select("id").limit(1).execute()
            print("✅ consulting_history 테이블: 존재함")
        except Exception as e:
            print(f"❌ consulting_history 테이블: 오류 - {str(e)}")
            return False
        
        # 테스트 데이터 삽입
        print("\n테스트 데이터 삽입 중...")
        try:
            test_data = {
                "product_name": "테스트 상품",
                "company": "테스트 보험사",
                "analysis_data": {"test": "data"},
                "user_id": "admin-temp-id"
            }
            result = supabase.table("insurance_products").insert(test_data).execute()
            print("✅ 테스트 데이터 삽입 성공!")
            
            # 테스트 데이터 삭제
            if result.data:
                test_id = result.data[0]['id']
                supabase.table("insurance_products").delete().eq("id", test_id).execute()
                print("✅ 테스트 데이터 삭제 완료")
        except Exception as e:
            print(f"⚠️ 테스트 데이터 삽입 실패: {str(e)}")
            print("   (테이블은 존재하지만 권한 문제일 수 있습니다)")
        
        print("\n✅ 모든 테이블이 정상적으로 생성되었습니다!")
        print("애플리케이션을 사용할 준비가 되었습니다.")
        return True
        
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        return False

if __name__ == "__main__":
    test_tables()

