# Object 클래스의 __repr__() 메소드는 객체가 가진 정보를 한 줄의 문자열로 만들어서 반환.
class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn

    def __repr__(self):
        return "ISBN:" + self.__isbn +"\n" + "TITLE:" + self.__title
    
book = Book("The Python Tutorial", "0123456")
print(book)