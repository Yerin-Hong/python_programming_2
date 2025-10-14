# 사용자가 데이터를 입력하면 동적으로 그래프가 그려지는 코드(plot 사용)
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 시헝볼 때 만들어야 되는 부분
def plot_graph():
    # 입력창에서 받은 값을 x_data와 y_data 리스트에 추가하고, 그리면 됨
    # x, y값은 엔트리 위젯에서 가져옴(문자열 상태로) --> 실수로 변경
    x = float(x_entry.get())
    y = float(x_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker = 'o', linestyle = '-')    # 각 리스트에서 값을 가져옴.
    # 그림 그리는 부분(호출해서 tk 안의 값이 저장됨)
    canvas.draw()

# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Dynamic Line Graph")

x_data = []
y_data = []    # 좌표 데이터 저장할 리스트

x_label = tk.Label(root, text = "Enter x coordinate:")   # 좌표 입력
x_label.pack()   # 고정
x_entry = tk.Entry(root)    # 입력
x_entry.pack()    # 고정

y_label = tk.Label(root, text = "Enter y coordinate:")   # 좌표 입력
y_label.pack()
y_entry = tk.Entry(root )     
y_entry.pack()

plot_button = tk.Button(root, text = "Plot", command = plot_graph)    # 버튼 생성
plot_button.pack()

# Matplotlib Figure 생성
fig = Figure(figsize = (5, 4), dpi = 100)   # 해상도 지원
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master = root)
canvas.get_tk_widget().pack()

# 애플리케이션 실행
root.mainloop()
