"""
문제 2. 파일, 문자열
-텍스트 파일에서 특정 문자열을 검색하고, 
해당 문자열이 파일 안에서 몇 번 나타나는지 카운팅하는 프로그램
"""

def countStr(filename, search):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.open()
            count = content.count(search)
            return count
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return 0
    
filename = input("파일 이름을 입력하세요:")
search = input("찾을 문자열 이름을 입력하세요:")

find = countStr(filename, search)
print(f"'{search}'(은)는 파일 내에서 {find}번 나타납니다.")