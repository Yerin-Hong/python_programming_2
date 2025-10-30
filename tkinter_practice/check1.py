# check1.py
# 해당하는 것을 모두 고르는 체크박스
from tkinter import *

root = Tk()
Label(root, text="선호하는 언어를 모두 고르세요").grid(row=0, sticky=W)    # grid는 배치관리자. 위젯을 격자 형태로 배치

value1 = IntVar()       # IntVar()는 Tkinter에서 제공하는 변수 클래스 중 하나, 정수(integer) 값을 저장하는 데 사용.
Checkbutton(root, text="Python", variable=value1).grid(row=1, sticky=W)
value2 = IntVar()
Checkbutton(root, text="C", variable=value2).grid(row=2, sticky=W)
value3 = IntVar()
Checkbutton(root, text="Java", variable=value3).grid(row=3, sticky=W)
value4 = IntVar()
Checkbutton(root, text="Swift", variable=value4).grid(row=4, sticky=W)

root.mainloop()