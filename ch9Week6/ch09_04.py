class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, amount):
        self.salary += amount
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")


# 직원 인스턴스 생성
kim = Employee("Kim", 5000)    # Employee니까 (이름, 연봉)
lee = Employee("Lee", 6000)

print(f"{kim.name}의 연봉은 {kim.salary}입니다.")
print(f"{lee.name}의 연봉은 {lee.salary}입니다.")

kim.raise_salary(2000)     # amount
lee.raise_salary(2000)