# canvas_lab.py
# 사용자에게 색상 물어보기(사용자에게 채우기 색상, 외곽선 색상을 묻기.)
# 사각형 그리기. 버튼을 클릭 -> 색상 선택 대화상자로 색 선택 -> 확인버튼

from tkinter import *
from tkinter import colorchooser

# 사각형 그리기 함수
def draw_rectangle():
    fill_color = colorchooser.askcolor(title="채우기 색상 선택")[1]
    outline_color = colorchooser.askcolor(title="외곽선 색상 선택")[1]
    canvas.create_rectangle(50, 50, 200, 150, fill=fill_color, outline=outline_color)
# [1]이걸 하는 이유는 colorchooser.askcolor()함수는 ((좌표값), 16진수 색상코드) 이런 튜플 형태를 냄. 따라서 튜플의 16진수 색상 값인 [1]을 사용.

root = Tk()
 
canvas = Canvas(root, width=300, height=200)
canvas.pack()

button = Button(root, text="사각형 그리기", command=draw_rectangle)
button.pack()

root.mainloop()