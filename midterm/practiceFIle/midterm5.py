# Student 클래스 정의, __eq__() 메서드
class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def __eq__(self, other):
        # Student 객체끼리만 비교(학번이 같으면 같은 학생)
        if isinstance(other, Student):      # 비교 대상(other)이 Student 클래스의 객체인지 확인.
            return self.stu_id == other.stu_id
            # 두 객체의 학번이 같으면 True 반환
        return False

# 등록된 학생 목록 및 로그인 함수
# 등록된 학생 목록(주어짐.)
students = [
    Student("202501", "김민수"),
    Student("202502", "이수정"),
    Student("202503", "박지훈")
]

# 로그인 확인 함수
def check_student():
    sid = e_id.get()
    name = e_name.get()
    user = Student(sid, name)    # 입력한 학번/이름으로 객체 생성

    if user in students:    # __eq__() 메서드 자동으로 호출
        result_label.config(text=f"{name} 학생, 로그인 성공!", fg = "blue")
    else:
        result_label.config(text="등록되지 않은 학번입니다.", fg = "red")


# tkienr 
from tkinter import *

# 윈도우 생성
root = Tk()
root.title("중간고사 5번")
root.geometry("250x150")

# 라벨 및 입력창
Label(root, text = "학번").grid(row=0, column=1, padx=10, pady=5)
Label(root, text = "이름").grid(row=1, column=1, padx=10, pady=5)

e_id = Entry(root)
e_name = Entry(root)

e_id.grid(row=0, column=1, padx=10, pady=5)
e_name.grid(row=1, column=1, padx=10, pady=5)

# 버튼
Button(root, text="로그인", command=check_student).grid(row=2, column=0, sticky=W, pady=8)
Button(root, text="취소", command=root.quit).grid(row=2, column=1, sticky=W, pady=8)

# --- 결과 출력 라벨 ---
result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()