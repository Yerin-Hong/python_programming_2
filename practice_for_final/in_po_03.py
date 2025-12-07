"""
Bird 클래스와 오버라이딩
1. Bird: fly()는 "새가 날고 있습니다.
2. Penguin: Bird를 상속받고, fly() 오버라이딩 --> "펭귄은 날지 못합니다."
3. 객체 두 개 생성 후, 각각의 결과 출력
"""

class Bird:
    def __init__(self):
        pass

    def fly(self):
        print("새가 날고 있습니다.")
    
class Penguin(Bird):
    def fly(self):
        print("펭귄은 날지 못합니다.")

# 실행예시
b = Bird()
p = Penguin()

b.fly()
p.fly()