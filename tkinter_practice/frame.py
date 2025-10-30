# frame.py
# 프레임 위젯은 다른 위젯을 담을 수 있는 컨데이너 역할. 프레임은 일종의 빈 집합. 다른 위젯 그룹화하거나 배치할 때 사용
from tkinter import *

root = Tk()
root.geometry("300x200")

frame = Frame(root, width=200, height=100)    # Frame 위젯생성
frame.pack()

button1 = Button(frame, text="버튼1")   # 버튼1
button1.pack(side="left")

button2 = Button(frame, text="버튼2")   # 버튼2
button2.pack(side="right")

root.mainloop()
