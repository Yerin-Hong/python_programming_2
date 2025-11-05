from tkinter import *

# Book 클래스 정의 부분
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False    # 대출상태의 기본값은 False(대출 여부)

    def borrow(self):   # 대출
        if self.borrowed != True:      # 대출 중이 아니면(==False도 동일)
            self.borrowed = True       # 대출 중으로 상태 변경 후, 
            return f"{self.title}이(가) 대출되었습니다."    # 문자열 반환
        else:       # 아니면(=이미 True. =대출 중이면) 
            return f"{self.title}은(는) 이미 대출 중입니다."     # 문자열 반환

    def return_book(self):    # 반납
        if self.borrowed == True:       # 대출 중이면(!=False도 동일)
            self.borrowed = False       # 대출 상태를 반납으로 상태 변경.
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은 대출되지 않은 상태입니다."   

# Tkinter GUI 구현 부분

root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("430x280")  # 윈도우 창 키움

books = {}    # 딕셔너리 형태로 book 목록 생성
borrowed_books = []  # 현재 대출 중 도서 리스트

label_start = Label(root, text="도서 대출 관리 시스템", font=("명조체", 16, "bold"))
label_start.grid(row=0, column=0, columnspan=2, pady=15)

# 제목
label_title = Label(root, text="제목:")
label_title.grid(row=1, column=0, padx=10, pady=5, sticky='E')
entry_title = Entry(root, width=30)
entry_title.grid(row=1, column=1, padx=10, pady=5)

# 저자
label_author = Label(root, text="저자:")
label_author.grid(row=2, column=0, padx=10, pady=10, sticky='E')
entry_author = Entry(root, width=30)
entry_author.grid(row=2,column=1, padx=10, pady=10)

result_label = Label(root, text="", font=("명조체", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=10)  # 뒤에서 받을건데, 사용자가 아무것도 안 쓰면, 빈 문자열 반환

# 대출 현황 라벨 추가
borrowed_label = Label(root, text="대출 현황: ", font=("명조체", 8), justify=LEFT, anchor='w')    # 젤 기본은 대출 중인 도서 없음임.
borrowed_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='W')

# 대출 현황 갱신
def update_borrowed_list():
    if borrowed_books:
        text = ", ".join([f"{b.title}({b.author})" for b in borrowed_books])
    else:
        text = "없음"
    borrowed_label.config(text=f"대출 현황: {text}")

# 버튼 이벤트
def borrow_book():
    title = entry_title.get()
    author = entry_author.get()

    # [검증]
    if title == "" or author == "":
        result_label.config(text="제목과 저자를 입력하세요.", fg="red")  # 제목이랑 저자가 비어있으면 출력
        return
    
    # 중복 방지
    for b in borrowed_books:
        if b.title == title and b.author == author:   # 제목이랑 저자 둘 다 동일하면
            result_label.config(text=f"『{title}』은(는) 이미 대출 중입니다.", fg="red")
            return

    # 책이 등록되지 않았으면 딕셔너리에 추가
    key = (title, author) 
    if key not in books:
        books[key] = Book(title, author)

    book = books[key]
    msg = book.borrow()

    # [처리]
    if book.borrowed and book not in borrowed_books:
        borrowed_books.append(book)

    result_label.config(text=msg, fg="blue")

    update_borrowed_list()

    # 입력창 초기화(값을 다 지움)
    entry_title.delete(0, END)
    entry_author.delete(0, END)

def return_book():
    title = entry_title.get()    
    author = entry_author.get()   
    
    if title == "" or author == "":
        result_label.config(text="제목과 저자를 입력해주세요.", fg="red")
        return
    
    # 제목이랑 저자가 일치하는 책 찾기
    found = None
    for b in borrowed_books:
        if b.title == title and b.author == author:
            found = b
            break
    
    if found:
        msg = found.return_book()
        borrowed_books.remove(found)
        result_label.config(text=msg, fg="green")
    else:
        result_label.config(text=f"{title}은(는) 대출 목록에 없습니다.", fg="red")

    # 대출 현황 갱신
    update_borrowed_list()

    # 입력창 초기화(값을 다 지움)
    entry_title.delete(0, END)
    entry_author.delete(0, END)
    
# 버튼을 담을 프레임
button_frame = Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

button_borrow = Button(button_frame, text="대출", command=borrow_book, width=8)
button_borrow.grid(row=3, column=0, padx=20, pady=10)

button_return = Button(button_frame, text="반납", command=return_book, width=8)
button_return.grid(row=3, column=1, padx=20, pady=10)

root.mainloop()
