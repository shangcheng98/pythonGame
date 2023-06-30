import pygame
import random
from pygame.locals import *
from pygame.sprite import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill((255,200,0))
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(0,1000-self.rect.width)
        self.rect.y = random.randint(0,650-self.rect.height)
        self.speed = 10

    def update(self):
        movement = pygame.key.get_pressed()
        if movement[K_UP]:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.speed
        if movement[K_DOWN]:
            if self.rect.y >= 650:
                self.rect.y = 650
            else:
                self.rect.y += self.speed
        if movement[K_LEFT]:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.speed
        if movement[K_RIGHT]:
            if self.rect.x >= 950:
                self.rect.x = 950
            else:
                self.rect.x += self.speed


class Monster(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([50,50])
        self.image.fill((0,255,0))
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







####setup
pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

###sprite gruppe 
all_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()

###add monster
for i in range(10):
    monster = Monster()
    all_sprites.add(monster)
    monsters.add(monster)

running = True
## add player
player = Player()
all_sprites.add(player)

#####add score
counter=0


while running:

    ### list of event of action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #####update the sprite
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player,monsters,True)
    
    for hit in hits:
        counter = counter+1
        print(counter)
        monster = Monster()
        monster.image.fill((50+counter*2,200-counter*2,150+counter*2))
        player.image.fill((counter*3,counter*3+100,250-counter*2))
        all_sprites.add(monster)
        monsters.add(monster)

    screen.fill("gray")

   
    all_sprites.draw(screen)
    #add player on the screen
 
    pygame.display.flip()#display the work on screen




    clock.tick(60) ##FPS 60

pygame,quit()

#####todo:
#
 