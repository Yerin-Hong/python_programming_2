# entry1.py
# 이름이나 이메일 주소와 같이, 사용자로부터 한 줄의 텍스트를 가져와야 하는 경우에 Entry 위젯을 씀
from tkinter import *

def get_entry_value():
    value = entry.get()
    print("입력된 값: ", value)

# 순서는 윈도우 창 만들고, 엔트리 위젯 생성하고(한 줄 문자를 받을 거), 그 아래에 버튼 위젯을 생성
root = Tk()
root.geometry("300x200")

entry = Entry(root)     # 엔트리 위젯 생성
entry.pack()

button = Button(root, text = "확인")    # 버튼 위젯 생성
button.pack()

root.mainloop()