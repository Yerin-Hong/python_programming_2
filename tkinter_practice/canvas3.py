# canvas3.py
# 캔버스의 그래픽 요소들
"""
캔버스 위젯에 추가된 항목(선, 사각형, 원)들은 삭제하기 전까지 유지됨.
만약 그리기 속성을 변경하고 싶으면, coords(), itemconfig(), move() 를 상ㅅㅇ
필요 없으면 delete()로 삭제
"""

from tkinter import *

root = Tk()

w = Canvas(root, width=300, height=200)
w.pack()

i = w.create_line(0, 0, 300, 200, fill="red")   #  (1)
w.coords(i, 0, 0, 300, 100)     # coordinaton system. 좌표 변경
w.itemconfig(i, fill="blue")    # 색상 변경

# w.delete(i)   # 삭제
# w.delete(ALL)    # 모든 항목 삭제

root.mainloop()