from tkinter import *

def callback():
    """클릭함수: 버튼이 클릭되면 호출되어 버튼의 텍스트를 변경."""
    button["text"] = "버튼이 클릭되었음!"


# Tkinter 윈도우 생성
root = Tk()

# 버튼 생성 및 콜백 함수와 연결
button = Button(root, text="클릭", command=callback)
button.pack(side = LEFT)

root.mainloop()     # Tkinter 이벤트 루프 실행