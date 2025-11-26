# 상품 할인 계산 클래스
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, rate):
        self.price -= self.price * rate    # 공식: 할인된 가격 = 원가 - (원가*할인율)

    def get_info(self):
        print(f"상품명: {self.name}, 가격: {int(self.price)}원")   # int() 안해주면, 출력결과가 27000.0원으로 나옴.

p1 = Product("운동화", 30000)
p1.discount(0.1)
p1.get_info()    # 상품명: 운동화, 가격: 27000원