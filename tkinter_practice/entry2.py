# entry2.py
# 두 개의 엔트리 위젯을 사용해 사용자의 이름과 나이를 입력받는 프로그램

from tkinter import *

def submit():
    name = entry_name.get()
    age = entry_age.get()
    print("이름: ", name)
    print("나이: ", age)

root = Tk()
root.geometry("300x200")

Label(root, text="이름:").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="나이:").pack()
entry_age = Entry(root)
entry_age.pack()

button_submit = Button(root, text = "제출", command = submit)
button_submit.pack()

root.mainloop()