infile = open(r"C:\Python\PythonProgramming2\practicemans\read2.txt", "r", encoding="utf-8")

line = infile.readline()

while line != "":
    print(line)
    line = infile.readline()
infile.close()