# 6.5,6.5p_02수정전 코드
# 클래스 생성
class Dog:
    def __init__(self, name, age, tricks):    # 생성자 메서드
        self.name = name
        self.age = age
        self.tricks = tricks
    
    # 메서드 추가
    def bark(self):
        print(f"{self.name}가 짖고 있습니다!")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")

    # 새로운 메서드를 추가해서 원하는 형태로 결과를 출력해주기(아래 문제 해결)
    def show_tricks(self):
        tricks_str = ', '.join(self.tricks)
        # 리스트나 튜플같은 시퀀스의 항목을 '' 안의 값으로 구분해서 결합('and'면 뒹굴기 and 달리기)
        print(f"{self.name}의 장기는 {tricks_str}입니다.")

# 객체 생성(= 개 인스턴스 생성)
dog1 = Dog("바둑이", 3, ["뒹굴기", "달리기"]) 
dog2 = Dog("멍멍이", 5, ["먹기"])
"""
수정전 코드로 출력하면 이런 식으로 그대로 출력됨 --> 이걸 원하는 게 아님.
["뒹굴기", "달리기"]
["먹기"]
"""

# 개가 짖는 메서드 호출
dog1.bark()
dog2.bark()

# 개 정보(이름, 나이) 메서드 호출
dog1.info()
dog2.info()

"""수정전
print(f"{dog1.name}의 장기는 {dog1.tricks} 입니다.")
print(f"{dog2.name}의 장기는 {dog2.tricks} 입니다.")
"""

# 수정후
dog1.show_tricks()
dog2.show_tricks()
