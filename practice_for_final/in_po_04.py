"""
Computer와 Laptop 클래스(상속과 오버라이딩)
1. Computer
속성: brand, price
get_info(): "브랜드: LG, 가격: 150만 원" 출력
2. Laptop: weight 속성 추가
3. get_info() 오버라이딩: "브랜드: LG, 가격: 150만 원, 무게: 1.5kg"
"""

class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        return f"브랜드: {self.brand}, 가격: {self.price}만 원"
    
class Laptop(Computer):
    def __init__(self, brand, price, weight):
        super().__init__(brand, price)
        self.weight = weight

    def get_info(self):
        return f"브랜드: {self.brand}, 가격: {self.price}만 원, 무게: {self.weight}kg"

# 실행 예시
com = Computer("LG", 150)
lap = Laptop("LG", 150, 1.5)

print(com.get_info())
print(lap.get_info())