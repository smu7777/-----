from tkinter import *
window = Tk()

button1= Button(window, text="파이썬 종료", fg="red", command=quit)
label1= Label(window, text="하지마라",fg="black", font=("Arial", 50))

button1.pack()
label1.pack()
window.title("윈도우창 연습")
window.mainloop()