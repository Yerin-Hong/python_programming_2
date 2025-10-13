class Student:
    def __init__(self, name):
        self.name = name
        self.score = []    # 성적은 리스트 형태로 저장.(빈 리스트 생성)

    # 메소드 정의
    def add_score(self, score):
        self.score.append(score)
        print(f"{self.name}의 성적 {score}점이 추가되었습니다.")

    def cal_avg(self):
        if not self.score:    # 점수가 없으면(=0이면)
            return 0   # 0을 출력
        return sum(self.score) / len(self.score)   # 평균 연산(값이 있는 경우)
    
# 학생 인스턴스 생성
stu = Student("Kim")

# 성적 추가
stu.add_score(90)
stu.add_score(85)
stu.add_score(78)

# 평균 성적 출력
avg = stu.cal_avg()
print(f"{stu.name}의 평균 성적은 {avg:.2f}")    # 소수점 둘째 자리까지 출력