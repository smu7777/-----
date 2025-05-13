from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지버튼", "강아지가 귀엽죠?")

window = Tk()

photo=PhotoImage(file="/Applications/무제 폴더/windowProgramming/스크린샷 2025-05-09 오전 12.26.07.png")
button=Button(window, image=photo, command=myFunc)
button.pack()

window.mainloop()