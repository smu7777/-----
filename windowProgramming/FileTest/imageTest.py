from tkinter import *

def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp=open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList=[]
        for k in range(0, YSIZE):
            data=int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()

def displayImage(image):
    global XSIZE, YSIZE
    rgbString=""
    for i in range(0, XSIZE):
        tmpString=""
        for k in range(0, YSIZE):
            data=image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)

#전역 변수 선언
window= None
canvas= None
XSIZE, YSIZE= 256, 256
inImage= []

#메인 코드
window= Tk()
window.title("흑백사진보기")
canvas= Canvas(window, height=XSIZE, width=YSIZE)
paper= PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image=paper, state="normal")

#파일 --> 메모리
filename='/Applications/무제 폴더/windowProgramming/Lenna.raw'
loadImage(filename)

#메모리 --> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()
