import pygame.sprite
import pygame
from pygame.locals import *


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 이미지 불러오기
        self.image = pygame.image.load('res/cat003.png')

        # 이미지 직사각형 불러오기
        self.rect = self.image.get_rect()

        # 이미지 축소
        self.rect = self.rect.inflate(-100, -200)
        print("ITEM001: ", self.rect)

        # 이미지 시작 위치
        self.rect.center = (220, 330)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                return self.rect.center

        if self.rect.right < 640:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                return self.rect.center

