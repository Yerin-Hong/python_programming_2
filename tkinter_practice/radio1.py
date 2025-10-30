# radio1.py
# 라디오 버튼(radio button)은 체크박스랑 비슷하지만, 한 개의 버튼만 가능.

from tkinter import *

root = Tk()
choice = IntVar()

Label(root,
      text="가장 선호하는 프로그래밍 언어를 선택하시오.",
      justify=LEFT,
      padx=20).pack()

Radiobutton(root, text="Python", padx=20, variable=choice, value=1).pack(anchor=W)    # anchor 옵션은 W, E, N, S로 4가지. 전체 라디오버튼의 모든 게 한 번에 움직임
Radiobutton(root, text="C", padx=20, variable=choice, value=2).pack(anchor=W)
Radiobutton(root, text="Java", padx=20, variable=choice, value=3).pack(anchor=W)
Radiobutton(root, text="Swift", padx=20, variable=choice, value=4).pack(anchor=W)

root.mainloop()