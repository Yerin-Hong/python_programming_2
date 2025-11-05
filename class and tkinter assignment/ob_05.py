# 자동차 주행기록 프로그램
class Car:
    def __init__(self, model, odometer=0):  # 기본 주행거리 = 0
        self.model = model
        self.odometer = odometer

    def drive(self, km):
        self.odometer += km         # drive로 주행거리를 km만큼 증가.

    def info(self):
        return f"모델: {self.model}, 주행거리: {self.odometer}km"   # info()로 문자열 반환(return)

c = Car("BMW")
c.drive(50)
c.drive(70)
print(c.info()) # 모델: BMW, 주행거리: 120km