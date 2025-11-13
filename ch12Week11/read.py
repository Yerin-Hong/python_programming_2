import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "C:\\Python\\PythonProgramming2\\practicemans\\1234.txt")        # 백슬래쉬(\)를 두 번 써서 해주기
print(base_dir)
print(file_path)
infile = open(file_path, "r", encoding="utf-8")
s = infile.read()
print(s)
infile.close()