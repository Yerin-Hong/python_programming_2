# DS_20241241_01.py
class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def show_info(self):
        print(f"학번: {self.stu_id}, 이름: {self.name}")

stu = DSstudent(20241241, "홍예린")
print(stu.show_info())