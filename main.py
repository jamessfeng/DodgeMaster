# Lets make a game
# James Feng
import pygame
import os
import random
from Colours import *
from Entities import *
from abc import ABC, abstractmethod

os.environ['SDL_AUDIODRIVER'] = 'dummy'
# Define some colors


class main(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dodge Master")
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.playtime = 0.0

        self.playerList = pygame.sprite.Group()
        self.itemList = pygame.sprite.Group()
        self.enemyList = pygame.sprite.Group()

        self.player = Character()
        self.playerList.add(self.player)
        self.enemyList.add(Enemy(5, 5, 5, 5))

    def run(self):

        running = True
        lastItemSpawn = 0
        lastEnemyTick = 0
        lastEnemySpawn = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000
            lastItemSpawn += milliseconds
            lastEnemyTick += milliseconds
            lastEnemySpawn += milliseconds
            # Enemy Spawner
            if lastEnemySpawn > 1000:
                # Which side to spawn on
                # Spawn on left side
                rand = random.randint(1, 4)
                if rand == 1:
                    self.enemyList.add(Enemy(0, random.randint(0, self.height - 10),
                                             random.randint(1, 10), random.randint(-10, 10)))
                # Spawn on right side
                elif rand == 2:
                    self.enemyList.add(Enemy(self.width, random.randint(0, self.height - 10),
                                             random.randint(-10, -1), random.randint(-10, 10)))
                # Spawn on top side
                elif rand == 3:
                    self.enemyList.add(Enemy(random.randint(0, self.width - 10), 0,
                                             random.randint(-10, 10), random.randint(1, 10)))
                # Spawn on bottom side
                elif rand == 4:
                    self.enemyList.add(Enemy(random.randint(0, self.width - 10), self.height - 10,
                                             random.randint(-10, 10), random.randint(-10, -1)))
                lastEnemySpawn = 0

            # Enemy Movement
            if lastEnemyTick > 100:
                for enemy in self.enemyList:
                    enemy.move()
                lastEnemyTick = 0

            # Item Spawner
            if lastItemSpawn > 1500:
                rand = random.randint(1, 2)
                if rand == 1:
                    self.itemList.add(SpeedUp(random.randint(0, self.width - 20),
                                              random.randint(0, self.width - 20), 20, 20))
                elif rand == 2:
                    self.itemList.add(IncreaseSize(random.randint(0, self.width - 20),
                                                   random.randint(0, self.width - 20), 20, 20))
                lastItemSpawn = 0

            # Item pickup
            collisionList = pygame.sprite.spritecollide(self.player, self.itemList, True)
            for collision in collisionList:
                collision.upgrade(self.player)

            # Enemy Collision
            collisionList = pygame.sprite.spritecollide(self.player, self.enemyList, True)
            for collision in collisionList:
                running = False
                print("HIT AND DEAD")
            #   TO DO:
            #   SPEED CHECKING
            #   SPEED CANNOT EXCEED WIDTH AND HEIGHT OF THE PLAYER

            # Checking if player moves out of bounds
            if self.player.x < 0:
                self.player.x = 0
            elif self.player.x + self.player.width > self.width:
                self.player.x = self.width - self.player.width
            elif self.player.y < 0:
                self.player.y = 0
            elif self.player.y + self.player.height> self.height:
                self.player.y = self.height - self.player.height

            # Collision Checking



            # Getting key
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.moveLeft()
            if keys[pygame.K_RIGHT]:
                self.player.moveRight()

            if keys[pygame.K_UP]:
                self.player.moveDown()

            if keys[pygame.K_DOWN]:
                self.player.moveUp()

            self.screen.fill(BLACK)

            self.playerList.draw(self.screen)
            self.playerList.update()
            self.itemList.draw(self.screen)
            self.itemList.update()
            self.enemyList.draw(self.screen)
            self.enemyList.update()

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    # call the main function
    main().run()