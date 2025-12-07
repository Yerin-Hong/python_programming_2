"""
외계인이 랜덤으로 겁나 많이 쏟아지고, 우주선은 x축으로 양쪽 끝까지 이동만 가능한 상태.
총알을 쏘거나 하는 기능은 아직.
"""

import pygame
import sys
import random

# 게임 화면 크기
screen_width = 800
screen_height = 600

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(green)
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

# 외계인 클래스
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((30 30))  
        # self.image.fill(red)

        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:   # 객체 머리(top)부분이 스크린 height보다 높으면,
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)

# 스프라이트 그룹 생성(그룹은 각 객체(sprite)들의 집합)
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()

# 플레이어 생성
player = Player()
all_sprites.add(player)

# 외계인 생성
for _ in range(10):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

# 게임 화면 생성
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
# 윗줄은 윈도우를 생성하고 초기화하는 함수인데, pygamedml display 모듈의 함수.
pygame.display.set_caption("Space Invader")
# 게임 루프
clock = pygame.time.Clock()

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5      # 절댓값은 속도를, 부호는 방향(-는 왼쪽, +는 오른쪽) 의미.
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # 화면 업데이트(이것도 루프 안에서 반복할 거니까 while문 안에 넣어주기)
    all_sprites.update()
    screen.fill(black)
    # 스프라이트 그룹을 화면에 그리기
    all_sprites.draw(screen)
    # 화면 업데이트
    pygame.display.flip()
    # FPS 설정(60)
    clock.tick(60)

pygame.quit()