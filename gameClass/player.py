import pygame
import random
from pygame.sprite import *
import os




class Player(pygame.sprite.Sprite):

    def __init__(self):
        player_img   = pygame.image.load(os.path.join("image","Sad_tomato.png"))
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.transform.scale(player_img,(60,55))
       ## self.image.set_colorkey((255,255,255))## get rid of (r,b,g)
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(0,1000-self.rect.width)
        self.rect.y = random.randint(0,650-self.rect.height)
        self.speed = 10
        self.hp = 100
    def update(self):
    
        movement = pygame.key.get_pressed()
        if movement[pygame.K_w] or movement[pygame.K_UP]:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.speed
        if movement[pygame.K_s] or movement[pygame.K_DOWN]:
            if self.rect.y >= 650:
                self.rect.y = 650
            else:
                self.rect.y += self.speed
        if movement[pygame.K_a] or movement[pygame.K_LEFT]:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.speed
        if movement[pygame.K_d] or movement[pygame.K_RIGHT]:
            if self.rect.x >= 950:
                self.rect.x = 950
            else:
                self.rect.x += self.speed