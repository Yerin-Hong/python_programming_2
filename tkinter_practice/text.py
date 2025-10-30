# text.py
# 텍스트 그리기
"""
create_text()는 텍스트의 중앙 위치를 나타내는 (x, y) 좌표와 표시할 텍스트가 전달되는 매개 변수 text를 가짐
다음 코스에서는 (100, 100) 위치에 간단한 텍스트를 표시함.
"""
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=200)
canvas.pack()
canvas.create_text(200, 100, text="Hello World", fill="blue", font=('Courrier', 30))

root.mainloop()