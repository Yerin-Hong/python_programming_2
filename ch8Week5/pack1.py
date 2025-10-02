# 다양한 옵션을 사용하여 pack() 메서드를 호출하여 버튼을 배치하는 방식을 조정할 수 있음.
# side 매개변수를 사용해 버튼을 좌측이나 우측으로 배치 가능.
# fill 매개변수를 사용해 버튼을 수평으로 확장 가능.(창의 너비를 채우기 가능)

from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text = "버튼 1", bg = "red", fg = "white")
button2 = Button(root, text = "버튼 2", bg = "green", fg = "white")
button3 = Button(root, text = "버튼 3", bg = "blue", fg = "white")
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

root.mainloop()