import sqlite3
import os
from striprtf.striprtf import rtf_to_text
import datetime

# 1. NoteStore.sqlite 경로 지정
DB_PATH = os.path.expanduser('~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite')

def extract_notes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 2. ZNOTEBODY 테이블에서 ZCONTENT 컬럼 가져오기
    cursor.execute('SELECT Z_PK, ZCONTENT FROM ZNOTEBODY')
    rows = cursor.fetchall()

    if not os.path.exists('extracted_notes'):
        os.makedirs('extracted_notes')

    count = 0
    for row in rows:
        note_id = row[0]
        raw_content = row[1]

        if raw_content is None:
            continue

        text = ''
        try:
            text = rtf_to_text(raw_content)
        except Exception:
            text = raw_content  # 실패하면 원본 저장

        filename = f'extracted_notes/note_{note_id}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        count += 1

    conn.close()
    print(f'총 {count}개의 메모를 extracted_notes 폴더에 저장 완료.')

if __name__ == '__main__':
    extract_notes()
