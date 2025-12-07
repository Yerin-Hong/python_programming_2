import pygame 
import sys          # sys.exit() 기능을 위한 모듈
import random       # 여기서는 안 쓰고 추후 코드에 사용할 예정.

# 게임 화면 크기
screen_width = 800
screen_height = 600

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 게임 화면 생성
pygame.init()       # pygame의 모든 모듈 초기화(pygame을 사용하기 위해 반드시 수행)
screen = pygame.display.set_mode((screen_width, screen_height))    # 위에서 정의한 screen_wi, hei를 통해 800x600 크기의 게임창 객체 생성, 이 객체를 screen 변수에 할당.
pygame.display.set_caption("Space Inverder")    # 게임 창의 제목.

# 게임 루프
while True:
    for event in pygame.event.get():    # 루프가 돌 때마다 발생한 모든 이벤트(키보드, 마우스입력 등)를 가져와 하나씩 처리.
        if event.type == pygame.QUIT:   # 처리 중인 이벤트가 창 닫기 버튼이면 ,
            pygame.quit()       # Pygame 라이브러리 종료.
            sys.exit()          # 이건 파이썬 프로그램 자체를 완전히 종료.
    screen.fill(black)

pygame.quit()