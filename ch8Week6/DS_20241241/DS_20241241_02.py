class BankAccount:
  def __init__(self, balance, owner, amount):
    self.__balance = balance
    self.__owner = owner
    self.__amount = amount

  def getOwner(self):
    return self.__owner

  def get_balance(self):
    return self.__balance

  def set_balance(self, amount):
    if  amount < 0:
        self.__amount = 0
    else:
        self.__amount = amount

  def withdraw(self, amount):
    if amount <= self.__balance:
        self.__balance -= amount
        print(f"통장에 {amount}가 입금되었음.")
        return self.__balance
    else:
       print("잔액이 부족합니다")

  def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
        print(f"통장에서 {amount}가 출금되었음.")
        return self.__balance
    else:
        print("0보다 큰 금액만 입력 가능")

owner = input("계좌 주인의 이름을 입력하시오")
print(f"{owner}의 계좌가 생성되었습니다")

a = BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(100)
a.withdraw(30)
b.withdraw(30)
print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:", a.get_balance())