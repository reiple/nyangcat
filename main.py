import pygame
import sys
from pygame.locals import *
import random
import time

from cat import Cat
from nemo import Nemo

# 게임 초기화
pygame.init()

# 프레임 설정
FPS = 60
FramePerSec = pygame.time.Clock()

# 색상 설정
RED = (255, 0, 0)

# 게임 옵션
SPEED = 5  # 게임 속도
SCORE = 0  # 게임 점수

# 폰트 설정
font = pygame.font.SysFont('Tahoma', 60)

# 게임 배경화면
background = pygame.image.load('res/background.png')

# 게임 화면 생성
GameDisplay = pygame.display.set_mode((640, 400))
GameDisplay.fill(RED)
pygame.display.set_caption("Dodo Game")

# 게임 아이템 생성
item_001 = Cat()

# 장애물 생성
nemo_001 = Nemo('nemo001')

# 그룹화
all_groups = pygame.sprite.Group()
all_groups.add(item_001)
all_groups.add(nemo_001)

# 적 개체 1초(1000ms)마다 새로 생기는 이벤트 생성
increaseSpeed = pygame.USEREVENT + 1
pygame.time.set_timer(increaseSpeed, 1000)


# 게임 배경음악
bgm = pygame.mixer.Sound('res/music-background.mp3')
bgm.play()

while True:

    for event in pygame.event.get():
        if event.type == increaseSpeed:
            SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    GameDisplay.blit(background, (0, 0))

    # 게임 내 물체 생성
    for item in all_groups:
        GameDisplay.blit(item.image, item.rect)
        item.move()

    pygame.display.update()
    FramePerSec.tick(FPS)
