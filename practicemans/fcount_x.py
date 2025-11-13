# 사용자로부터 파일명을 입력받아 파일명을 filename 변수에 저장
filename = input("파일명을 입력하세요").strip()

# 입력받은 파일명으로 파일을 읽기 모드로 열어 infile에 저장.
infile = open(filename, "r")

# 문자의 빈도수를 저장할 빈 사전 freqs를 생성
freqs = {}

# 파일의 각 줄에 대하여 문자를 추출
# 각 문자를 사전 freqs에 추가, 의미 있는 문자면 빈도수를 증가시킴
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

# 문자의 빈도수를 출력
print(freqs)
infile.close()
