# 동물 울음소리 버튼 GUI

# 클래스 구현
class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Duck(Animal):
    def speak(self):
        return "꽥꽥!"
    
# tkinter 구현
from tkinter import *

root = Tk()
root.title("동물 소리 듣기")
root.geometry("500x400")

# 틀짜기(아예 전체를 크게 3덩이로 나눠서 만들어주기)
frame1 = Frame(root)     # 젤 위 레이블(버튼 누르라는 안내문)
frame1.pack(pady=40)

frame2 = Frame(root)    # 가운데 버튼 3개 
frame2.pack(pady=40)

frame3 = Frame(root)    # 소리 나올 곳(처음엔 레이블)
frame3.pack(pady=40)

label1 = Label(frame1, text="동물 버튼을 눌러 소리를 들어보세요.")
label1.pack()

label3 = Label(frame3, text = "(여기에 울음소리가 나옵니다)")
label3.pack()

# 기능
def make_sound(animal):
    sound = animal.speak()
    label3.config(text=sound)

# 버튼 클릭 시 호출 함수
def dog_sound():
    make_sound(Dog())

def cat_sound():
    make_sound(Cat())
    
def duck_sound():
    make_sound(Duck())

dog_button = Button(frame2, text="강아지", command=dog_sound)
dog_button.pack(side="left") 

cat_button = Button(frame2, text="고양이", command=cat_sound)
cat_button.pack(side="left") 

duck_button = Button(frame2, text="오리", command=duck_sound)
duck_button.pack(side="left") 

root.mainloop()