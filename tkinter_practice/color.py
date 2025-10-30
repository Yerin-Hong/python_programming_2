# color.py
# 색상. 대부분의 위젯은 생성 시에 배경(bg)과 전경(fg) 변수를 사용해 위젯 및 텍스트 색상을 지정할 수 있음
# 색을 지정하려면 색상 이름(영어)를 사용하면 됨. 예를 들어, red, white, blue와 같은 색상의 이름을 사용하면 됨.

from tkinter import *

root = Tk()

button = Button(root, text="버튼을 클릭하세요")
button.pack()
button["fg"] = "yellow"
button["bg"] = "green"

root.mainloop()