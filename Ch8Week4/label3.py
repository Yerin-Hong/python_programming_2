# 이미지 표시 레이블

from tkinter import *
root = Tk()
photo = PhotoImage(file = "dog2.gif")
label = Label(root, image=photo)
label.pack()
root.mainloop()