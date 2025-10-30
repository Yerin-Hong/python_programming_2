class Inventory:
    def _init__(self, stock):
        self.__stock = stock
        print("새 상품이 등록되었습니다.")

    def get_stock(self):
        return self.__stock

    def set_stock(self, amount, stock):
        if amount < 0:
            print("재고는 0개 이상이어야 합니다.")
        else:
            self.__stock = stock
    
    def add_stock(self, amount):
        if amount < 0:
            print("0보다 큰 수량만 입고 가능")
        else:
            self.__stock += amount


    def remove_stock(self, amount, stock):
        if amount < stock:
            print("현재 재고보다 큰 수량은 출고 불가능")
        else:
            self.__stock -= amount

amount = int(input("재고의 수량을 입력하세요"))

item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:", item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())