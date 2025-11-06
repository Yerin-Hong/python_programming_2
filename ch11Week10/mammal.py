# 종과 나이를 가지는 포유류(종, 나이) 클래스를 작성한 후에 포유류 클래스를 상속해 사람 클래스(종류, 나이, 이름, 직업)를 작성
class Mammal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
class Person(Mammal):
    def __init__(self, species, age, name, job):
        super().__init__(species, age)         # super() 메서드로 상속해서, 부모 클래스의 기능을 그대로 불러옴.
        self.name = name
        self.job = job
    
m1 = Mammal("동물", 30)
p1 = Person("동물", 30, "Kim", "Engineer")

print(f"포유류: {m1.species}, {m1.age}")
print(f"사람: {p1.name}, {p1.age}, {p1.job}")