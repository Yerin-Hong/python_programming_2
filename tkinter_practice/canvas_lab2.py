# canvas_lab2.py
 # 랜덤한 사각형 그리기. 윈도우 하나 만들고, 랜덤한 사각형(크기, 위치 모두) 생성
from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width=500, height=400)
canvas.pack()
color = ["red", "orange", "yellow", "green", "blue", "violet"]

def draw_rect():
    x = random.randint(0, 500)    # x축은 캔버스 사이즈 따라(너비)
    y = random.randint(0, 400)    # y축은 캔버스 사이즈 따라(높이)
    w = random.randrange(100)     
    h = random.randrange(100)
    canvas.create_rectangle(x, y, w, h, fill=random.choice(color))

for i in range(10):
    draw_rect()

root.mainloop()