# 5. 실시간 키 입력(get_pressed)
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 5")

# 이동 테스트용 좌표
x, y = WIDTH // 2, HEIGHT // 2    # 처음 시작점을 중간으로 할 거기 때문에 얘의 중간을 미리 정해둠.
speed = 1
size = 40    # 네모 크기(연습용 네모를 그려서 얘 움직임을 볼거임)

running = True

while running:    
    # 4. 이벤트 처리(좌표로 다 보임)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     # 창 닫기 버튼
            running = False    # 이벤트가 quit(창 닫기)면 그만 돌아가.
        if event.type == pygame.KEYDOWN:  # 키 눌림
            print("KEYDOWN:", event.key)
        if event.type == pygame.KEYUP:    # 키에서 손 뗌.
            print("KEYUP:", event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:   # 마우스 클릭
            print("MOUSE Click:", event.pos)


    # 실시간 키 입력(get_Pressed)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # 중요. 화면 안으로만 이동하도록 제한(튕기거나 나가지지 X.)
    if x < 0:
        x = 0
    if x > WIDTH - size:
        x = WIDTH - size
    if y < 0:
        y = 0
    if y > HEIGHT - size:
        y = HEIGHT - size
    
    # 화면 그리기 로직
    screen.fill((200, 200, 200))    # 회색 창
    pygame.draw.rect(screen, (0, 0, 255), (x, y, size, size))
    pygame.display.flip()

pygame.quit()