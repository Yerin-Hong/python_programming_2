# 왼쪽엔 글씨, 오른쪽엔 사진
from tkinter import *

root = Tk()
photo = PhotoImage(file="images.jpg")
w = Label(root ,image=photo, justify="left").pack(side="right")
message = """배고프다 진짜 너무너무 배고프다
졸리다 피곤한데 뭔가를 한 게 없어서 잘 수도 없다
집에 엄마가 케이크 있댔는데
내일 오전수업이라 케이크 먹으러 가면 5시 버스타고 돌아와야 돼서
도저히 섣부른 선택을 할 수가 없다."""
w2 = Label(root,
           padx=10,
           text=message).pack(side="left")
root.mainloop()