from tkinter import *

root = Tk()
root.geometry("420x440")
root.title("중간고사 7번")
canvas = Canvas(width=400, height=320, bg = "white")

frame = Frame(root, width=200, height=100)

b1 = Button(root, text="사각형")
b2 = Button(root, text="원")
b3 = Button(root, text="그림")
b4 = Button(root, text="지우기")