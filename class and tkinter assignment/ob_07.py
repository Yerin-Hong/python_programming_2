# 환율 계산 프로그램 만들기
class ExchangeRate:
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate
    
    # 달러 -> 원화
    def to_won(self, amount):
        won = amount * self.rate
        return won
    
    # 원화 -> 달러
    def to_dollar(self, amount):
        dollar = amount / self.rate
        return dollar

    # 환율을 새로운 값으로 변경
    def update_rate(self, new_rate):
        self.rate = new_rate    # 환율을 새로 갱신하는 거니까, self.rate에 new_rate를 갱신.
        print(f"{self.currency} 환율이 {self.rate}원으로 변경됨.")

    def info(self):
        print(f"통화: {self.currency}, 현재 환율: {self.rate}원")
    
usd = ExchangeRate("USD", 1440)
usd.info()
print("100달러=", usd.to_won(100), "원")
print("270000원=", round(usd.to_dollar(270000), 2), "달러")

usd.update_rate(1440)
print("100달러=", usd.to_won(100), "원")