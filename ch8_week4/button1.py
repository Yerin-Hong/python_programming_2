# 버튼
# 버튼(Button)은 사용자와 상호작용을 목적으로 설계된 위젯. 클릭할 때마다 함수 호출.

from tkinter import *

def button_clicked():
    print("버튼이 클릭됨.")

root = Tk()     # 부모 위젯 생성
root.geometry("300x200")      

button = Button(root, text = "클릭하세요", command = button_clicked)    # 버튼 위젯 생성
button.pack()

root.mainloop()