"""
문제 1. 파일, 예외처리
-텍스트 파일을 열고 내용을 읽어서 화면에 출력하는 프로그램.
-파일을 열 때 발생할 수 있는 예외(FileNotFoundError)응 처리하는 프로그램 추가.
"""
def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

filename = input("파일 이름을 입력하세요:")
read_file(filename)