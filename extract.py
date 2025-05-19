import sqlite3
from striprtf.striprtf import rtf_to_text

DB_PATH = "/Users/kimhyeonjung/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite"

def extract_text_notes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT Z_PK, ZDATA FROM ZICNOTEDATA")
    
    for pk, data in cursor.fetchall():
        if data:
            try:
                # RTF 바이너리 데이터를 텍스트로 변환
                text = rtf_to_text(data.decode('utf-8', errors='ignore'))
                print(f"--- Note {pk} ---")
                print(text)
                print()
            except Exception as e:
                print(f"Note {pk} 변환 중 오류:", e)
    
    conn.close()

if __name__ == "__main__":
    extract_text_notes()
