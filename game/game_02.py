# game_01.py에 점수 계산 기능 추가

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

# 게임 상태에 대한 변수
game_over = False # 게임 오버 상태
game_over_text = None 
restart_button_text = None   # 재시작 버튼

# (추가) 점수 관련 변수
score = 0     
score_text = None # 점수 텍스트 ID


# 점수 표시
def draw_score():
    global score_text, score
    # 이전 텍스트가 있으면 지움
    if score_text is not None:
        try:
            canvas.delete(score_text)
        except:
            pass

    score_text = canvas.create_text(
        40, 20, # 캔버스 왼쪽 위에 위치
        text="Score: %s" % score,
        font=('Helvetica', 15),
        fill='black'
    )

# 게임 재시작 함수
def restart_game(event=None):
    global game_over, game_over_text, restart_button_text, score, score_text, ball, paddle

    # 점수 초기화
    score = 0
    draw_score()    # 점수 실시간 반영
    
    # 상태 초기화
    game_over = False
    if hasattr(ball, 'hit_bottom'):
        ball.hit_bottom = False

    if game_over_text is not None:
        try:
            canvas.delete(game_over_text)
        except:
            pass
        game_over_text = None
        
    if restart_button_text is not None:
        try:
            canvas.delete(restart_button_text)
        except:
            pass
        restart_button_text = None

    # 공 위치 초기화 및 속도 재설정
    try:
        canvas.coords(ball.id, 245, 100, 260, 115)
        ball.reset_ball()
    except:
        pass

    # 패들 위치 초기화
    try:
        paddle.reset_position()
    except:
        pass

class Ball:
    def __init__(self, canvas, paddle, color):   # 공에게 패들이 추가된 것을 알려줌. Ball 클래스에 paddle 추가
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)   # 도형 ID
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100)   # canvas.move(객체ID, X방향이동, Y방향이동)

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

        self.reset_ball()

    def reset_ball(self):
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts
        self.y = -3

        # 좌우 시작 속도 후보에서 하나를 골라 설정
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
        if not paddle_pos:
            return False

        # 공과 패들이 가로 및 세로 방향으로 겹치는지 확인
        # pos = [x1, y1, x2, y2]
        # paddle_pos = [px1, py1, px2, py2]
        if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and
            pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
            return True
        return False
        
    def draw(self): 
        global score
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      # 현재 공의 위치 가져오기 [x1, y1, x2, y2]
        
        # 위쪽 벽 충돌
        if pos[1] <= 0:
            self.y = 3

        # 바닥에 닿으면 hit_bottom 플래그
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        # 패들과 충돌 검사 (바닥에 아직 닿지 않았을 때만)
        if not self.hit_bottom:
            if self.hit_paddle(pos):
                self.y = -3
                score += 1
                draw_score()

        # 좌우 벽 충돌 처리
        if pos[0] <= 0:
            self.x = abs(self.x) if self.x <= 0 else self.x
            if self.x == 0:
                self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -abs(self.x) if self.x >= 0 else self.x
            if self.x == 0:
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

        # 키보드 이벤트 연결
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop_movement)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop_movement)

        # 엔터키 누르면 재시작
        self.canvas.bind_all('<KeyPress-Return>', restart_game)

    def turn_left(self, evt):
        self.x = -6   # 왼쪽으로 이동하는 속도 (조정)

    def turn_right(self, evt):
        self.x = 6    # 오른쪽으로 이동

    def stop_movement(self, evt):
        # 키에서 손을 떼면 멈춤
        self.x = 0

    def draw(self):   # 패들을 x 방향으로만 이동
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        # 화면 왼쪽/오른쪽 끝을 넘지 않도록 구간 지정
        if pos[0] <= 0:
            # 되돌리기
            self.canvas.move(self.id, -pos[0], 0)
            self.x = 0
        elif pos[2] >= self.canvas_width:
            overshoot = pos[2] - self.canvas_width
            self.canvas.move(self.id, -overshoot, 0)
            self.x = 0

    def reset_position(self):
        pos = self.canvas.coords(self.id)
        if pos:
            dx = self.start_x - pos[0] # 현재 위치과 초기 위치의 차이
            self.canvas.move(self.id, dx, 0)
        self.x = 0 # 이동 속도 초기화

paddle = Paddle(canvas, 'blue')    # 패들 객체 먼저 생성.
ball = Ball(canvas, paddle, 'red')   # paddle 속성 추가.

draw_score()    # 게임 시작 시 점수판 초기화

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
                text="여기를 클릭하거나 ENTER키를 누르시오",
                font=('Helvetica', 12),
                fill='green'
            )

            # 재시작 텍스트에 이벤트 바인딩
            canvas.tag_bind(restart_button_text, '<Button-1>', restart_game)
            canvas.tag_bind(restart_button_text, '<Enter>', lambda event: canvas.config(cursor="hand2"))
            canvas.tag_bind(restart_button_text, '<Leave>', lambda event: canvas.config(cursor=""))

    tk.update_idletasks() #tkinter내부 작업 처리
    tk.update() 
    time.sleep(0.01)

tk.mainloop()