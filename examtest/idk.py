from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text="입력된 값")
label1.pack()

filename = askopenfilename(parent = window, filetypes = (("GIF 파일","*.gif"),("모든 파일","*.*")))
saveFp = asksaveasfilename(parent = window, mode = "w", defaultextension = ".txt", filetypes = (("JPG 파일","*.jpg;*"),("모든 파일","*.*")))
label1.configure(text = saveFp)
saveFp.close()
