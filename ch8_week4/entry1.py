# 엔트리
# 이름이나 이메일 주소와 같이, 사용자로부터 한 줄의 텍스트를 가져와야 하는 경우, 엔트리(Entry) 위젯 사용

from tkinter import *

def get_entry_value():
    value = entry.get()
    print("입력된 값:", value)

root = Tk()     # 부모 위젯 생성
root.geometry("300x200")

entry = Entry(root)   # 엔트리 위젯 생성
entry.pack()     # 엔트리 위젯 배치

button = Button(root, text = "확인", command = get_entry_value)      # 버튼 위젯 생성
button.pack()

root.mainloop()