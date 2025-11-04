# 일반적인 운송수단을 나타내는 클래스
class Vehicle:
    def __init__(self, make, model, color, price):
        self.make = make       # 메이커
        self.model = model     # 모델
        self.color = color     # 자동차의 색상
        self.price = price     # 자동차의 가격

    def setMake(self, make):      # 설정자 메소드
        self.make = make
    
    def getMake(self):            # 접근자 메소드
        return self.make

    # 차량에 대한 정보를 문자열로 요약해 반환
    def getDesc(self):
        return "차량=(" + str(self.make) + "," + \
                              str(self.model) + "," + \
                              str(self.color) + "," + \
                              str(self.price) + ")"
    
# 트럭 클래스를 정의할 때, Vehicle로부터 상속받음. Truck은 자식, Vehicle은 부모 클래스.
class Truck(Vehicle):           # Truck은 Vehicle의 모든 메소드와 인스턴스 변수를 상속받음. 
    def __init__(self, make, model, color, price, payload):
        super().__init__(make, model, color, price)         # 부모 클래스인 Vechicle의 생성자 호출. super()은 부모 클래스 의미.
        self.payload = payload       # Truck 클래스에 트럭의 적재용량을 나타내는 payload라는 인스턴스 변수를 추가.

    def setPayload(self, payload):     # Truck 클래스의 메소드를 추가한 것.(Vehicle의 메소드에서.)
        self.payload = payload

    def getPayload(self):
        return self.payload
    
# 테스트 코드
myTruck = Truck("Tisla", "Syber Truck", "white", 10000, 2000)    # 객체 생성
myTruck.setMake("Tesla")    # 설정자 메소드 호출
myTruck.setPayload(2000)    # 설정자 메소드 호출
print(myTruck.getDesc())    # 트럭 객체를 문자열로 출력