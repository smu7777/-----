import sqlite3

def read_notes_v7(path):
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        # 테이블 목록 출력
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables found:")
        for table in tables:
            print(table[0])

        # 예시로 첫 테이블 데이터 5개 출력
        if tables:
            table_name = tables[0][0]
            print(f"\nData from table '{table_name}':")
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            print("No tables found in the database.")

        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

if __name__ == "__main__":
    path = "/Users/kimhyeonjung/Library/Containers/com.apple.Notes/Data/Library/Notes/NotesV7.storedata"
    read_notes_v7(path)
