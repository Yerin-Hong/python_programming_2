# 10. 충돌 판정(Collision)
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DSfinal_20241241_03")

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 추가: 게임 상태 변수
lives = 3
kill_count = 0
game_over = False

font = pygame.font.SysFont(None, 24)

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")    
        self.image = pygame.transform.scale(self.image, (40, 40))  
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self):  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)   # 플레이어의 cnterx값 때문에 가운데서 총알 발사.
        all_sprites.add(bullet)
        bullets.add(bullet)


        # 화면 경계 제한
        self.rect.clamp_ip(screen.get_rect())

# 총알 클래스
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

def reset_game():
    global lives, kill_count, game_over, all_sprites, bullets, player

    lives = 3                  # 목숨 초기화
    kill_count = 0             # 점수 초기화
    game_over = False          # 게임 오버 해제

    # 스프라이트 그룹 재생성
    all_sprites.empty()
    bullets.empty()

    # 플레이어 다시 생성
    player = Player()
    all_sprites.add(player)

# 게임 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DSfinal_20241241_03")

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 최초 1회 초기화
reset_game()    # 추가

# 게임 루프
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()     # 추가: Sprite 그룹 생성 및 Player 
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)       

running = True
game_over = False    # 추가: 게임 오버 상태 표시용 플래그

# 2. 사과(Apple)
apples = []

# 추가: 사과 생성 주기 관리용 카운터
apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30 

def spawn_apple():
    # 추가: 화면 네 가장자리(상하좌우)에 사과 하나 생성
    side = random.choice(["top", "bottom"])
    size = 40
    if side == "top":
        x = random.randint(0, WIDTH - size) # 화면 위쪽 바깥
        y = -size
        vx = random.randint(2, 4)  
        vy = random.randint(-2, 2)  # 아래로 이동
    else:   # "bottom"
        x = random.randint(0, WIDTH - 40)
        y = HEIGHT
        vx = random.randint(-2, 2)   
        vy = -random.randint(2, 4)  # 위로 이동

    rect = pygame.Rect(x, y, size, size)
    apples.append({"rect": rect, "vx": vx, "vy": vy})       # 추가: 라스트에 사과 추가
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            all_sprites.update()   
    
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

            if event.type == pygame.KEYDOWN:        # 키 눌렸는데,
                if event.key == pygame.K_SPACE:     # 그 키가 스페이스 바면: 
                    player.shoot()                  # 쏴.
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -5      # 절댓값은 속도를, 부호는 방향(-는 왼쪽, +는 오른쪽) 의미.
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0

        apple_spawn_timer += 1
        if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
            apple_spawn_timer = 0
            spawn_apple()

        new_apples = []
        for apple in apples:
            rect = apple["rect"]
            vx = apple["vx"]
            vy = apple["vy"]

            rect.x += vx
            rect.y += vy

            # 화면을 완전히 벗어난 사과는 버림
            if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
                continue

    # 충돌처리
    if not game_over:
         all_sprites.update()

        # 외계인과 레이저의 충돌 검사
        hits = pygame.sprite.groupcollide(image, bullets, True, True)   # 외계인이랑 총알을 둘 다 한 그룹 안에 묶어뒀으니까 한 번에 불러오기.(groupcollide 사용) 
        for hit in hits:
            image.explode()   
            all_sprites.add(image)
            kill_count += 1     # 추가

        # 외계인과 우주선의 충돌 검사
        if pygame.sprite.spritecollide(player, image, False):
            lives -= 1      # 추가
            if lives <= 0: 
                game_over = True    # 추가
    



    # ---------- 그림 그리기 영역 ------------
    screen.fill((170, 200, 255))    # 파란 하늘 느낌 배경
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))   # 땅  

    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)  # 장애물 선
    
    all_sprites.draw(screen)  

    ui_text = font.render(f"Score: {kill_count}                     Lives: {lives}", True, white)

    #추가: 게임오버 메시지 (플래그가 True일 때만)
    if game_over:
        over_text = font.render("GAME OVER(Press R to Restart", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2 #글씨 정중앙에 배치
        over_y = (HEIGHT - over_text.get_height()) // 2 
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()