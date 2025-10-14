# 텍스트가 부드럽게 움직이거나 색상이 바뀌는 등의 애니메이션 효과를 가진 프로그램(animate_text)

import tkinter as tk
import random
import time   # 시간차에 대한 걸 쓸 거라, time 불러옴
import random

def animate_text(canvas, text_id):
    for i in range(10):    # 텍스트를 10번 반복
        update_text_size(canvas, text_id)
        update_text_color(canvas, text_id)
        canvas.update()
        time.sleep(0.5)
    
def update_text_size(canvas, text_id):
    current_size = 100
    new_size = current_size + random.randint(-100, 100)
    canvas.itemconfigure(text_id, font = ("Helvetica", new_size))

def update_text_color(canvas, text_id):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "yellow"]
    new_color = random.choice(colors)
    canvas.itemconfigure(text_id, fill = new_color)

# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Text Animation")

canvas = tk.Canvas(root, width = 400, height = 200)
canvas.pack()

text_id = canvas.create_text(200, 100, text = "Hello", font = ("Helevetica", 12), fill = "black")

# 애니메이션 실행
animate_text(canvas, text_id)

# 애플리케이션 실행
root.mainloop()
