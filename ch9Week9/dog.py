class Animal:
    def __init__(self, name=""):
        self.name = name
    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    # 여기부터는 강아지 클래스(자식)의 메서드
    def eat(self):
        print("강아지가 먹고 있습니다.")

d = Dog()
d.eat()