from tkinter import *
import random

btnList = [None] * 9
fnameList = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0
random.shuffle(fnameList)

window = Tk()
window.geometry("600x600")
window.title("랜덤 냥이")

for i in range(0,9):
    photoList[i] = PhotoImage(file="/Applications/무제 폴더/windowProgramming/"+fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 200
    xPos = 0
    yPos += 200

window.mainloop()