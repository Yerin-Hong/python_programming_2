infile = open(r"C:\Python\PythonProgramming2\practicemans\read2.txt", "r", encoding="utf-8")

for line in infile:
    line = line.rstrip()    # 오른쪽 공백 제거
    print(line)
infile.close()