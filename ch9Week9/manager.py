# 직원과 매니저
# 메소드 오버라이드 실습.
"""
회사에 직원(Employee)과 매니저(Manager)가 있음. 직원은 월급만 있지만, 매니저는 월급외에 보너스가 있음.
Employee 클래스를 상속받아서 Manager 클래스를 작성함.
"""

class Employee:
    def __init__(self, name ,salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def getSalary(self):    
        salary = super().getSalary()
        return salary + self.bonus
    
    def __repr__(self):
        return "이름:" + self.name + ";월급:" + str(self.salary) + ";보너스:" + str(self.bonus)
    
# 출력
Kim = Manager("김철수", 20000000, 10000000)
print(Kim)