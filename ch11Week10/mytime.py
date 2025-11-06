# __str__()은 객체의 문자열 표현을 반환
# 예를 들어, 시간을 나타내는 클래스인 Time에서 __str__()은 다음과 같음.
class MyTime:
    def __init__(self, hour, minute, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%.2d:%.2d:%.2d"%(self.hour, self.minute, self.second)
    
time = MyTime(10, 25)
print(time)