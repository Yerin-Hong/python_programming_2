# pack2.py
# pack 배치 관리자
# 앞에서 pack 배치관리자를 이용해서 위아래로 세워둠, 이번에는 가로로 눕도록 변경
from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", bg="red", fg="white")
button2 = Button(root, text="버튼2", bg="green", fg="black")
button3 = Button(root, text="버튼3", bg="blue", fg="white")

# 이번에는 가로로 눞인 걸, 지들끼리 padding 넣어서 간격을 벌려줌. LEFT 기준이므로 padx(x축 기준 이동)
button1.pack(side=LEFT, padx=10)
button2.pack(side=LEFT, padx=10)
button3.pack(side=LEFT, padx=10)

root.mainloop()