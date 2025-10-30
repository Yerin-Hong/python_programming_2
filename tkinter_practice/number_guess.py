# number_guess.py
# 사용자가 컴퓨터가 생성한 숫자(1~100 중 랜덤)를 알아맞히는 게임.
from tkinter import *
import random

answer = random.randint(1, 100)    # 컴터가 랜덤으로 정할 수(사용자가 맞힐 정답)

def guessing():     # 사용자 시도시 실행
    guess = int(guessFiled.get())

    if guess > answer:
        msg = "높음"
    elif guess < answer:
        msg = "낮음"
    else:
        msg = "정답!"

    resultLabel["text"] = msg   # 비교하고 큰지 작은지 정답인지 알려줌
    guessFiled.delete(0, 5)     # 입력창 내용 삭제(다음 입력을 위해)
    # entry 창의 텍스트를 지운다는 거 --> delete(시작인덱스, 끝인덱스)

def reset():        # 초기화 버튼 누를 때 실행
    global answer
    answer = random.randint(1, 100)    # 리셋하고 새로운 랜덤수 생성
    resultLabel["text"] = "다시 한 번 하세요"

root = Tk()
root.configure(bg="white")
root.title("숫자를 맞혀보세요")
root.geometry("500x100")

# 젤 위 레이블
titleLabel = Label(root, text="숫자 게임에 오신 것을 환영합니다!", bg="white")
titleLabel.pack()

# 사용자 입력창
guessFiled = Entry(root)
guessFiled.pack(side="left")

# 시도 버튼 --> 클릭하면 guessing() 함수 실행
tryButton = Button(root, text="시도", bg="white", fg="green", command=guessing)
tryButton.pack(side="left")

# 초기화 버튼 --> 클릭하면 reset() 함수 실행
resetButton = Button(root, text="초기화", bg="white", fg="red", command=reset)
resetButton.pack(side="left")

# 젤 아래 레이블
resultLabel = Label(root, text="1부터 100 사이의 숫자를 입력하세요.", bg="white")
resultLabel.pack(side="left")

root.mainloop()