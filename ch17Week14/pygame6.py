"""

"""

import pygame
import sys
import random

pygame.init()

# 게임 화면 크기
screen_width = 800
screen_height = 600

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# (추가) 폭발 사운드 준비
explosion_sound = pygame.mixer.Sound("explosion.wav")

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

    # Player가 총을 쏘는 기능 추가.
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)   # 플레이어의 cnterx값 때문에 가운데서 총알 발사.
        all_sprites.add(bullet)
        bullets.add(bullet)

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

    def explode(self):
        explosion_sound.play()    # (추가) 폭발 사운드 재생
        # self.kill()

# 레이저(총알) 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y   # Bullet 객체의 현재 Y축 위치(수직). 총알은 앞으로만 나감. y축만 변경. self.speed_y는 Bullet 클래스의 생성자에서 -2로 됨. 위로 2칸씩 이동.
        if self.rect.bottom < 0:
            self.kill()

# 게임 화면 생성
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")

# 스프라이트 그룹 생성(그룹은 각 객체(sprite)들의 집합)
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 플레이어 생성
player = Player()
all_sprites.add(player)

# 외계인 생성
for _ in range(10):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

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

    # 외계인과 레이저의 충돌 검사
    hits = pygame.sprite.groupcollide(aliens, bullets, True, True)   # 외계인이랑 총알을 둘 다 한 그룹 안에 묶어뒀으니까 한 번에 불러오기.(groupcollide 사용) 
    for hit in hits:
        alien = Alien()
        alien.explode()    # 충돌 함수 추가
        all_sprites.add(alien)
        aliens.add(alien)

    # 외계인과 우주선의 충돌 검사
    if pygame.sprite.spritecollide(player, aliens, False):
        print("우리 우주선 피격!")
        # pygame.quit()
        # sys.exit()

    # 배경 화면 채우기
    screen.fill(black)

    # 스프라이트 그룹을 화면에 그리기
    all_sprites.draw(screen)

    # 화면 업데이트
    pygame.display.flip()
    # FPS 설정(60)
    clock.tick(60)