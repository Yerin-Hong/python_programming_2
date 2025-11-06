# 1. Dog has an Animal
class Animal:
    def move(self):
        print("동물이 움직입니다.")

class Dog:
    def __init__(self):
        self.animal = Animal()      # 포함관계(Dog는 Animal을 가짐)
       
    def move(self):
        self.animal.move()      # Animal의 행동 사용
        print("개가 달립니다.")

dog = Dog()
dog.move()

# 2. Student has a Person
class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Student:
    def __init__(self):
        self.person = Person()      # Student는 Person을 가짐.

    def study(self):
        self.person.speak()     # 포함된 Person의 행동 사용
        print("학생이 공부를 합니다")

stu = Student()
stu.study()

# 3. Car has a Vehicle
class Vehicle:
    def drive(self):
        print("차량이 이동 중입니다.")

class Car:
    def __init__(self):
        self.vehicle = Vehicle()        # Car은 Vehicle을 가짐.

    def drive(self):
        self.vehicle.drive()        # Vehicle의 기능 사용
        print("자동차가 도로를 달립니다.")

car = Car()
car.drive()

# 4. Manager has an Employee
class Employee:
    def work(self):
        print("직원이 일합니다.")

class Manager:
    def __init__(self):
        self.employee = Employee()      # Manager은 Employee를 가짐
    
    def work(self):
        self.employee.work()        # Employee의 기능 사용.
        print("관리자가 팀을 관리합니다.")

m = Manager()
m.work()

# 5. Penguin has a Bird
class Bird:
    def fly(self):
        print("새가 날아갑니다.")

class Penguin:
    def __init__(self):
        self.bird = Bird()      # Penguin은 Bird를 가짐

    def fly(self):
            self.bird.fly()     # Bird의 기능을 사용
            print("펭귄은 날지 못하지만 수영을 합니다.")

p = Penguin()
p.fly()