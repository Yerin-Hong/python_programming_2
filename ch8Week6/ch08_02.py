# 이미지 4개를 하나씩 불러오는 코드

import tkinter as tk
from PIL import ImageTk, Image
import os    # 이건 디렉토리를 지정해주는 거.

# 현재의 파이썬 파일이 있는 폴더 기준으로 경로 설정. 이걸 마치 전역변수처럼 사용. 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 내가 채워넣을 부분(시험의 경우)
def update_image():
    global current_index

    # 일반적인 경우(이 방식을 쓰면 현재와 같이 사진 파일이 코드 파일과 함께 있는 경우에 실행되지 않는 문제 발생.)
    # 현재 이미지 파일 경로 생성(폴더 경로 + 파일명)
    # image_path = image_files[current_index]
    image_path = os.path.join(BASE_DIR, image_files[current_index])

    # 이미지 열기
    image = Image.open(image_path)

    # 크기 조정(예: 400x300으로 고정)
    image = image.resize((400, 300))

    # Tkinter용 PhotoImage 객체로 변환
    photo = ImageTk.PhotoImage(image)

    # Label1 위젯에 이미지 표시
    image_label.config(image = photo)
    image_label.image = photo

    # 다음 이미지 인덱스로 이동(마지막이면 0으로 돌아감) --> 여기선 이미지가 계속 돌아오기를 원하는 거니까, 0 1 2 3 다음이 다시 0임.
    current_index = (current_index + 1) % len(image_files)
    # 일정 시간이 지나면 다시 update_image 실행 --> 0 1 2 3 4%4=0 1 2 3 --> 이런식으로 나머지 연산자를 쓰면 다시 돌아가게 됨(처음으로)
    # 이런 식으로  
    root.after(interval, update_image)

# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Image Slider")

# 
image_files = ["image1.png", "image2.png", "image3.png", "image4.png"]

interval = 2000   # (2000 == 2초)
current_index = 0    # 이미지를 가지고 오는 인덱스는 0부터 시작.

image_label = tk.Label(root)
image_label.pack()

# 이미지 업데이트 시작
update_image()

# 애플리케이션 실행
root.mainloop()

