from tkinter import *
window= Tk()
window.title("냥이들")

photo1= PhotoImage(file='/Applications/무제 폴더/windowProgramming/8.png')
photo2= PhotoImage(file='/Applications/무제 폴더/windowProgramming/9.png')
# 맥이에요
label1= Label(window, image=photo1)
label2= Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()