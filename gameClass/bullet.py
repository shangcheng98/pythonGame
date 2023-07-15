
import pygame
import random
from pygame.sprite import *
import os


class Bullet(pygame.sprite.Sprite):

    def __init__(self,owner):
        pygame.sprite.Sprite.__init__(self)
        bullet_img   = pygame.image.load(os.path.join("image","bullet_red.png")).convert_alpha()
        self.image =pygame.transform.scale(bullet_img,(50,50))
       ## self.image.set_colorkey((0,0,0))## get rid of (r,b,g)
        self.rect = self.image.get_rect()
        self.rect.x =owner.rect.x
        self.rect.y = owner.rect.y
        self.speedx = 15
        self.speedy = 15

    def update(self):  
            
        if self.rect.x >= 1000:
            self.kill
            
        self.rect.y -=self.speedy
       
          