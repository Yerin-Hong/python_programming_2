# canvas1.py
# tkinter 에서는 canvas라는 위젯을 윈도우 위에 생성한 후에 캔버스에 그림을 그릴 수 있음
# Canvas 위젯은 도형, 텍스트, 이미지 등 다양한 그래픽 요소를 그리는 함수를 가지고 있음

from tkinter import *

root = Tk()

w = Canvas(root, width=300, height=200)
w.pack()

root.mainloop()