class Employee:
    empCount = 0   # 클래스 변수

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount += 1     # 이 변수는 Employee 클래스에서 사용되는 변수라는 것을 명시해야함.

    def displayEmp(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Employee 객체 생성
emp1 = Employee("Kim", 5000)
emp2 = Employee("Lee", 6000)

# 직원 정보 출력
emp1.displayEmp()
emp2.displayEmp()

# 전체 직원 수 출력
print("Total employees: ", Employee.empCount)