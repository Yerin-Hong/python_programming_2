class BankAccount:
    def __init__(self, owner, balance = 0):
        self.__owner = owner        # 얘랑
        self.__balance = balance    # 얜 바뀌어도 됨
        print(f"{owner}의 계좌가 생성되었습니다.")

    def getOwner(self):
        return self.__owner
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance < 0:
            print("잔액은 0원 미만일 수 없습니다.")
        else:
            self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"통장에 {amount}원이 입금되었습니다.")
            return self.__balance
        else:
            print("0보다 큰 금액만 입금 가능합니다.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"통장에서 {amount}원이 출금되었습니다.")
            return self.__balance
        else:
            print("잔액이 부족합니다")

# 객체 생성
owner = input("계좌 주인의 이름을 입력하세요: ")

a = BankAccount(owner)
b = BankAccount("김민수")

a.deposit(100)
b.deposit(100)
a.withdraw(30)
b.withdraw(30)

print(f"{a.getOwner()}의 계좌의 현재 잔액: ", a.get_balance())
print(f"{b.getOwner()}의 계좌의 현재 잔액: ", b.get_balance())

a.set_balance(500)
print(f"{a.getOwner()} 계좌의 수정된 잔액: ", a.get_balance())