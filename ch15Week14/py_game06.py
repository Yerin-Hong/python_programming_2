# 6. Surface와 Rect(이미지적용버전)
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 6 - 네모 상자 이미지로 변경")

# 사용자 이미지 로드
img = pygame.image.load("cat.png")    # 여기에 파일 이름 입력(png, jpg 등)
img = pygame.transform.scale(img, (70, 70))   # 크기 조절
rect = img.get_rect()
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 1
running = True

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     # 창 닫기 버튼
            running = False    # 이벤트가 quit(창 닫기)면 그만 돌아가.

    # 실시간 키 입력(get_Pressed)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed

    # 화면 경계 제한
    if rect.left < 0:
        rect.left = 0
    if rect.right > WIDTH:
        rect.right = WIDTH
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT
  
    # 화면 그리기 로직
    screen.fill((200, 200, 200))  
    screen.blit(img, rect)    # 네모 대신 이미지로 그리기.
    pygame.display.flip()

pygame.quit()