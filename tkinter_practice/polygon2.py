# polygon2.py
# 다각형의 좌표 지정시 리스트를 사용하는 경우
from tkinter import *

w = 300
h = 200
root = Tk()

w = Canvas(root, width=w, height=h)
w.pack()

points = [0, 0, 80, 150, 250, 20]
w.create_polygon(points, outline="red", fill="yellow", width=5)   # width는 outline(테두리) 두께

root.mainloop()
