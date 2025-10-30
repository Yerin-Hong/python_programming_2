# animation.py
# 공이 움직이는 애니메이션(왼쪽에서 오른쪽으로)
"""
일정한 간격으로 조금씩 달라지는 그림을 그리면 애니메이션 됨.
"""
from tkinter import *

def move_oval():
    canvas.move(id, 3, 0)
    if canvas.coords(id)[2] < 400:    # 오른쪽 끝(width=400이므로)에 도달하기 전까지만 반복
        root.after(50, move_oval)     # 50ms 후에 move_oval 함수 호출

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

id = canvas.create_oval(10, 100, 50, 150, fill="green")
move_oval()    # move_oval 함수 호출

root.mainloop()
