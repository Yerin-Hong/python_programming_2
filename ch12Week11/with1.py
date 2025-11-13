# 텍스트 파일을 읽어서 각 라인을 출력
with open(r"C:\Python\PythonProgramming2\practicemans\proverbs.txt", "r") as file:
    for line in file:
        print(line.strip())      # 각 라인의 끝에 있는 개행 문자 제거 후 출력

# with 블록을 빠져나오면 자동으로 닫힘