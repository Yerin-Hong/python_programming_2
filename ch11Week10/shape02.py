# 기본 도형 클래스는 밑변과 높이를 가짐. 기본 도형 클래스를 상속받아서 삼각형(Triangle) 클래스 작성하고 삼각형의 넓이를 계산.

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def get_area(self):
        return (self.width * self.height) / 2

tri = Triangle(4, 6)
print(f"삼각형의 밑변: {tri.width}")
print(f"삼각형의 높이: {tri.height}")
print(f"삼각형의 넓이: {tri.get_area()}")