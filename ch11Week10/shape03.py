# calculate_area()메서드를 가지는 도형 클래스 작성
# 도형 클래스를 상속받아 원과 사각형을 나타내는 클래스를 정의하고 각각의 면적을 계싼하는 calculate_area()메서드를 오버라이딩해 반환
# 다양한 도형 클래스의 인스턴스를 리스트로 입력받아 calculate_area()메서드를 호출해 모든 도형의 넓이를 합산하는 함수

import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
def total_area(shapes):
    total = 0
    for s in shapes:
        total += s.calculate_area()
    return total

c = Circle(5)
r = Rectangle(4, 6)

print(f"Circle의 면적: {c.calculate_area():.2f}")
print(f"Rectangle의 면적: {r.calculate_area():.2f}")
print(f"도형들의 총 넓이: {total_area([c, r]):.2f}")