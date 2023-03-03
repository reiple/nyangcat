import pygame.sprite
import random

class Nemo(pygame.sprite.Sprite):
    def __init__(self, name: str):
        super().__init__()

        # 이미지 불러오기
        self.image = pygame.image.load('res/nemo001.png')

        # 이미지 직사각형 불러오기
        self.rect = self.image.get_rect()

        # 이미지 축소
        self.rect = self.rect.inflate(0, 0)
        print("", name, ": ", self.rect)

        # 이미지 시작 위치
        rand_x = random.randrange(10, 400)
        self.rect.center = (rand_x, -100)

    def move(self):
        if self.rect.bottom < 500:
            self.rect.move_ip(0, 5)
        else:
            # 화면 밖으로 나가서 화면 위로 옮기고 위치 재조정
            self.rect.center = (10, -100)
            rand_x = random.randrange(10, 400)
            self.rect.center = (rand_x, -100)
            print("장애물 위치 이동: ", rand_x)
