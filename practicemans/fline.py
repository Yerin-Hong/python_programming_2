# "proverbs.txt" 파일을 읽기 모드로 열고 "infile" 변수에 할당
infile = open("proverbs.txt")

# "output.txt" 파일을 쓰기 모드로 열고 "outfile" 변수에 할당
outfile = open("outfile.txt", "w")

# 라인 번호를 저장할 변수 초기화
i = 1

# "proverbs.txt" 파일의 각 라인에 대해 반복
for line in infile:
    # 각 라인 앞에 라인 번호를 추가하고 ':'과 공백을 포함해 "output.txt" 파일에 쓰기
    outfile.write(str(i) + ":" + line)
    
    # 다음 라인으로 이동하기 위해 라인 번호 증가'
    i += 1

# 파일 닫기
infile.close()
outfile.close()