# 문제 4. 과목 선택 프로그램(Person - Student - Teacher)
from tkinter import *

class Person:
    def __init__(self, name: str):
        self.name = name

class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        # 수강 과목 리스트
        self.classes = []  

    def enrollCourse(self, subject: str):
        if subject not in self.classes:
            self.classes.append(subject)

    def clearCourses(self):
        self.classes.clear()

# Tkinter 구현.
root = Tk()
root.title("문제 4")
root.geometry("380x280")

# 객체 생성
stu = Student("홍길동") 

title = Label(root, text=f"학생: {stu.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=5)

frm = Frame(root)
frm.pack(pady=10, anchor="center")

# Checkbutton 상태 변수, 모두 해제되어 있는 상태
var_py  = IntVar(value=0)
var_ai  = IntVar(value=0)
var_ds  = IntVar(value=0)

# Checkbutton 3개
cb1 = Checkbutton(frm, text="Python", variable=var_py)
cb2 = Checkbutton(frm, text="AI", variable=var_ai)
cb3 = Checkbutton(frm, text="DataScience", variable=var_ds)

cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

# 결과 표시 라벨
result = StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb = Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)

# 동작 함수들
def register_courses():# 현재 체크 상태를 기준으로 과목 리스트 갱신
    stu.clearCourses()
    if var_py.get(): stu.enrollCourse("Python")
    if var_ai.get(): stu.enrollCourse("AI")
    if var_ds.get(): stu.enrollCourse("DataScience")

    # 결과 표시
    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0); var_ai.set(0); var_ds.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")

# 버튼 영역
frame = Frame(root)
frame.pack(pady=6)

Button(frame, text="등록하기", command=register_courses).pack(side="left", padx=8)
Button(frame, text="초기화", command=reset_all).pack(side="left", padx=8)

root.mainloop()