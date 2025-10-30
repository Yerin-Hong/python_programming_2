# label1.py 
from tkinter import *

root = Tk()    # 윈도우 창 생성
root.geometry("300x200")    # 윈도우 크기 설정

label = Label(root, text = "Hello, World!")    # 레이블 위젯 생성
label.pack()    # 라벨 크기를 글자에 맞게 축소

root.mainloop()  