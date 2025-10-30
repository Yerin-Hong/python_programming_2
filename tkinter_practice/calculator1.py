# calculator1.py
# 계산기_파이썬과 동일한 수식 사용

from tkinter import *
from math import *

# eval() 함수를 호출해서 사용자가 입력한 수식을 계산. 
# 레이블의 configure()를 호출하여 레이블의 텍스트를 변경
def calculate(event):
    label.configure(text="결과" + str(eval(entry.get())))

root = Tk()

Label(root, text="파이썬 수식 입력: ").pack()

entry = Entry(root)

# 엔트리 위젯에서 엔터키를 치면 calculator()가 호출되게 연결.
# <Return> 이벤트는 엔터키를 입력하면 실행
entry.bind("<Return>", calculate)
entry.pack()

# 결과
label = Label(root, text="결과:")
label.pack()

root.mainloop()