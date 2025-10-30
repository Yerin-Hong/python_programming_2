 # calculator2.py
# 파이썬을 이용해 버튼을 가지는 계산기 작성. 실제 계산기 모양(배치 관리자 중요)
from tkinter import *

def click(key):
    if key == '=':     # "=" 버튼이면 수식을 계산해 결과를 표시.
        try:
            result = eval(entry.get())
            entry.delete(0, END)     # 기존 입력 지우기
            entry.insert(END, str(result))     # 결과 출력
        except:
            entry.insert(END, "오류!")
    elif key == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, key)

root = Tk()
root.title("간단한 계산기")

buttons = [
'7', '8', '9', '+', 'C',
'4', '5', '6', '-', ' ',
'1', '2', '3', '*', ' ',
'0', '.', '=', '/', ' ']     # 이 형태를 그대로 유지하는 각각의 버튼 생성

# 버튼은 반복문으로 생성
i = 0
for b in buttons:
    cmd = lambda x = b: click(x)     # 버튼 클릭시 click(x) 실행
    b = Button(root, text=b, width=5, relief='ridge', command=cmd)
    b.grid(row=i//5+1, column=i%5)
    i+=1

# 엔트리 위젯은 맨 윗줄의 셀에 걸쳐서 배치됨.
entry = Entry(root, width=33, bg="yellow")
entry.grid(row=0, column=0, columnspan=5)

root.mainloop()