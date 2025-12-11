import tkinter as tk

class Person:
    def __init__(self, name: str):
        self.name = name

class HobbyPerson(Person):
    def __init__(self, name: str):
        super().__init__(name)
        
        self.hobbies = []  # has-a: 취미 리스트

    def add_hobby(self, hobby):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)

    def clear_hobbies(self):
        self.hobbies.clear()


# tkinter
root = tk.Tk()
root.title("문제 2")
root.geometry("380x260")

stu = HobbyPerson("김덕성") #객체 생성
title = tk.Label(root, text=f"이름: {stu.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=6)

frm = tk.Frame(root)
frm.pack(pady=8, anchor="center")

# RadioButton 상태 변수, 모두 해제되어 있는 상태
var_g  = tk.IntVar(value=0)
var_rb  = tk.IntVar(value=0)
var_w  = tk.IntVar(value=0)

# Radiobutton 3개
rb1 = tk.Radiobutton(frm, text="게임",      variable=var_g, value=1)
rb2 = tk.Radiobutton(frm, text="독서",        variable=var_rb ,value=2)
rb3 = tk.Radiobutton(frm, text="운동", variable=var_w ,value=3)

rb1.grid(row=0, column=0, padx=8, pady=4)
rb2.grid(row=0, column=1, padx=8, pady=4)
rb3.grid(row=0, column=2, padx=8, pady=4)

# 결과 표시 라벨
result = tk.StringVar(value="취미를 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)

# 동작 함수들
def select_hobby():# 현재 체크 상태를 기준으로 리스트 갱신
    stu.clear_hobbies()
    if var_g.get(): stu.add_hobby("게임")
    if var_rb.get(): stu.add_hobby("독서")
    if var_w.get(): stu.add_hobby("운동")

    # 결과 표시
    if stu.hobbies:
        result.set(f"현재 선택된 취미: {', '.join(stu.hobbies)}")
    else:
        result.set("선택된 취미가 없습니다.")

def reset_all():
    var_g.set(0); var_rb.set(0); var_w.set(0)
    stu.clear_hobbies()
    result.set("모든 선택을 해제했습니다.")

# 버튼 영역
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(btn_frame, text="등록하기", command=select_hobby).pack(side="left", padx=8)
tk.Button(btn_frame, text="초기화",   command=reset_all).pack(side="left", padx=8)

root.mainloop()