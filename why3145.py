import sqlite3

DB_PATH = "/Users/kimhyeonjung/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM ZICNOTEDATA")
count = cursor.fetchone()[0]
print(f"총 노트 개수: {count}")

cursor.execute("SELECT Z_PK FROM ZICNOTEDATA")
all_ids = [row[0] for row in cursor.fetchall()]
print(f"노트 ID 목록 예: {all_ids[:10]} ...")

conn.close()
