# 문제 3. Shape 계층(사각형 + 원) 오버라이딩 + Canvas에 그리기

from tkinter import *
import math

class Shape:
    def __init__(self, x, y): self.x, self.y = x, y
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError
    def draw(self, canvas): raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w 
        self.h = h
    
    def area(self): 
        return self.w * self.h
    
    def perimeter(self): 
        return 2 * (self.w + self.h)
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="orangered")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
    
    def area(self): 
        return math.pi * self.r ** 2
    
    def perimeter(self): 
        return 2 * math.pi * self.r
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="skyblue")

# Tkinter 구현
root = Tk()
root.title("문제3")
canvas = Canvas(root, width=300, height=220, bg="white")
canvas.pack(pady=5)

var = StringVar(value="rect")
info = StringVar(value="도형을 선택하고 그리기를 누르세요.")
Label(root, textvariable=info).pack()

frame = Frame(root)
frame.pack(pady=5, anchor="center")

Radiobutton(frame, text="사각형", value="rect", variable=var).pack(side="left", padx=6)
Radiobutton(frame, text="원", value="circle", variable=var).pack(side="left", padx=6)

def draw_shape():
    canvas.delete("all")
    if var.get() == "rect":
        s = Rectangle(50, 50, 100, 60)
    else:
        s = Circle(150, 110, 40)
    s.draw(canvas)
    info.set(f"면적={s.area():.2f}, 둘레={s.perimeter():.2f}")

Button(root, text="그리기", command=draw_shape).pack(pady=6)


root.mainloop()