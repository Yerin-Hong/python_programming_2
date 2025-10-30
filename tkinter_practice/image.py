# image.py
# 이미지 표시하기
"""
tkinter에서 이미지를 표시하려면 먼저 이미지를 로드한 후에 create_image() 함수 사용.
tkinter가 읽을 수 있는 이미지 파일은 PNG 파일과 JPG 파일.(다른 파일 읽으려면 PIL(Python Imaging Library)기능 이용)
"""

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

img = PhotoImage(file="C:\Users\82103\Desktop\images.jpg")
canvas.create_image(20, 20, anchor=NW, image=img)

root.mainloop()