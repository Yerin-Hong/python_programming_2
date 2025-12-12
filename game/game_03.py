# 내가 원하는 기능 추가(막대 바가 상하좌우로 움직이는 기능 추가)

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
game_over = False
game_over_text = None
restart_button_text = None

# 점수 관련
score = 0
score_text = None

# 점수 표시
def draw_score():
    global score_text, score

    # 전 판의 점수 지우기
    if score_text is not None:
        try:
            canvas.delete(score_text)
        except Exception:
            pass

    score_text = canvas.create_text(
        40, 20,
        text=f"Score: {score}",
        font=('Helvetica', 15),
        fill='black'
    )

# 게임 재시작
def restart_game(event=None):
    global game_over, game_over_text, restart_button_text, score
    score = 0
    draw_score()

    game_over = False

    # 글자 삭제
    if game_over_text is not None:
        try:
            canvas.delete(game_over_text)
        except Exception:
            pass
    if restart_button_text is not None:
        try:
            canvas.delete(restart_button_text)
        except Exception:
            pass

    # 공, 패들 초기화
    try:
        canvas.coords(ball.id, 245, 100, 260, 115)
        ball.reset_ball()
        ball.hit_bottom = False
    except Exception:
        pass

    try:
        paddle.reset_position()
    except Exception:
        pass

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

        self.reset_ball()

    def reset_ball(self):
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        # 캔버스 크기 최신화
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if not paddle_pos:
            return False

        if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and
            pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
            return True
        return False

    def draw(self):
        global score
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # 위쪽 벽 충돌
        if pos[1] <= 0:
            self.y = abs(self.y)

        # 바닥 닿음 체크
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        # 패들과 충돌
        if not self.hit_bottom:
            if self.hit_paddle(pos):
                self.y = -abs(self.y)  # 위로 튕기기
                score += 1
                draw_score()

        # 좌우 벽 반사
        if pos[0] <= 0:
            self.x = abs(self.x) if self.x != 0 else 3
        if pos[2] >= self.canvas_width:
            self.x = -abs(self.x) if self.x != 0 else -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # 초기 위치
        self.start_x = 200
        self.start_y = 300
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, self.start_x, self.start_y)

        self.x = 0
        self.y = 0

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        # 키 
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop_x)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop_x)

        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)
        self.canvas.bind_all('<KeyRelease-Up>', self.stop_y)
        self.canvas.bind_all('<KeyRelease-Down>', self.stop_y)

        # 엔터로 재시작
        self.canvas.bind_all('<KeyPress-Return>', restart_game)

    # 함수 재정의
    def turn_left(self, evt):
        self.x = -6

    def turn_right(self, evt):
        self.x = 6

    def stop_x(self, evt):
        self.x = 0

    def turn_up(self, evt):
        self.y = -4

    def turn_down(self, evt):
        self.y = 4

    def stop_y(self, evt):
        self.y = 0

    def draw(self):
        # 이동
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # 좌우 경계 처리
        if pos[0] < 0:
            self.canvas.move(self.id, -pos[0], 0)
        if pos[2] > self.canvas_width:
            self.canvas.move(self.id, self.canvas_width - pos[2], 0)

        # 상하 경계 처리
        if pos[1] < 0:
            self.canvas.move(self.id, 0, -pos[1])
        if pos[3] > self.canvas_height:
            self.canvas.move(self.id, 0, self.canvas_height - pos[3])

    def reset_position(self):
        pos = self.canvas.coords(self.id)
        if pos:
            dx = self.start_x - pos[0]
            dy = self.start_y - pos[1]
            self.canvas.move(self.id, dx, dy)
        self.x = 0
        self.y = 0

# 객체 생성
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

draw_score()

# 메인 루프
while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    else:
        if not game_over:
            game_over = True
            game_over_text = canvas.create_text(
                250, 150,
                text="GAME OVER",
                font=('Helvetica', 30),
                fill='red'
            )
            restart_button_text = canvas.create_text(
                250, 220,
                text="[클릭 또는 Enter 키로 재시작]",
                font=('Helvetica', 12),
                fill='green'
            )
            # 클릭하면 재시작
            canvas.tag_bind(restart_button_text, '<Button-1>', restart_game)
            canvas.tag_bind(restart_button_text, '<Enter>', lambda e: canvas.config(cursor="hand2"))
            canvas.tag_bind(restart_button_text, '<Leave>', lambda e: canvas.config(cursor=""))

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
