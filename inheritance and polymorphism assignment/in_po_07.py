# -------------------------------------------------------------------
# 0. 모듈 가져오기
# -------------------------------------------------------------------
# tkinter 라이브러리의 모든 기능을 가져옵니다. (PDF 스타일)
from tkinter import *

# -------------------------------------------------------------------
# 1. 부모 클래스 Food 정의
# -------------------------------------------------------------------
class Food:
    """
    모든 메뉴의 기본이 되는 부모 클래스입니다.
    """
    def __init__(self, name, price):
        # 속성: 메뉴 이름(name), 단가(price)
        self.name = name
        self.price = price

    def total_price(self, qty):
        """
        수량(qty)만큼의 총 가격을 반환합니다.
        (기본: 단가 * 수량)
        """
        return self.price * qty

    def __str__(self):
        """
        객체를 문자열로 표현할 때 사용됩니다. (메뉴 Listbox 표시에 사용)
        형식: "메뉴 : 김밥, 단가 : 3000원"
        """
        return f"메뉴 : {self.name}, 단가 : {self.price}원"

# -------------------------------------------------------------------
# 2. 자식 클래스 DeliveryFood 정의
# -------------------------------------------------------------------
class DeliveryFood(Food):
    """
    Food 클래스를 상속받는 배달 음식 클래스입니다.
    """
    def __init__(self, name, price, delivery_fee):
        # 부모 클래스(Food)의 __init__을 호출하여 name, price를 설정
        super().__init__(name, price)
        # 속성: 배달비(delivery_fee) 추가
        self.delivery_fee = delivery_fee

    def total_price(self, qty):
        """
        total_price 메서드를 오버라이딩(재정의)합니다.
        (단가 × 수량) + 배달비를 반환합니다.
        """
        return (self.price * qty) + self.delivery_fee

    def __str__(self):
        """
        __str__ 메서드를 오버라이딩(재정의)합니다.
        형식: "메뉴: 치킨, 단가: 18000원, 배달비: 3000원"
        """
        return f"메뉴: {self.name}, 단가: {self.price}원, 배달비: {self.delivery_fee}원"

# -------------------------------------------------------------------
# 3. 주문 클래스 Order 정의
# -------------------------------------------------------------------
class Order:
    """
    주문 내역(장바구니)을 관리하는 클래스입니다.
    """
    def __init__(self):
        # items: (Food 객체, 수량) 형태의 튜플(tuple)을 리스트로 저장
        self.items = []

    def add(self, food, qty):
        """
        메뉴(food 객체)와 수량(qty)을 장바구니 리스트(items)에 추가합니다.
        """
        self.items.append((food, qty))

    def clear(self):
        """
        장바구니(items 리스트)를 초기화합니다.
        """
        self.items = []

    def total(self):
        """
        장바구니 내 모든 항목의 합계 금액을 계산합니다.
        """
        total_price = 0
        # self.items 리스트에서 (Food 객체, 수량) 튜플을 하나씩 꺼냅니다.
        for food, qty in self.items:
            # ★ 다형성(Polymorphism) ★
            # food 객체가 Food 타입이면 Food의 total_price()가,
            # DeliveryFood 타입이면 DeliveryFood의 total_price()가
            # 자동으로 호출되어 배달비가 올바르게 계산됩니다.
            total_price += food.total_price(qty)
        return total_price

    def summary_lines(self):
        """
        영수증 형태로 출력될 문자열의 "리스트"를 반환합니다.
        """
        lines = []  # 영수증의 각 줄을 저장할 리스트
        lines.append("--- 영수증 ---")
        
        # 장바구니를 순회하며 항목별 내역 추가
        for food, qty in self.items:
            item_total = food.total_price(qty)
            # 예: "치킨 x 1 = 21000원"
            lines.append(f"{food.name} x {qty} = {item_total}원")
            
        lines.append("-------------")
        # Order.total() 메서드를 호출하여 최종 합계 추가
        lines.append(f"총 합계: {self.total()}원")
        return lines

# -------------------------------------------------------------------
# 4. GUI 애플리케이션 함수 (콜백) 정의
# (위젯보다 먼저 정의되어야 위젯의 command에서 사용 가능)
# -------------------------------------------------------------------

def update_gui():
    """
    [헬퍼 함수] 
    장바구니(오른쪽 Listbox)와 총 합계(Label)를 업데이트합니다.
    """
    # 1. 장바구니 Listbox 업데이트
    cart_listbox.delete(0, END) # 기존 내용을 모두 삭제
    total_price = 0
    
    # main_order(Order 객체)의 items 리스트를 순회
    for food, qty in main_order.items:
        # 장바구니 목록에는 "메뉴이름 x 수량" 형식으로 표시
        cart_listbox.insert(END, f"{food.name} x {qty}")
        # 합계 계산 (다형성)
        total_price += food.total_price(qty)
    
    # 2. 총 합계 Label 업데이트
    total_label.config(text=f"총 합계: {total_price}원")

def add_to_cart():
    """
    [콜백 함수 1] "장바구니 담기" 버튼 클릭 시 실행
    """
    # 1. 왼쪽 메뉴 Listbox에서 현재 선택된 항목의 인덱스(번호)를 가져옴
    try:
        # curselection()은 (인덱스,) 형태의 튜플을 반환
        selected_index = menu_listbox.curselection()[0]
    except IndexError:
        # 아무것도 선택하지 않았으면 함수 종료
        return 

    # 2. menu_items 리스트에서 해당 인덱스의 Food 객체를 가져옴
    food_item = menu_items[selected_index]
    
    # 3. Spinbox에서 수량(qty) 값을 가져옴 (문자열이므로 정수로 변환)
    qty = int(qty_spinbox.get())
    
    # 4. Order 객체에 선택한 메뉴와 수량을 추가
    main_order.add(food_item, qty)
    
    # 5. 장바구니와 합계 금액 GUI를 업데이트
    update_gui()
    
    # 6. 영수증 Text 위젯은 비워줌 (새 항목이 추가되었으므로)
    receipt_text.config(state="normal") # 수정 가능 상태로 변경
    receipt_text.delete(1.0, END)      # (1.0 = 1번째 줄 0번째 칸)
    receipt_text.config(state="disabled") # 다시 읽기 전용으로

def clear_cart():
    """
    [콜백 함수 2] "전체 비우기" 버튼 클릭 시 실행
    """
    # 1. Order 객체의 장바구니를 비움
    main_order.clear()
    
    # 2. 장바구니와 합계 금액 GUI를 업데이트 (빈 목록, 0원으로)
    update_gui()
    
    # 3. 영수증 Text 위젯도 비움
    receipt_text.config(state="normal")
    receipt_text.delete(1.0, END)
    receipt_text.config(state="disabled")

def do_order():
    """
    [콜백 함수 3] "주문하기" 버튼 클릭 시 실행
    """
    # 1. Order 객체에서 영수증 문자열 리스트를 가져옴
    summary = main_order.summary_lines()
    
    # 2. 영수증 Text 위젯에 표시
    receipt_text.config(state="normal")  # 수정 가능 상태로
    receipt_text.delete(1.0, END)      # 기존 내용 삭제
    # "\n" (줄바꿈)으로 리스트의 각 항목을 합쳐서 하나의 문자열로 삽입
    receipt_text.insert(END, "\n".join(summary))
    receipt_text.config(state="disabled") # 읽기 전용으로
    
    # 3. 합계 레이블을 다시 한번 업데이트 (이미 update_gui로 맞지만 확인차)
    total_label.config(text=f"총 합계: {main_order.total()}원")


# -------------------------------------------------------------------
# 5. 전역 데이터 및 객체 생성
# -------------------------------------------------------------------

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

# 2. 메인 주문 객체 (이 객체에 모든 주문 내역이 저장됨)
main_order = Order()

# -------------------------------------------------------------------
# 6. GUI 창 설정 및 레이아웃
# -------------------------------------------------------------------

# 1. 기본 윈도우(root) 생성
root = Tk()
root.title("주문·배달 시스템")
root.geometry("680x440")    # 창 크기 680x440
root.resizable(False, False) # 창 크기 조절 비활성화

# 2. 레이아웃을 위한 메인 프레임 (좌 / 우)
# (PDF의 pack.py 예제처럼 side="left"를 사용)
# 왼쪽 프레임 (메뉴 영역)
left_frame = Frame(root)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# 오른쪽 프레임 (장바구니, 영수증 영역)
right_frame = Frame(root)
right_frame.pack(side="left", fill="y", padx=10, pady=10)


# -------------------------------------------------------------------
# 7. 왼쪽 영역 위젯
# -------------------------------------------------------------------

# 1. 메뉴 라벨
Label(left_frame, text="[ 메뉴 ]", font=("Arial", 12)).pack(pady=5)

# 2. 메뉴 Listbox + 스크롤바 (PDF의 listbox.py 참고)
# Listbox와 Scrollbar를 담을 Frame
menu_frame = Frame(left_frame)
menu_frame.pack()

# 스크롤바 생성
menu_scrollbar = Scrollbar(menu_frame, orient="vertical")
menu_scrollbar.pack(side="right", fill="y")

# Listbox 생성 (너비 40, 높이 15)
menu_listbox = Listbox(menu_frame, width=40, height=15, 
                     yscrollcommand=menu_scrollbar.set)
menu_listbox.pack(side="left")

# 스크롤바와 Listbox를 서로 연결
menu_scrollbar.config(command=menu_listbox.yview)

# 3. 메뉴 Listbox에 데이터 채우기
for item in menu_items:
    # item 객체의 __str__() 메서드가 자동으로 호출되어 문자열이 삽입됨
    menu_listbox.insert(END, str(item))

# 4. 수량 선택 (Spinbox) 영역
qty_frame = Frame(left_frame)
qty_frame.pack(pady=10)

Label(qty_frame, text="수량:").pack(side="left", padx=5)
# Spinbox 생성 (1부터 50까지 선택 가능)
qty_spinbox = Spinbox(qty_frame, from_=1, to=50, width=5)
qty_spinbox.pack(side="left")

# 5. "장바구니 담기" 버튼
# 버튼 클릭 시 add_to_cart 함수가 호출되도록 command 설정
add_button = Button(left_frame, text="장바구니 담기", command=add_to_cart)
add_button.pack(pady=10, fill="x") # fill="x"로 가로 꽉 채우기

# -------------------------------------------------------------------
# 8. 오른쪽 영역 위젯
# -------------------------------------------------------------------

# 1. 장바구니 라벨
Label(right_frame, text="[ 장바구니 ]", font=("Arial", 12)).pack(pady=5)

# 2. 장바구니 Listbox + 스크롤바
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

# -------------------------------------------------------------------
# 9. 메인 루프 시작
# -------------------------------------------------------------------
root.mainloop() # 윈도우 창을 실행하고 사용자 입력을 기다립니다.