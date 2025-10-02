from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text = "버튼1", bg = "red", fg = "white")
button2 = Button(root, text = "버튼2", bg = "green", fg = "white")
button3 = Button(root, text = "버튼3", bg = "blue", fg = "white")

# pady는 상단과 하단에 픽셀을 추가하고, padx는 왼쪽 및 오른쪽에 픽셀 추가
button1.pack(side = LEFT, padx=10)
button2.pack(side = LEFT, padx=10)
button3.pack(side = LEFT, padx=10)

root.mainloop()