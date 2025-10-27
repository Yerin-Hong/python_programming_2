class BankAccount:
  def __init__(self, balance, owner, amount):     # __init__에서 인자 3개를 만들었는데, 객체 생성할 때 1개의 인자만 전달함, balance 초기값 설정도 문제(balance = 0)으로 초기화
    self.__balance = balance
    self.__owner = owner    
    self.__amount = amount     # _amount 변수(멤버 변수)는 다른 메서드에서 안 쓰는데, 여기서 불러옴

  # 접근자(getter)
  def getOwner(self):
    return self.__owner
  def get_balance(self):
    return self.__balance

  # 설정자(setter)
  def set_balance(self, amount):   # 여기도 문제, amount가 아니라, balance를 바꿔여 하는데 amount를 변경중
    if  amount < 0:
        # print("잔액은 0원 미만일 수 없습니다")
        self.__amount = 0    # self.__balance
    else:
        self.__amount = amount    # self.__balance = amount여야함.

  def withdraw(self, amount):   
    if amount <= self.__balance:    
        self.__balance -= amount
        print(f"통장에 {amount}가 입금되었음.")    # withdraw는 출금
        return self.__balance
    else:
       print("잔액이 부족합니다")

  def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
        print(f"통장에서 {amount}가 출금되었음.")     # deposit은 입금
        return self.__balance
    else:
        print("0보다 큰 금액만 입력 가능")

owner = input("계좌 주인의 이름을 입력하시오")
print(f"{owner}의 계좌가 생성되었습니다")

a = BankAccount("A")     # 이게 아니라, owner을 받아줘야함 # a = BankAccounter(owner)
b = BankAccount("B")

a.deposit(100)
b.deposit(100)
a.withdraw(30)      
b.withdraw(30)
print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())     # a. getOwner() 접근자를 만들어줘서 그걸 써줘야함.
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:", a.get_balance())