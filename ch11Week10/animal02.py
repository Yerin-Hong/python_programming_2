# 소리를 내는 make_sound() 메서드를 가지는 동물 클래스 작성
# 개 클래스는 동물 클래스를 상속받아 make_sound() 메서드를 오버라이딩해 "멍멍" 출력. 동일 방식으로 고양이 클래스는 "야옹"
class Animal:
    def __init__(self):
        pass 

class Dog(Animal):
    def make_sound(self):
        return "멍멍"

class Cat(Animal):
    def make_sound(self):
        return "야옹"
    
dog = Dog()
cat = Cat()

print(f"강아지 소리: {dog.make_sound()}")
print(f"고양이 소리: {cat.make_sound()}")