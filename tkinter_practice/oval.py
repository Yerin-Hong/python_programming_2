# oval.py
# 타원 그리기. 타원을 그리려면 타원을 둘러싸는 사각형을 지정하면 됨. 타원은 지정된 사각형 안에 그려짐
from tkinter import *
root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_oval(10, 10, 200, 150)

root.mainloop()