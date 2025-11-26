from tkinter import *

# 함수 설정
def draw_shape():
    canvas.delete("all")    # 이전 그림 지우기
    choice = shape_var.get()

    if choice == 1:     # 사각형
        canvas.create_rectangle(50, 50, 150, 150, fill = "red")
    elif choice == 2:       # 원
        canvas.create_oval(200, 80, 300, 150, fill = "blue")
    elif choice == 3:       # 텍스트
        canvas.create_text(200, 150, text="hello, Duksung", fill = "blue", font = ("Helvetica", 20, "bold"))
 
# 1-2. 메인 윈도우 생성
root = Tk()
root.title = "중간고사 4번"
root.geometry("400x400")

# 3. 캔버스
canvas = Canvas(root, width = 400, height = 300, bg = "white")
canvas.pack()

# 4. 라디오 버튼 선택값 저장할 변수(사각형, 원, 텍스트 중 택 1이니까, 함수로 생성)
shape_var = IntVar()
shape_var.set(1)    # 기본값: 사각형

# 라디오버튼 생성
frame = Frame(root)
frame.pack(pady = 10)

Radiobutton(frame, text = "사각형", variable=shape_var, value = 1).pack(side="left", padx=10)
Radiobutton(frame, text = "원", variable=shape_var, value = 2).pack(side="left", padx=10)
Radiobutton(frame, text = "텍스트", variable=shape_var, value = 3).pack(side="left", padx=10)

# 버튼 생성
Button(root, text = "그리기", command = draw_shape, bg="lightgray").pack(pady=5)

root.mainloop()