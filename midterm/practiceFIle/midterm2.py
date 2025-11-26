class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0   # 인스턴스 변수 balance는 각 계좌별로 잔액을 관리하므로 초기값은 0.
        print(f"{self.owner} 계좌가 생성되었습니다.")

    # 접근자(getter)
    def get_balance(self):
        return self.__balance

    # 설정자(setter)
    def set_balance(self, amount):
        if amount >= 0:
            self.balance = amount
        else:
            print("잔액은 음수가 될 수 없습니다.")

    # 입금(deposit)과 출금(withdraw) 메서드 작성
    def deposit(self, amount):
        if amount >= 0:
           self.__balance += amount
           print(f"{self.owner} 통장에 {amount}원이 입금되었습니다.")     
        else:
            print("0보다 큰 금액만 입금 가능")

    def withdraw(self, amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} 통장에서 {amount}원이 출금되었습니다.")
        else:
            print("잔액보다 많은 금액은 출금이 불가능합니다.")

a = BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner}계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner}계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner}계좌의 수정된 잔액:", a.get_balance())