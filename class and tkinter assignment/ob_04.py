# 과목 성적 관리 클래스
class Course:
    def __init__(self, name):
        self.name = name
        self.scores = []     # 빈 리스트(성적)

    def add_score(self, s):
        self.scores.append(s)   # 리스트에 점수(성적) 추가

    def avg(self):  # 평균점수 반환
        return sum(self.scores) / len(self.scores)   # sum(점수 리스트 값) / len(리스트)
    
    def info(self):
        return f"과목: {self.name}, 평균: {self.avg()}"     # info()로 문자열 반환(return)

c = Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info())