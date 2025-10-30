# pack1.py
# pack 배치 관리자
# 앞에서 pack 배치관리자를 이용해서 위아래로 세워둠, 이번에는 가로로 눕도록 변경
from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", bg="red", fg="white")
button2 = Button(root, text="버튼2", bg="green", fg="black")
button3 = Button(root, text="버튼3", bg="blue", fg="white")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

root.mainloop()