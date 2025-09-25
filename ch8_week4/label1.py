# 예제(label.py)
from tkinter import *

root = Tk()     # 윈도우 생성
root.geometry("300x200")    # 창의 크기 설정

label = Label(root, test = "Hello, World!")   # 레이블 위젯 생성
label.apck()      # 레이블 배치

root.mainloop()     # 이벤트 루프 시작.