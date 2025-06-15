from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    # Shift + 화살표 키 조합일 때 키 이름 해석
    key_names = []

    if event.state & 0x0001:  # Shift 키가 눌렸는지 확인
        key_names.append("Shift")

    # keysym으로 방향키 확인
    if event.keysym == "Down":
        key_names.append("아래쪽 화살표")
    elif event.keysym == "Up":
        key_names.append("위쪽 화살표")
    elif event.keysym == "Left":
        key_names.append("왼쪽 화살표")
    elif event.keysym == "Right":
        key_names.append("오른쪽 화살표")
    else:
        key_names.append(event.keysym)

    messagebox.showinfo("키보드이벤트", "눌린 키는 " + " + ".join(key_names) + " 입니다")

window = Tk()
window.bind("<Shift-Down>", keyEvent)
window.mainloop()
