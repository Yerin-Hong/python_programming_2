# complex.py
# 여러 배치 관리자 혼용하기
from tkinter import *

root = Tk()
root.geometry("300x100")

# 버튼 3개를 frame안에 배치
f = Frame(root)

b1 = Button(f, text="버튼1", bg="red", fg="white")
b2 = Button(f, text="버튼2", bg="green", fg="black")
b3 = Button(f, text="버튼3", bg="blue", fg="white")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

# 레이블을 수평으로 놓인 3개의 버튼 위에 배치하고 루트 윈도우에 수직으로 프레임 배치
l = Label(root, text="이 레이블은 버튼들 위에 배치된다.")
l.pack()
f.pack()

root.mainloop()