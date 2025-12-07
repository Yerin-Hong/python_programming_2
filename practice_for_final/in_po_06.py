"""
동물 울음소리 버튼 GUI
1. Animal --> Dog, Cat, Duck 클래스 정의.
- 각각 speak() 오버라이딩(멍멍!, 야옹!, 꽥꽥!)

2. Tkinter 윈도우 제목: "동물 소리 듣기!"
-버튼 3개: "강아지", "고양이", "오리"
-버튼 클릭 시 해당 객체 생성 후 Label에 울음소리 출력.
-다형성을 이용해 같은 make_sound(animal) 함수에서 처리
"""
import tkinter as tk

# 1) 상속 / 다형성 모델
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

# 2) Tkinter GUI
# 동물소리를 내는 기능을 tkinter 에서도 정의를 해줘야함.
def make_sound(animal: Animal):
    sound = animal.speak()
    result_label.config(text=sound)

root = tk.Tk()
root.title("동물 소리 듣기")
root.geometry("360x180")
root.resizable(False, False)

# 안내 문구
tk.Label(root, text="동물 버튼을 눌러 소리를 들어보세요.").pack(pady=(12, 6))

# 버튼 프레임
btns = tk.Frame(root)
btns.pack(pady=4)

# 버튼 프레임 안에 버튼
tk.Button(btns, text="강아지", width=10, command=lambda: make_sound(Dog())).pack(side="left", padx=6)
tk.Button(btns, text="고양이", width=10, command=lambda: make_sound(Cat())).pack(side="left", padx=6)
tk.Button(btns, text="오리", width=10, command=lambda: make_sound(Duck())).pack(side="left", padx=6)

# 결과 라벨(StringVar 없이 text 직접 사용)
result_label = tk.Label(root, text="(여기에 울음소리가 나옵니다)", font=("맑은 고딕", 14, "bold"))
result_label.pack(pady=16)

root.mainloop()