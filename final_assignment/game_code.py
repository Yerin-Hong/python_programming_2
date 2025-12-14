import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 생성
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("물고기 키우기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (150, 230, 255) # 배경 물 색상
gray = (100, 100, 100) # 임시 물고기 색상

# 게임 상태 변수
lives = 3 # 목숨
score = 0 # 물고기 먹은 횟수
game_over = False # 실패 상태
game_win = False  # 승리 상태

# 폰트 설정
# 폰트가 없을 경우 기본 폰트를 쓰기
try:
    font_kor = pygame.font.SysFont('Malgun Gothic', 50)
except:
    font_kor = pygame.font.SysFont(None, 50) # 대체 폰트
font_eng = pygame.font.SysFont(None, 35) # 영어 폰트

# 클래스 정의
class Player(pygame.sprite.Sprite):
    # 단계별로 main_fish보다 작은 sub_fish 먹고 사이즈 갱신
    STAGES = {
        0: (40, 40), # 초기 크기
        10: (60, 60), # Score 10 달성 시
        15: (100, 100), # Score 15 달성 시
        25: (110, 110), # Score 25 달성 시 (수정: 20 -> 25)
        45: (150, 150) # Score 45 달성 시 (수정: 25 -> 45)
    }

    def __init__(self):
        super().__init__()
        
        self.current_score_stage = 0
        # 초기 크기 설정: 튜플의 첫 번째 값(가로 크기)을 사용
        self.size_w, self.size_h = self.STAGES[self.current_score_stage]
        self.size = self.size_w # 대표 크기를 정수형으로 저장
        
        # 플레이어 물고기 이미지 로드
        try:
            self.original_image = pygame.image.load("fish01.png").convert_alpha()
        except pygame.error:
            # 이미지 파일이 없을 경우 임시 Surface 생성
            print("Warning: fish01.png not found. Using a default red block.")
            size_px = self.STAGES[0][0]
            self.original_image = pygame.Surface((size_px, int(size_px * 0.75)))
            self.original_image.fill(red)
            self.original_image.set_colorkey(black) # 투명도 설정

        self.facing_right = True # 초기 방향은 오른쪽
        self.size_update_rect() # 초기 이미지 및 rect 설정

        # 초기 위치: 화면 중앙
        self.rect.centerx = width // 2
        self.rect.centery = height // 2
        self.speed = 4 # 이동 속도

    def size_update_rect(self):
        # 현재 크기(self.size)에 맞춰 rect 업데이트
        # self.size는 정수값(가로 크기)
        self.image = pygame.transform.scale(
            self.original_image, 
            (self.size, int(self.size * 0.75)) # 가로세로 비율 유지 (임의로 0.75 비율 적용)
        )

        # 이미지 방향(좌우 반전) 설정 (기본은 오른쪽을 바라보게)
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

        # rect 업데이트: rect의 중심을 유지하면서 크기 변경
        if hasattr(self, 'rect'):
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
        else:
            self.rect = self.image.get_rect()

    def check_size(self, current_score):
        # 점수에 따라 물고기의 크기 변경
        new_size_set = False

        # STAGES를 점수 순서대로 반복
        for target_score, target_size_tuple in sorted(self.STAGES.items()):
            target_size = target_size_tuple[0]

            # 현재 점수가 다음 단계 점수에 도달했고, 현재 크기가 다음 단계 크기보다 작다면
            if current_score >= target_score and self.size < target_size:
                print(f"LEVEL UP! Size: {target_size}")
                self.size = target_size
                self.current_score_stage = target_score
                self.size_update_rect()
                new_size_set = True
                break
        return new_size_set

    def update(self):
        keys = pygame.key.get_pressed()
        
        # 이동 방향 감지 (이미지 반전)
        if keys[pygame.K_LEFT]:
            if self.facing_right:
                self.facing_right = False
                self.size_update_rect()
        elif keys[pygame.K_RIGHT]:
            if not self.facing_right:
                self.facing_right = True
                self.size_update_rect()

        # 화면 경계 이탈 방지
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(width, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(height, self.rect.bottom)

class SubFish(pygame.sprite.Sprite):
    # 크기를 정수(가로 크기)로 변경하여 SubFish.__init__에서 오류를 방지
    FISH_SPECS = {
        'sub_fish01': {"file": "fish02.png", "size": 25, "direction": "left"}, 
        'sub_fish02': {"file": "fish03.png", "size": 60, "direction": "left"}, 
        'sub_fish03': {"file": "fish04.png", "size": 100, "direction": "right"}, 
        'sub_fish04': {"file": "fish05.png", "size": 130, "direction": "left"}, 
    }

    def __init__(self, fish_type):
        super().__init__()
        self.fish_type = fish_type 
        spec = self.FISH_SPECS[fish_type]
        file_name, size, direction = spec["file"], spec["size"], spec["direction"]

        self.size = size # 정수형 가로 크기
        self.direction = direction

        # 이미지 로드 및 크기 설정
        try:
            self.original_image = pygame.image.load(file_name).convert_alpha()
        except pygame.error:
            # 이미지 파일이 없을 경우 임시 Surface 생성
            print(f"Warning: {file_name} not found. Using a default gray block.")
            size_px = self.size
            self.original_image = pygame.Surface((size_px, int(size_px * 0.75)))
            self.original_image.fill(gray)
            self.original_image.set_colorkey(black)
            
        self.image = pygame.transform.scale(
            self.original_image, 
            (self.size, int(self.size * 0.75))
        )
        self.rect = self.image.get_rect()
        self.random_position(direction) # rect 설정 후 위치 지정

    # 새 물고기 생성(랜덤으로)
    def random_position(self, direction):
        # 물고기가 화면 세로 중앙 영역(20% ~ 70%)에서 생성되도록 설정
        self.rect.y = random.randint(int(height * 0.20), int(height * 0.70) - self.size)

        if direction == "right":
            # 왼쪽 밖에서 시작
            self.rect.x = random.randint(-self.size * 2, -10) 
        elif direction == "left":
            # 오른쪽 밖에서 시작
            self.rect.x = random.randint(width + 10, width + self.size * 2) 

        # 속도 랜덤 설정
        self.speed_x = random.randint(1, 4)
        if direction == "left":
            self.speed_x *= -1 # 왼쪽으로 이동

    def update(self):
        # 물고기를 수평으로 이동
        self.rect.x += self.speed_x

        # 화면 오른쪽 경계 이탈 (왼쪽으로 이동하는 물고기)
        if self.speed_x < 0 and self.rect.right < 0:
            self.random_position("left") # 왼쪽으로 이동하는 물고기는 왼쪽 밖에서 재생성

        # 화면 왼쪽 경계 이탈 (오른쪽으로 이동하는 물고기)
        elif self.speed_x > 0 and self.rect.left > width:
            self.random_position("right") # 오른쪽으로 이동하는 물고기는 오른쪽 밖에서 재생성


# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group() 
sub_fishes = pygame.sprite.Group() 

# 플레이어 객체 생성
player = Player()
all_sprites.add(player)

# 서브 물고기 객체 생성
def create_sub_fishes():
    for fish_type in SubFish.FISH_SPECS.keys():
        num_to_create = random.randint(1, 3) 
        for _ in range(num_to_create):
            new_fish = SubFish(fish_type)
            all_sprites.add(new_fish)
            sub_fishes.add(new_fish)

create_sub_fishes()

clock = pygame.time.Clock() # FPS

def draw_text(surf, text, size, x, y, color=white):
    if size == 48:
        text_font = font_kor
    else: 
        text_font = font_eng 

    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)

# 게임 오버, 목숨(3)
def draw_score_and_lives():
    draw_text(screen, f"Score: {score} (Size: {player.size})", 30, 10, 10, black)
    draw_text(screen, f"Lives: {lives}", 30, 10, 40, black)

def show_game_over_screen():
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 0, 0, 150)) 
    screen.blit(s, (0, 0))

    text_go = font_kor.render("GAME OVER", True, white) 
    rect_go = text_go.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text_go, rect_go)

    text_score = font_eng.render(f"Final Score: {score}", True, white) 
    rect_score = text_score.get_rect(center=(width // 2, height // 2))

    screen.blit(text_score, rect_score)

    text_restart = font_eng.render("Press ENTER to Restart", True, white) 
    rect_restart = text_restart.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(text_restart, rect_restart)

def show_game_win_screen():
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 200, 0, 150)) # 승리 시 배경색을 녹색 계열로 변경
    screen.blit(s, (0, 0))

    # 점수 다 획득해서 물고기가 다 크면 출력
    text_win = font_kor.render("물고기가 다 자랐습니다!", True, black) 
    rect_win = text_win.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text_win, rect_win)
    
    # 승리시 점수
    text_score = font_eng.render(f"Final Score: {score}", True, black) 
    rect_score = text_score.get_rect(center=(width // 2, height // 2))
    screen.blit(text_score, rect_score)

    # 리셋문구
    text_restart = font_eng.render("Press ENTER to Restart", True, black) 
    rect_restart = text_restart.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(text_restart, rect_restart)

# 게임 재시작 함수
def reset_game():
    global lives, score, game_over, game_win, player 

    # 게임 상태 초기화
    lives = 3 
    score = 0 
    game_over = False
    game_win = False

    # 모든 스프라이트 그룹 비우기
    all_sprites.empty()
    sub_fishes.empty()

    # 플레이어 재생성
    player = Player()
    all_sprites.add(player)

    # 서브 물고기 재생성
    create_sub_fishes()

# 게임 루프
running = True
while running:

    clock.tick(60) # FPS 설정

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (game_over or game_win) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset_game()

    # 게임 상태 업데이트
    if not game_over and not game_win:
        keys = pygame.key.get_pressed()
        player.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player.speed
        player.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player.speed

        player.update() 
        sub_fishes.update() 

        hits = pygame.sprite.spritecollide(player, sub_fishes, False)

        for hit_fish in hits:
            
            # 크기 비교
            if player.size >= hit_fish.size:
                # 먹기 성공
                score += 1
                hit_fish.kill()
                
                # 먹은 물고기(충돌한 애)랑 같은애 재생성
                new_fish = SubFish(hit_fish.fish_type)
                all_sprites.add(new_fish)
                sub_fishes.add(new_fish)

                player.check_size(score)

            else:
                # 현재 사이즈보다 큰 물고기랑 부딪힌 경우 목숨하나 줄어듦.
                lives -= 1
                hit_fish.kill()
                
                # 부딪힌 물고기랑 같은 애로 재생성
                new_fish = SubFish(hit_fish.fish_type)
                all_sprites.add(new_fish)
                sub_fishes.add(new_fish)

                if lives <= 0:
                    game_over = True

        # 게임 승리 조건 확인 (최대 크기 진화 점수인 45점 이상, STAGES의 마지막 키)
        if player.size == player.STAGES[45][0]: 
            game_win = True

    # 그리기 (Draw)
    screen.fill(blue) 
    all_sprites.draw(screen) 

    draw_score_and_lives() 

    if game_over:
        show_game_over_screen()
    elif game_win:
        show_game_win_screen()

    pygame.display.flip() 

# Pygame 종료
pygame.quit()
sys.exit()