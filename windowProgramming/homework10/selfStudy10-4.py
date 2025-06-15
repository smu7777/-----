from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    englishKey = {
        "Left": "왼쪽 화살표",
        "Right": "오른쪽 화살표",
        "Up": "위쪽 화살표",
        "Down": "아래쪽 화살표"
    }
    
    koreanKey = englishKey.get(event.keysym, event.keysym)
    messagebox.showinfo("키보드 이벤트", "눌린 키: Shift + " + koreanKey)

window = Tk()

window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()