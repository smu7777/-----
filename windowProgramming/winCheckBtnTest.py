from tkinter import *
from tkinter import messagebox
window= Tk()

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("체크박스", "체크박스가 꺼졌습니다.")
    else:
        messagebox.showinfo("체크박스", "체크박스가 켜졌습니다.")

chk= IntVar()
cb1= Checkbutton(window, text="체크박스", variable=chk, command=myFunc)
cb1.pack()

window.mainloop()