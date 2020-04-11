import pygame
import os
import random
from Colours import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.update()
        # self.rect = self.image
        # [x, y, width, height]

    def update(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Item(Entity):
    def __init__(self, x, y, width, height, colour):
        super().__init__(x, y, width, height, colour)


class SpeedUp(Item):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, BLUE)

    def upgrade(self, player):
        player.vel *= 1.2


class IncreaseSize(Item):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, GREY)

    def upgrade(self, player):
        player.height *= 1.2
        player.width *= 1.2


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 100
        self.y = 100
        self.width = 25
        self.height = 25
        self.vel = 15
        self.colour = GREEN
        self.update()

    def moveRight(self):
        self.x += self.vel

    def moveLeft(self):
        self.x -= self.vel

    def moveUp(self):
        self.y += self.vel

    def moveDown(self):
        self.y -= self.vel

    def update(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Enemy(Entity):
    def __init__(self, x, y, xvel, yvel):
        super().__init__(x, y, 10, 10, RED)
        self.xvel = xvel
        self.yvel = yvel

    def move(self):
        self.x += self.xvel
        self.y += self.yvel