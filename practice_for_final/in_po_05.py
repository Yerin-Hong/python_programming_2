"""
음식 배달 시스템(오버라이딩 + 조건처리)
1. Food 클래스: name, price
-__str__() --> 메뉴: 김밥, 가격: 3000원"

2. DeliveryFood 클래스: delivery_fee(배달비) 속성 추가.
-__str__() 오버라이딩 --> 메뉴: 김밥, 총 가격: 4000원(배달비 포함)"

3. Order 클래스
-add_food()로 음식 객체를 리스트에 추가.
-show_order()로 전체 주문 출력.

4. DeliveryFood와 Food가 섞여 있어도 다형성으로 각각의 __str__() 호출
"""

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"메뉴: {self.name}, 가격: {self.price}원"
    
class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)       # 상위 클래스의 속성을 상속받는 경우에 super() 사용.
        self.delivery_fee = delivery_fee

    def __str__(self):
        return f"메뉴: {self.name}, 총 가격: {self.price + self.delivery_fee}(배달비 포함)"

class Order:
    def __init__(self):
        self.foods = []

    def add_food(self, food):
        self.food = food    # 생략하고 다음 줄만 실행해되 됨.
        self.foods.append(food)
    
    def show_order(self):
        print("=== 주문 내역 ===")
        # foods 리스트 내부의 모든 내용을 출력해야 되니까 for문 사용.
        for f in self.foods:
            print(f)     # __str__() 자동 호출(다형성)
"""마지막에 __str__()이 자동으로 호출되는 이유는 
print() 함수가 내부적으로 어떤 과정을 거쳐서 __str__을 반환하기 때문."""

"""다형성은 하나의 인터페이스가 서로 다른 종류의 객체에 대해 다른 동작을 수행하는 것 의미.
Food, DeliveryFood 객체 모두 print(f)라는 동일한 코드 작성(하나의 인터페이스).
그러나 파이썬에서 어떤 클래스의 인스턴스인지 확인, 그 객체에 맞는 __str__ 메서드를 선택적으로 호출.
--> 객체의 실제 타입에 따라 적절한 메서드가 호출되는 현상. 메서드 오버라이딩을 통한 다형성."""

f1 = Food("김밥", 3000)
f2 = DeliveryFood("짜장면", 6000, 2000)

order = Order()
order.add_food(f1)
order.add_food(f2)
order.show_order()