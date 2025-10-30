# arc.py
# 호(arc)는 원의 일부. 호도 타원이랑 마찬가지로 사각형을 지정해 그림. 
# 추가되는 매개 변수 extent를 사용해 각도를 지정함

from tkinter import *
root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_arc(10, 10, 200, 150, extent=90, style=ARC)

root.mainloop()