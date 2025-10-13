class BankAccount(object):

    interest_rate = 0.3     # 은행이율(클래스 변수)

    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance    # 인스턴스 변수

    # 입금 메소드(잔고 증가)
    def diposit(self, amount):
        self.balance += amount
        print("입금 성공!")

    # 출금 메소드(잔고 감소)
    def withdraw(self, amount):
        # 출금의 경우, 내 balance가 출금하려는 amount보다 커야지만 출금 가능. 따라서 if로 조건 제약.
        if self.balance >= amount:
            self.balance -= amount
            print("인출 성공!")
        else:
            print(f"출금희망 금액: {amount}, 현재 잔액: {self.balance}\n잔액이 부족합니다.")

# 객체 생성
account = BankAccount("Kim", "12345678", 1000)
print("초기 잔고: ", account.balance)

account.diposit(500)
print("저축 후 잔고: ", account.balance)

account.withdraw(200)
print("인출 후 잔고: ", account.balance)

# 잔액보다 출금 희망 금액이 더 큰 경우(balance <= amount)
account.withdraw(20000)
        