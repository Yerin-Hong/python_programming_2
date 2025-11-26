# 문제 2. Person - Pet 관계(has-a) + speak() 호출

from tkinter import *

# 1. class Pet
class Pet():
    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet = None):
        self.name = name
        self.pet = pet

# 전역 객체 생성
person = Person("홍길동")

# 3. 동작 요구
# 버튼 클릭 시 실행할 함수

# 강아지 선택 --> Dog() 생성해 Person.pet에 할당 --> 선택 완료 메세지 출력
def select_dog():
    # Dog 인스턴스를 생성(원래면 dog = Dog()인데(has-a라서.), 지금은 person 객체의 pet 속성에 할당)
    person.pet = Dog()
    result_label.config(text="강아지를 선택했습니다.")

# 고양이 선택 --> Cat() 생성해 Person.pet에 할당 --> //
def select_cat():
    person.pet = Cat()
    result_label.config(text="고양이를 선택했습니다.")

# 동물 선택을 안하고 말하기를 누르는 경우
def selet_spaek_first():
    if person.pet is None:
        result_label.config(text="동물을 먼저 선택해주세요.")
        return
    
    speak_result = person.pet.speak()
    final_message = f"{person.name}의 반려동물 --> {speak_result}"
    result_label.config(text=final_message)

# 2. TKinter UI 구성
# 순서상의 이유로 동작 구현이 먼저임.
root = Tk()
root.title("문제2")
root.geometry("400x200")

guide_label = Label(root, text="동물을 선택해 주세요.")
guide_label.pack(pady=10)

# 강아지 / 고양이 선택 버튼과 말하기 버튼을 배치하기 위한 frame
frame1 = Frame(root)
frame1.pack(pady=10)

frame2 = Frame(root)
frame2.pack(pady=10)

# 버튼(강아지랑 고양이는 나란히, 말하기는 그 아래에 배치)
button_dog = Button(frame1, text="강아지 선택", command=select_dog)
button_dog.pack(side=LEFT, padx=5)

button_cat = Button(frame1, text="고양이 선택", command=select_cat)
button_cat.pack(side=LEFT, padx=5)

button_speak = Button(frame2, text="말하기", command=selet_spaek_first)
button_speak.pack()

# 결과 라벨(버튼아래)
result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()