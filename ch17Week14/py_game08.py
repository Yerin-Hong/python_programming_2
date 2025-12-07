# 8. 프레임 속도(FPS) 제어
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 8")

clock = pygame.time.Clock() # FPS 제어 준비
"""
FPS(초당 프레임 수)는 게임 내 프레임 설정. 프레임은 화면에 나타나는 그림 한 장(정지화면)을 의미.
프레임을 빠르게 움직이면 그게 영상처럼 보이는 원리.
화면이 1초에 몇 번씩 바뀔건지를 의미함. 그래서 초당 프레임 수.
그렇다고 크다고 다 좋은 건 아님. 컴터가 못 따라가주면 렉걸림.
"""

# 사용자 이미지 로드
img = pygame.image.load("cat.png")    # 여기에 파일 이름 입력(png, jpg 등)
img = pygame.transform.scale(img, (70, 70))   # 크기 조절
rect = img.get_rect()
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 3
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # 화면 경계 제한(네 줄로 정의한 걸, 스크린 크기까지만 이동하는 내장기능 사용.)
    rect.clamp_ip(screen.get_rect())   # 추가: Rect의 내장기능 사용(더 깔끔!)
    
    # 추가: 화면 그리기(Drawning) 영역
    screen.fill((170, 200, 255))    # 추가: 파란 하늘 느낌 배경

    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))#추가: 바닥(땅) 그리기
    pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40))#추가: 빨간 박스(아이템처럼 보이게)
    pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20) #추가: 초록 원(코인 느낌)
    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)#추가: 검은 선(장애물 느낌)
  
    screen.blit(img, rect) #추가: 캐릭터 그리기

    pygame.display.flip()

    clock.tick(60)    # 추가: 60 FPS(초당 60회를 그려줌.)
pygame.quit()