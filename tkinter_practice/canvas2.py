# canvas2.py
# 선과 사각형 그리기
from tkinter import *

# Tkinter 윈도우 생성
root = Tk()

# Canvas 생성 및 크기 설정
w = Canvas(root, width=300, height=200)
w.pack()

# 선 그리기(검은색_다른 옵션 필요 없음)
w.create_line(0, 0, 300, 200)   # (2)

# 선 그리기(빨간색)
w.create_line(0, 0, 300, 100, fill="red")   # (3)

# 파란색 사각형 그리기
w.create_rectangle(50, 25, 200, 100, fill="blue")

# Tkinter 이벤트 루프 실행
root.mainloop()