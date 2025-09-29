# 레이블(label_2)
"""
레이블(Label) 위젯은 텍스트나 이미지를 표시하는 데 이용.(사용자 편집 불가)
레이블 위젯(GUI 기반 운영체제에서 사용하는 시각적 요소)은 Tkinter 라이브러리에서 제공하는 Label 클랴스를 사용해 생성.
"""

from tkinter import * 

root = Tk()

Label(root,
      text = "Times Font 폰트와 빨강색을 사용한다.", 
       fg = "red",
       font = "Times 32 bold italic").pack()
Label(root,
      text = "Helvetica 폰트와 녹색을 사용한다.",
      fg = "blue",
      bg = "yellow",
      font = "Helvetica 32 bold italic").pack()

root.mainloop()
