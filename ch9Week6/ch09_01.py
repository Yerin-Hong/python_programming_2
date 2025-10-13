# 클래스 생성
class Dog:
    def __init__(self, name, age):    # 생성자 메서드
        self.name = name
        self.age = age
    
    # 메서드 추가
    def bark(self):
        print(f"{self.name}가 짖고 있습니다!")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")

# 객체 생성(= 개 인스턴스 생성)
dog1 = Dog("바둑이", 3) 
dog2 = Dog("멍멍이", 5)

# 개가 짖는 메서드 호출
dog1.bark()
dog2.bark()

# 개 정보(이름, 나이) 메서드 호출
dog1.info()
dog2.info()