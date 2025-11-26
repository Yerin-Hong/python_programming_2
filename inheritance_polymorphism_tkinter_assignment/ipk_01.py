# 문제 1. Vehicle 계층과 다형적 drive() (is-a) + tkinter 버튼

from tkinter import *

# 1. 부모 클래스 Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    # drive() 메서드를 자식 클래스에서 반드시 오버라이딩할 것이므로 pass로 넘어가줌.
    def drive(self):
        pass

# 2. 자식 클래스
class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."
    
class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."
    
# 3. 객체 생성
car = Car("car1")
truck = Truck("truck1")

# 4. Tkinter 구성
root = Tk()
root.title("문제1")
root.geometry("400x300")

# 안내 라벨(버튼 위)
guide_label = Label(root, text="버튼을 눌러보세요.")
guide_label.pack(pady=10) 

# 버튼 클릭 시 실행할 함수.
def car_drive():
    result_text = car.drive()
    # 라벨의 텍스트 수정(config)
    result_label.config(text=result_text)    

def truck_drive():
    result_text = truck.drive()
    result_label.config(text = result_text)

# 버튼 담기 위한 프레임(나란히 배치.)
button_frame = Frame(root)
button_frame.pack(pady=10)    # 프레임 자체를 padding해줌.

button1 = Button(button_frame, text="자동차 주행", command=car_drive)
button1.pack(side=LEFT, padx=5)

button2 = Button(button_frame, text="트럭 주행", command=truck_drive)
button2.pack(side=LEFT, padx=5)
# 버튼끼리 띄어놓으려면 padding을 x 기준으로.

# 결과 라벨(버튼아래)
result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()