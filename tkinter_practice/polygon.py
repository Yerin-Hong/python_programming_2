# polygon.py
# 다각형 그리기
"""
다각형(polygon)은 3개 이상의 선분으로 둘러싸인 도형. 삼각형이나 사각형도 다각형의 일종.
다각형을 사용하면 불규칙적인 형상도 유사하게 그릴 수 있음.
tkinter로 다각형을 그리려면 다각형의 각 점에 대한 좌표를 제공하면 됨.
"""
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")

root.mainloop()
