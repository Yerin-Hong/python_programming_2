# animation2.py
# 공이 두 개 움직이는 애니메이션. animation1.py와 동일하게 공이 자동으로 움직이게 만듦.
from tkinter import *

def move_ball(ball_id, dx, dy):
    canvas.move(ball_id, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball_id)
    if x2 < 400:    # 오른쪽 끝에 도달하지 않았을 때만 실행
        root.after(50, move_ball, ball_id, dx, dy)

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

id1 = canvas.create_oval(10, 100, 50, 150, fill="green")
id2 = canvas.create_oval(10, 200, 50, 250, fill="blue")

move_ball(id1, 3, 0)       # 두 개의 공 동시에 이동
move_ball(id2, 5, 0)

root.mainloop()