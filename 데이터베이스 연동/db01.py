# 데이터베이스 연동
# DBMS(데이터베이스 관리 시스템) - sqlite3
import sqlite3

# mydb와 연결
try:
    conn = sqlite3.connect("c:/pydb/mydb.db")
    print(conn, "데이터베이스 연결 객체 생성!")
except sqlite3.OperationalError as e:
    print("데이터베이스 연결 실패:", e)
    conn = None
    
# 사원 조회(SELECT) - 테이블이름: employee
def select():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
        cursor = conn.cursor() # 커서(작업) 객체 생성
        sql = "SELECT * FROM employee"
        cursor.execute(sql)
        rows = cursor.fetchall() # 모든 행 가져오기
        print(rows)

# 사원 삽입(INSERT)       
def insert():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
        cursor = conn.cursor()
        # ? - 데이터 바인딩(파라미터화 쿼리)
        sql = "INSERT INTO employee (id, name, salary) VALUES (?, ?, ?)"
        cursor.execute(sql, ('e1002', '우영우', 3500000))
        conn.commit() # 변경사항 저장
        print("데이터 삽입 완료!")

# 특정 사원 조회
def select_one():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM employee WHERE id = ?"
        cursor.execute(sql, ('e1001',))
        row = cursor.fetchone() # 한 행 가져오기
        print(row)
        
# 메인 영역 - 함수 호출
# insert()       
# select()
select_one()