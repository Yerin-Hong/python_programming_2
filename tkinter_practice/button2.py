# button2.py
# 파란색 배경과 노란색 텍스트가 있는 버튼, 너비(width) = 30, 높이(height) = 10
from tkinter import *

root = Tk()

button = Button(
    text="This is button!",
    width = 30,
    height = 10,
    bg = "blue",
    fg = "yellow"
)

button.pack()
root.mainloop()