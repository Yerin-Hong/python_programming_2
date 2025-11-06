class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):          # Dog is an Animal.(is-a 클래스 간의 유형적 관계. 부모의 기능을 물려받음. 상속)
    def speak(self):
        print("멍멍!")

dog = Dog()
dog.speak()