# Car와 SportsCar 클래스
class Car:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self):
        return f"현재 속도: {self.speed}km/h"

class SportsCar(Car):
    def __init__(self, speed, turbo):
        # 부모 클래스 __init__을 호출해서 speed 속성 설정
        super().__init__(speed)
        self.turbo = turbo  

    # 오버라이딩(get_speed() 재정의)
    def get_speed(self):
        if self.turbo == True:
            return f"현재 속도: 200km/h (터보 ON)"
        else:
            return f"현재 속도: 100km/h (터보 OFF)"
        
car1 = Car(80)
print(car1.get_speed())

sport1 = SportsCar(150, True)
print(sport1.get_speed())

sport2 = SportsCar(120, False)
print(sport2.get_speed())