import tkinter as tk
import random   # 무작위로 이동해야 하니까.

class MovingShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Shape")

        # 캔버스 생성
        self.canvas = tk.Canvas(root, width = 800, height = 800, bg = "white")
        self.canvas.pack()

        # 원
        self.shape = self.canvas.create_oval(100, 100, 200, 200, fill = "blue")
        # create_oval()의 숫자는 좌표의미. 

        # 키보드 이벤트_키보드 자판(방향키)을 누르면 원 도형 이동
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # 마우스 이벤트_마우스를 누르면 원 도형 색상 변경
        self.canvas.bind("<B1-Motion>", self.change_color)

    # 이동과 관련된 메서드
    def move_shape(self, dx, dy):
        self.canvas.move(self.shape, dx, dy)
        # x, y 값을 받아서 사용하겠단 의미

    # Tkinter의 Canvas의 좌표계는 x축과 y축이 각각 좌표계의 위 끝과 왼쪽 끝을 의미.(아래 문자열과 같은 형태.)
    """ (0,0)------->x 
             |
             |
             |
             y
    """
    # 따라서 위 좌표를 기준으로 up, down 함수는 y축 기준 이동, left, rigth 함수는 x축 기준 이동으로 보면 됨.
    def move_up(self, event):
        self.move_shape(0, -10)

    def move_down(self, event):
        self.move_shape(0, 10)

    def move_left(self, event):
        self.move_shape(-10, 0)

    def move_right(self, event):
        self.move_shape(10, 0)

    # 색변경 메서드
    def change_color(self, event):
        colors = ["red", "orange", "green", "purple", "blue", "pink"]
        color = random.choice(colors)
        self.canvas.itemconfig(self.shape, fill = color)

root = tk.Tk()
app = MovingShapeApp(root)
root.mainloop()