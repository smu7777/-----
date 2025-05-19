import sqlite3

DB_PATH = "/Users/kimhyeonjung/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite"

def extract_notes_from_zcontent():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT Z_PK, ZCONTENT FROM ZICCLOUDSYNCINGOBJECT WHERE ZCONTENT IS NOT NULL")
        notes = cursor.fetchall()

        print(f"총 노트 개수: {len(notes)}")
        for pk, content in notes:
            try:
                text = content.decode('utf-8', errors='ignore') if isinstance(content, bytes) else content
                print(f"\n--- Note ID: {pk} ---\n{text}\n")
            except Exception as e:
                print(f"[Note {pk}] 디코딩 실패: {e}")

    except Exception as e:
        print("쿼리 실패:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    extract_notes_from_zcontent()
