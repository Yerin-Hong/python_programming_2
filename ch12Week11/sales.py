import os
base_dir = os.path.dirname(__file__)

# 입력 차일과 출력 차일 이름을 받음.(input)
infilename = os.path.join(base_dir, input("입력 파일 이름: "))
outfilename = os.path.join(base_dir, input("출력 파일 이름: "))

# 합계와 횟수를 위한 변수 정의(누적합을 구할 거니까, 초기화 해주기)
sum = 0
count = 0

# 입력과 출력을 위한 파일을 열고 작업 수행
with open(infilename, "r", encoding="utf-8") as infile, \
    open(outfilename, "w", encoding="utf-8") as outfile:

    # 입력 파일에서 한 줄을 읽어서 합계 계산
    for line in infile:
        dailySale = int(line)
        sum += dailySale
        count += 1

    # 총매출과 일평균 매출을 출력 파일에 기록
    outfile.write("총매출 = " + str(sum) + "\n")
    outfile.write("평균 일매출 = " + str(sum // count))