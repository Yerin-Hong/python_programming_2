# mouse_evt.py
# 마우스 이벤트 처리(마우스 번호가 눌리는 걸, 좌표로 받는거)
from tkinter import *

def left_click(event):
    print(f"좌측 버튼이 ({event.x}, {event.y})에서 클릭되었습니다.")    # 실제 예제에서는 모두 x만 받고있는데, 난 x, y 둘 다 받는 걸로 수정

def right_click(event):
    print(f"우측 버튼이 ({event.x}, {event.y})에서 클릭되었습니다.")

root = Tk()

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-3>", right_click)
frame.pack()

root.mainloop()

# 마우스 버튼 번호 정리
"""
<Button-1>: 왼쪽 버튼 클릭
<Button-2>: 가운데 버튼 클릭(보통 휠)
<Button-3>: 오른쪽 버튼 클릭
<Button-4>: 마우스 휠 위로 스크롤
<Button-5>: 마우스 휠 아래로 스크롤
"""