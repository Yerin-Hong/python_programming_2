from tkinter import *

# 클래스 정의
class Food:
    def __init__(self, name, price):
        # 속성: 메뉴 이름(name), 단가(price)
        self.name = name
        self.price = price

    def total_price(self, qty):
        return self.price * qty   # 기본: 단가*수량

    def __str__(self):
        return f"메뉴 : {self.name}, 단가 : {self.price}원"

class DeliveryFood(Food):       # 상속
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)
        self.delivery_fee = delivery_fee

    def total_price(self, qty):
        return (self.price * qty) + self.delivery_fee

    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}원, 배달비: {self.delivery_fee}원"

class Order:
    def __init__(self):
        self.items = []

    def add(self, food, qty):
        self.items.append((food, qty))

    def clear(self):
        self.items = []

    def total(self):
        total_price = 0
        for food, qty in self.items:
            total_price += food.total_price(qty)
        return total_price

    def summary_lines(self):
        lines = []  # 영수증의 각 줄을 저장할 리스트(빈 리스트 생성)
        lines.append("--- 영수증 ---")
        
        # 장바구니를 순회하며 항목별 내역 추가
        for food, qty in self.items:
            item_total = food.total_price(qty)
            lines.append(f"{food.name} x {qty} = {item_total}원")
            
        lines.append("-------------")
        lines.append(f"총 합계: {self.total()}원")
        return lines

# 4. 창설정
def update_gui():
    cart_listbox.delete(0, END) # 전체 비우기                          
    total_price = 0
     
    for food, qty in main_order.items:
        cart_listbox.insert(END, f"{food.name} x {qty}")
        total_price += food.total_price(qty)
    
    # 2. 총 합계
    total_label.config(text=f"총 합계: {total_price}원")

def add_to_cart():
    try:
        selected_index = menu_listbox.curselection()[0]
    except IndexError:
        return      # 아무것도 선택 안하면 종료

    food_item = menu_items[selected_index]
    
    qty = int(qty_spinbox.get())
    
    main_order.add(food_item, qty)
    
    # 5. 장바구니와 합계 금액 GUI를 업데이트
    update_gui()
    
    # 6. 영수증 Text 위젯은 비워줌 (새 항목이 추가되었끼 때문에)
    receipt_text.config(state="normal") # 수정 가능 상태로 변경
    receipt_text.delete(1.0, END)      # (1.0 = 1번째 줄 0번째 칸)
    receipt_text.config(state="disabled") # 다시 읽기 전용으로

def clear_cart():
    main_order.clear()   # 장바구니 비우기
    
    update_gui()

    receipt_text.config(state="normal")
    receipt_text.delete(1.0, END)
    receipt_text.config(state="disabled")

def do_order():

    summary = main_order.summary_lines()
    
    receipt_text.config(state="normal")  # 수정 가능 상태로
    receipt_text.delete(1.0, END)      # 기존 내용 삭제
    # "\n" (줄바꿈)으로 리스트의 각 항목을 합쳐서 하나의 문자열로 삽입
    receipt_text.insert(END, "\n".join(summary))
    receipt_text.config(state="disabled") # 읽기 전용으로
    
    # 3. 합계 레이블을 다시 한번 업데이트 (이미 update_gui로 맞지만 확인차)
    total_label.config(text=f"총 합계: {main_order.total()}원")

# 1. 메뉴 목록 (Food, DeliveryFood 객체 리스트)
menu_items = [
    Food("김밥", 3000),
    Food("떡볶이", 4000),
    Food("라면", 3500),
    Food("우동", 4500),
    DeliveryFood("치킨", 18000, 3000),
    DeliveryFood("피자", 20000, 2500),
    DeliveryFood("족발", 25000, 3000),
    Food("콜라", 1500)
]

main_order = Order()

# tkinter 구현 시작 

root = Tk()
root.title("주문·배달 시스템")
root.geometry("600x400")

left_frame = Frame(root)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# 오른쪽 프레임 (장바구니, 영수증 영역)
right_frame = Frame(root)
right_frame.pack(side="left", fill="y", padx=10, pady=10)

# 7. 왼쪽 영역 위젯

# 1. 메뉴 라벨
Label(left_frame, text="[ 메뉴 ]", font=("Arial", 12)).pack(pady=5)

# 2. 메뉴 Listbox + 스크롤바
# Listbox와 Scrollbar를 담을 Frame
menu_frame = Frame(left_frame)
menu_frame.pack()

# 스크롤바 생성
menu_scrollbar = Scrollbar(menu_frame, orient="vertical")
menu_scrollbar.pack(side="right", fill="y")

# Listbox
menu_listbox = Listbox(menu_frame, width=40, height=15, 
                     yscrollcommand=menu_scrollbar.set)
menu_listbox.pack(side="left")

# 스크롤바랑 Listbox 연결
menu_scrollbar.config(command=menu_listbox.yview)

# 3. 메뉴 Listbox에 데이터 채우기
for item in menu_items:
    menu_listbox.insert(END, str(item))

# 4. 수량 선택 (Spinbox) 영역
qty_frame = Frame(left_frame)
qty_frame.pack(pady=10)

Label(qty_frame, text="수량:").pack(side="left", padx=5)
# Spinbox 생성 (1부터 50까지 선택 가능)
qty_spinbox = Spinbox(qty_frame, from_=1, to=50, width=5)
qty_spinbox.pack(side="left")

# 5. "장바구니 담기" 버튼
add_button = Button(left_frame, text="장바구니 담기", command=add_to_cart)
add_button.pack(pady=10, fill="x")

# 오른쪽 
Label(right_frame, text="[ 장바구니 ]", font=("Arial", 12)).pack(pady=5)

cart_frame = Frame(right_frame)
cart_frame.pack()

cart_scrollbar = Scrollbar(cart_frame, orient="vertical")
cart_scrollbar.pack(side="right", fill="y")

cart_listbox = Listbox(cart_frame, width=40, height=10,
                     yscrollcommand=cart_scrollbar.set)
cart_listbox.pack(side="left")
cart_scrollbar.config(command=cart_listbox.yview)

# 3. 버튼 (전체 비우기, 주문하기) 영역
button_frame = Frame(right_frame)
button_frame.pack(pady=10)

# "전체 비우기" 버튼
clear_button = Button(button_frame, text="전체 비우기", command=clear_cart)
clear_button.pack(side="left", padx=5)

# "주문하기" 버튼
order_button = Button(button_frame, text="주문하기", command=do_order)
order_button.pack(side="left", padx=5)

# 4. 합계 금액 Label
total_label = Label(right_frame, text="총 합계: 0원", font=("Arial", 14, "bold"))
total_label.pack(pady=10)

# 5. 영수증 Label 및 Text 위젯 (PDF의 text.py 참고)
Label(right_frame, text="[ 영수증 ]").pack()
receipt_text = Text(right_frame, width=40, height=7, state="disabled") # state="disabled"로 초기엔 수정 불가능
receipt_text.pack()

root.mainloop()