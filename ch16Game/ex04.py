# 태양 그리기(노란색)
import turtle

t = turtle.Pen()
t.speed(0)

def mystar(size, filled):
    if filled:
        t.begin_fill()

    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)

    if filled:
        t.end_fill()

# 별 색 칠하기
t.color(0.9, 0.75, 0)    # 금색
mystar(120, True)

# 테두리 그리기
t.color(0,0,0)    # 검정색
mystar(120, False)

turtle.done()