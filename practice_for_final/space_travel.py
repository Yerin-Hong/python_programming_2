import tkinter as tk
import random

# 전역 변수 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
SPACECRAFT_MOVE_SPEED = 10 # 우주선 이동 속도 (픽셀 단위)
spacecraft_id = None
canvas = None

# 별 생성 함수 (기존 유지)
def create_star(canvas, x, y, radius):
    return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = "white", outline = "")

# 우주선 생성 함수 (기존 유지)
def create_spacecraft(canvas, x, y, image):
    return canvas.create_image(x, y, image = image)

# 우주선 이동 함수 (기존 유지)
def move_spacecraft(canvas, obj_id, dx, dy):
    canvas.move(obj_id, dx, dy)

# --- 새로운 기능 ---

# 키 이벤트 처리 함수
def on_key_press(event):
    """
    키가 눌렸을 때 우주선을 이동시키는 함수
    """
    global spacecraft_id, canvas
    
    # 우주선 객체가 생성되지 않았거나 캔버스가 없으면 작동하지 않음
    if spacecraft_id is None or canvas is None:
        return

    dx, dy = 0, 0
    
    # 눌린 키에 따라 이동할 방향 결정
    if event.keysym == 'Left':
        dx = -SPACECRAFT_MOVE_SPEED
    elif event.keysym == 'Right':
        dx = SPACECRAFT_MOVE_SPEED
    elif event.keysym == 'Up':
        dy = -SPACECRAFT_MOVE_SPEED
    elif event.keysym == 'Down':
        dy = SPACECRAFT_MOVE_SPEED

    # 우주선 이동 실행
    if dx != 0 or dy != 0:
        move_spacecraft(canvas, spacecraft_id, dx, dy)
        
        # 캔버스 경계를 벗어나지 않도록 위치 보정 (옵션)
        coords = canvas.coords(spacecraft_id)
        current_x, current_y = coords[0], coords[1]
        
        # 캔버스 경계 확인 로직 (간단한 예시)
        # 이미지 크기에 따라 더 정교한 계산이 필요할 수 있습니다.
        if current_x < 0:
            canvas.coords(spacecraft_id, 0, current_y)
        elif current_x > WINDOW_WIDTH:
            canvas.coords(spacecraft_id, WINDOW_WIDTH, current_y)
        if current_y < 0:
            canvas.coords(spacecraft_id, current_x, 0)
        elif current_y > WINDOW_HEIGHT:
            canvas.coords(spacecraft_id, current_x, WINDOW_HEIGHT)


# 메인 실행 함수
def main():
    global spacecraft_id, canvas, photo_image
    
    # 윈도우(Root) 생성
    root = tk.Tk()
    root.title("Spacecraft Movement")

    # 캔버스 생성
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
    canvas.pack()

    # (주의) 우주선 이미지는 PhotoImage 객체로 로드해야 하며, 
    # 이 객체는 Tkinter 메인 윈도우가 닫힐 때까지 유지되어야 합니다 (전역 변수 처리).
    try:
        # 간단한 직사각형을 우주선으로 대체 (실제 이미지 파일 경로를 사용하세요)
        # 실제 이미지 파일을 사용할 경우: photo_image = tk.PhotoImage(file="spacecraft.png")
        photo_image = tk.PhotoImage(width=30, height=30)
        photo_image.put("white", to=(10, 10, 20, 20)) # 흰색 점을 찍어 모양 대체
        
        # 우주선 중앙 위치
        start_x = WINDOW_WIDTH // 2
        start_y = WINDOW_HEIGHT - 50 
        
        # 우주선 생성
        spacecraft_id = create_spacecraft(canvas, start_x, start_y, photo_image)
    except tk.TclError as e:
        print(f"이미지 로딩 오류: {e}. 이미지 파일 경로를 확인하거나 대체 코드를 사용하세요.")
        return
    
    # 배경 별 생성 (예시)
    for _ in range(50):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        radius = random.uniform(1, 3)
        create_star(canvas, x, y, radius)
    
    # 키 이벤트 바인딩
    # 1. 캔버스에 포커스를 설정하여 키 입력을 받을 수 있게 합니다.
    canvas.focus_set() 
    # 2. 화살표 키를 눌렀을 때 on_key_press 함수를 호출하도록 바인딩합니다.
    canvas.bind('<Key>', on_key_press)
    
    # 메인 루프 실행
    root.mainloop()

if __name__ == "__main__":
    main()