-- Supabase RLS 정책 설정 SQL
-- 이 파일을 Supabase SQL Editor에서 실행하세요.

-- 1. insurance_products 테이블에 RLS 활성화 확인 및 정책 추가

-- RLS 활성화 (이미 활성화되어 있을 수 있음)
ALTER TABLE insurance_products ENABLE ROW LEVEL SECURITY;

-- 기존 정책 삭제 (필요한 경우)
DROP POLICY IF EXISTS "Allow anon insert" ON insurance_products;
DROP POLICY IF EXISTS "Allow anon select" ON insurance_products;
DROP POLICY IF EXISTS "Allow anon update" ON insurance_products;
DROP POLICY IF EXISTS "Allow anon delete" ON insurance_products;

-- Anon Key로 INSERT 허용 정책
CREATE POLICY "Allow anon insert" ON insurance_products
    FOR INSERT
    TO anon
    WITH CHECK (true);

-- Anon Key로 SELECT 허용 정책
CREATE POLICY "Allow anon select" ON insurance_products
    FOR SELECT
    TO anon
    USING (true);

-- Anon Key로 UPDATE 허용 정책
CREATE POLICY "Allow anon update" ON insurance_products
    FOR UPDATE
    TO anon
    USING (true)
    WITH CHECK (true);

-- Anon Key로 DELETE 허용 정책
CREATE POLICY "Allow anon delete" ON insurance_products
    FOR DELETE
    TO anon
    USING (true);

-- 2. consulting_history 테이블에 RLS 활성화 확인 및 정책 추가

-- RLS 활성화
ALTER TABLE consulting_history ENABLE ROW LEVEL SECURITY;

-- 기존 정책 삭제 (필요한 경우)
DROP POLICY IF EXISTS "Allow anon insert" ON consulting_history;
DROP POLICY IF EXISTS "Allow anon select" ON consulting_history;
DROP POLICY IF EXISTS "Allow anon update" ON consulting_history;
DROP POLICY IF EXISTS "Allow anon delete" ON consulting_history;

-- Anon Key로 INSERT 허용 정책
CREATE POLICY "Allow anon insert" ON consulting_history
    FOR INSERT
    TO anon
    WITH CHECK (true);

-- Anon Key로 SELECT 허용 정책
CREATE POLICY "Allow anon select" ON consulting_history
    FOR SELECT
    TO anon
    USING (true);

-- Anon Key로 UPDATE 허용 정책
CREATE POLICY "Allow anon update" ON consulting_history
    FOR UPDATE
    TO anon
    USING (true)
    WITH CHECK (true);

-- Anon Key로 DELETE 허용 정책
CREATE POLICY "Allow anon delete" ON consulting_history
    FOR DELETE
    TO anon
    USING (true);

-- 확인 메시지
SELECT 'RLS 정책이 성공적으로 설정되었습니다!' AS message;

