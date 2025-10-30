# paint.py
# 마우스 그림 그리기
"""
마우스를 드래그래 그림을 그리는 프로그램. 윈도우 내에서 클랙하고 드래그해 그림을 그림.
마우스를 움직일 때마다 이전 위치와 현재 위치를 연결하는 선 생성
"""

import tkinter as tk

# 시작 좌표를 저장할 전역 변수
start_x = start_y = 0

# 그림 그리기 시작하는 지점을 설정하는 함수
def start_drawing(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

# 그림 그리기 함수
def draw(event):
    global start_x, start_y
    end_x, end_y = event.x, event.y
    # 시작점과 종료점을 연결하는 선을 생성하고 캔버스에 그림
    canvas.create_line(start_x, start_y, end_x, end_y, fill="black")
    start_x, start_y = end_x, end_y

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# 마우스 왼쪽 버튼 클릭 이벤트와 마우스 드래그 이벤트에 함수 연결
canvas.bind("<Button-1>", start_drawing)   # 마우스 왼쪽 버튼 클릭
canvas.bind("<B1-Motion>", draw)   # 마우스 드래그
# 마우스 오른쪽 버튼 클릭의 경우에는 <Button-3>

root.mainloop()