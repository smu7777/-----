from tkinter import *

fnameList= ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]
photoList= [None] * 9
num=0

def clickNect():
    global num
    num += 1
    if num > 8:
        num = 0
    photo= PhotoImage(file="/Applications/무제 폴더/windowProgramming/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image= photo
    fileName.configure(text=fnameList[num])

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo= PhotoImage(file="/Applications/무제 폴더/windowProgramming/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image= photo
    fileName.configure(text=fnameList[num])

window= Tk()
window.geometry("700x500")
window.title("냥이 앨범 보기")

btnPrev= Button(window, text="<< 이전", command=clickPrev)
btnNext= Button(window, text="다음 >>", command=clickNect)

photo= PhotoImage(file="/Applications/무제 폴더/windowProgramming/"+fnameList[0]) ##초기값인가?
pLabel= Label(window, image=photo)
fileName= Label(window, text=fnameList[0])


btnPrev.place(x=220, y=10)
btnNext.place(x=430, y=10)
fileName.place(x=340, y=10)
pLabel.place(x=15, y=50)

window.mainloop()