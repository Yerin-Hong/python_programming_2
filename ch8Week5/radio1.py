# 예제(radio1)
from tkinter import *

root = Tk()
choice = IntVar()

Label(root,
      text = "가장 선호하는 프로그래밍 언어를 선택하시오",
      justify = LEFT,
      padx = 20).pack()

# Python 버튼
Radiobutton(root, text = "Python", padx = 20, variable = choice,
            value = 1).pack(anchor = W)

# C 버튼
Radiobutton(root, text = "C", padx = 20, variable = choice,
            value = 2).pack(anchor = W)

# Java 버튼
Radiobutton(root, text = "Java", padx = 20, variable = choice,
            value = 3).pack(anchor = W)

# Swift 버튼
Radiobutton(root, text = "Swift", padx = 20, variable = choice,
            value = 4).pack(anchor = W)


root.mainloop()
