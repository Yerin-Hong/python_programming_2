# "GAME OVER" 텍스트 띄우면서, 재시작(재시작 버튼 누르면 시작)
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)   # 게임창이 항상 위로 있도록

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

# 게임 상태에 대한 변수(추가)
game_over = False # 게임 오버 상태
game_over_text = None 
restart_button_text = None   # 재시작 버튼

# 게임 재시작 함수
def restart_game(event=None):
    global game_over, game_over_text, restart_button_text

    # 상태 초기화
    game_over = False
    ball.hit_bottom = False

    if game_over_text:
        canvas.delete(game_over_text)
        game_over_text = None
    if restart_button_text:
        canvas.delete(restart_button_text)
        restart_button_text = None

    # 공 위치 초기화 및 속도 재설정
    ball.canvas.coords(ball.id, 245, 100, 260, 115) 
    ball.reset_ball() 

    # 패들 위치 초기화
    paddle.reset_position()

class Ball:
    def __init__(self, canvas, paddle, color):   # 공에게 패들이 추가된 것을 알려줌. Ball 클래스에 paddle 추가
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)   # 도형 ID
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100)   # canvas.move(객체ID, X방향이동, Y방향이동)

        self.reset_ball()

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def reset_ball(self):
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts
        self.y = -3

        # 공의 속도, 좌우로 움직이던 것을 수정
        starts = [-3, -2, -1, 1, 2, 3]   
        random.shuffle(starts)      # 리스트 순서를 섞기
        self.x = starts[0]          # 섞인 리스트의 첫 번째 값을 사용
        self.y = -3   # y 방향은 위로 -3 속도로 시작

        # 캔버스 높이 저장
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False   # 바닥에 닿았는지 여부를 저장하는 변수.

    # 패들에 닿았는지 확인하는 함수.
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)    # 패들의 위치 [px1, py1, px2, py2]

        # 가로 방향으로 공과 패들이 겹치는지 확인
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:    # 공의 아래쪽(y2)이 패들의 위 아래 사이에 있는지 확인.
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False
        
    def draw(self): 
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      # 현재 공의 위치 가져오기 [x1, y1, x2, y2]
        print(self.canvas.coords(self.id))   # 전 파일에서는 주석처리. 여기선 보여줌. 계속 위치를 보여주는거. 이제는 부딪힐 거니까.

        if pos[1] <= 0:  # 위쪽 벽에 닿으면 아래로 이동
            self.y = 3   # 속도수정
        if pos[3] >= self.canvas_height:   # 아래쪽(바닥)에 닿으면 위로 튕김.
            self.hit_bottom = True    # 바닥에 닿았을 경우 hit_bottom = True

        # 이미 바닥에 부딪혔으면 충돌 확인 X.
        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:   # 패들과 부딪혔는지 검사
                self.y = -3

        if pos[0] <= 0: # 왼쪽 벽에 닿으면 → 오른쪽으로 튕김
            self.x = 3
        if pos[2] >= self.canvas_width: # 오른쪽 벽에 닿으면 → 왼쪽으로 튕김
            self.x = -3

# 패들 클래스
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        # 초기 위치 저장
        self.start_x = 200

        self.x = 0   # 처음에는 안 움직임
        self.canvas_width = self.canvas.winfo_width()   # 너비를 저장하기(벽에 부딪히면 처리하기 위해서 설정)

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)   # 키보드 이벤트 연결
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        # 엔터키 누르면 재시작
        self.canvas.bind_all('<KeyPress-Return>', restart_game)

    def turn_left(self, evt):
        self.x = -2   # 왼쪽으로 이동하는 속도

    def turn_right(self, evt):
        self.x = 2    # 오른쪽으로 이동

    def draw(self):   # 패들을 x 방향으로만 이동
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        # 화면 왼쪽/오른쪽 끝을 넘지 않도록 구간 지정
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def reset_position(self):
        pos = self.canvas.coords(self.id)
        if pos:
            dx = self.start_x - pos[0] # 현재 위치와 초기 위치의 차이
            self.canvas.move(self.id, dx, 0)
        self.x = 0 # 이동 속도 초기화

paddle = Paddle(canvas, 'blue')    # 패들 객체 먼저 생성.
ball = Ball(canvas, paddle, 'red')   # paddle 속성 추가.

while True:
    # 게임 오버 상황(바닥에 닿았을 때)이 아닌 경우만 실행.
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()

    else:
        if not game_over:
            game_over = True # 게임 오버 상태 설정
            
            # GAME OVER 텍스트 표시
            game_over_text = canvas.create_text(
                250, 150,
                text="GAME OVER",
                font=('Helvetica', 30),
                fill='red'
            )
            
            # 재시작 버튼 텍스트 표시 (클릭 가능하도록)
            restart_button_text = canvas.create_text(
                250, 220,
                text="[클릭 또는 Enter 키로 재시작]",
                font=('Helvetica', 12),
                fill='green'
            )

            # 3. 재시작 버튼 클릭 이벤트 바인딩
            canvas.tag_bind(restart_button_text, '<Button-1>', restart_game)
            canvas.tag_bind(restart_button_text, '<Enter>', lambda event: canvas.config(cursor="hand2"))
            canvas.tag_bind(restart_button_text, '<Leave>', lambda event: canvas.config(cursor=""))


    tk.update_idletasks() #tkinter내부 작업 처리
    tk.update() 
    time.sleep(0.01)

tk.mainloop()