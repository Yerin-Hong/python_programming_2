# 도서 대출 관리 프로그램
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False    # 대출상태의 기본값은 False

    def borrow(self):   # 대출
        if self.borrowed != True:      # 대출 중이 아니면
            self.borrowed = True       # 대출 중으로 상태 변경 후, 
            print(f"{self.title}이(가) 대출되었습니다.")    # 문자열 출력
        else:       # 아니면(=이미 True. =대출 중이면) 
            print(f"{self.title}은(는) 이미 대출 중입니다.")     # 문자열 출력

    def return_book(self):    # 반납
        print(f"{self.title}이(가) 반납되었습니다.")
        self.borrowed = False       # 대출 상태를 반납으로 상태 변경.

b1 = Book("파이썬 프로그래밍", "홍길동")
b1.borrow()     # 대출
b1.borrow()     # 한 번 더 대출
b1.return_book()    # 반납