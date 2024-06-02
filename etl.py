import sqlite3

# SQLite 데이터베이스에 연결
sqlite_conn = sqlite3.connect(r'C:\Users\hospc\djangogirls\db.sqlite3')

# 모든 테이블 이름 조회
cursor = sqlite_conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 테이블 이름 출력
for table in tables:
    print(table[0])

# 연결 종료
sqlite_conn.close()

