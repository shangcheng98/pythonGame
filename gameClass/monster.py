import pygame
import random
from pygame.sprite import *
import os



class Monster(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        monster_img   = pygame.image.load(os.path.join("image","Wisdom.webp")).convert_alpha()
        self.image =pygame.transform.scale(monster_img,(45,50))
        self.image.set_colorkey((255,255,255))## get rid of (r,b,g)
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(0,1000-self.rect.width)
        self.rect.y = random.randint(0,650-self.rect.height)
        self.speedx = random.randint(-8,8)
        self.speedy = random.randint(-8,8)

    def update(self):  
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom >=700 or self.rect.top<=0:
            self.speedy *= -1
        if self.rect.left <=0 or self.rect.right >=1000:
            self.speedx *=-1
