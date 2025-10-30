# button1.py
from tkinter import *

def button_clicked():
    print("버튼이 클릭되었습니다.")

root = Tk()     # 부모 위젯 생성
root.geometry("300x200")

button = Button(root, text = "클릭하세요", command=button_clicked)   # 버튼 생성 위젯, command는 컴터로 시스템이나 장치에 특정 기능 실행하는 지시하기 위한 정보나 신호.
button.pack()

root.mainloop()