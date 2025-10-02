# 체크박스

from tkinter import *

root = Tk()
Label(root, text = "선호하는 언어를 모두 선택하시오.").grid(row = 0, sticky = W)

# Python
value1 = IntVar()
Checkbutton(root, text = "Python", valiable = value1).grid(row = 1, sticky = W)

value2 = IntVar()
Checkbutton(root, text = "C", valiable = value1).grid(row = 1, sticky = W)

value1 = IntVar()
Checkbutton(root, text = "Java", valiable = value1).grid(row = 1, sticky = W)

value1 = IntVar()
Checkbutton(root, text = "swift", valiable = value1).grid(row = 1, sticky = W)

root.mainloop()
