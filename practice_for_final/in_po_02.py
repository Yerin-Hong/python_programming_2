"""
Vehicle과 Truck클래스
1. Vehicle: drive() 정의하지 않음.
2. Truck: Vehicle을 상속받아 drive() → "트럭이 화물을 운송합니다."
3. Car: Vehicle을 상속받아 drive() → "승용차가 사람을 태우고 있습니다."
4. 리스트로 관리하며 반복문으로 호출
"""

class Vehicle:
    def drive(self):
        pass

class Truck(Vehicle):
    def drive(self):
        return "트럭이 화물을 운송합니다."
    
class Car(Vehicle):
    def drive(self):
        return "승용차가 사람을 태우고 있습니다."
    
vehicles = [Truck(), Car(), Truck()]      # 임의.

for v in vehicles:
    print(v.drive())