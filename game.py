import pygame
import random
from pygame.locals import *
from pygame.sprite import *
import time
import os

class Player(pygame.sprite.Sprite):

    def __init__(self):
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
        if movement[K_w]:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.speed
        if movement[K_s]:
            if self.rect.y >= 650:
                self.rect.y = 650
            else:
                self.rect.y += self.speed
        if movement[K_a]:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.speed
        if movement[K_d]:
            if self.rect.x >= 950:
                self.rect.x = 950
            else:
                self.rect.x += self.speed


class Monster(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

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

class Food(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image =pygame.transform.scale(food_img,(40,60))
       ## self.image.set_colorkey((0,0,0))## get rid of (r,b,g)
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(0,1000-self.rect.width)
        self.rect.y = random.randint(0,650-self.rect.height)
        self.speedx = 1
        self.speedy = 1

    def update(self):  
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom >=700 or self.rect.top<=0:
            self.speedy *= -1
        if self.rect.left <=0 or self.rect.right >=1000:
            self.speedx *=-1

            
####setup
pygame.init()

clock = pygame.time.Clock()


######
screen_width = 1000
screen_height = 700
####component create
font = pygame.font.Font(None, 36) 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BROMATO")

###image loading
player_img   = pygame.image.load(os.path.join("image","Sad_tomato.png")).convert_alpha()
monster_img   = pygame.image.load(os.path.join("image","Wisdom.webp")).convert_alpha()
food_img   = pygame.image.load(os.path.join("image","Lost_duck.png")).convert_alpha()
###sprite gruppe 
all_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()
foods=pygame.sprite.Group()

###add monster
for i in range(5):
    monster = Monster()
    all_sprites.add(monster)
    monsters.add(monster)

###start UI
def start_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                return
            
            if event.type == KEYDOWN:
                if event.key ==K_SPACE:
                    running = False

        screen.fill("gray")

        title = font.render("Bromato",True,(255,255,255))
        start_hint=font.render("Press SPACE to start",True,(255,255,255))

        screen.blit(title,((screen_width-title.get_width())/2,screen_height/3))
        screen.blit(start_hint,((screen_width-start_hint.get_width())/2,screen_height/3+100))

        pygame.display.flip() 

def end_game(score):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                return
            # if event.type ==KEYDOWN:
            #     if event.key == K_SPACE:
            #         start_game()
            
        screen.fill((200,200,200))
        end_text = font.render("game over,my Bromato",True,(255,255,255))
        score_text = font.render(f"Score:{score}",True,(255,255,255))

        screen.blit(end_text,(((screen_width-end_text.get_width())/2,screen_height/3)))
        screen.blit(score_text,(((screen_width-score_text.get_width())/2,screen_height/3+100)))

        pygame.display.flip()

start_game()
running = True
## add player
player = Player()
all_sprites.add(player)

#####add game parameter
counter=0 #score
game_duration=60
start_time=time.time()


while running:

    ### list of event of action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key ==K_ESCAPE:
                running = False

    ###time
    current_time = time.time()
    player_duration = int(current_time-start_time)
    countdown = game_duration-player_duration


    timer_text = font.render(f"Countdown:{countdown}",True,(255,255,255))

    #####update the sprite
    all_sprites.update()

    ####collision detection
    hits_byMonster = pygame.sprite.spritecollide(player,monsters,True)
    hits_byFood = pygame.sprite.spritecollide(player,foods,True)

    for hit in hits_byMonster:
        counter = counter+1
        monster = Monster()
        player.hp -=10
        if random.randint(1,9)%3 ==0:
            food = Food()
            all_sprites.add(food)
            foods.add(food)

        all_sprites.add(monster)
        monsters.add(monster)

    for eat in hits_byFood:
        player.hp+= random.randint(1,5)
        countdown -=10
       

    score = player.hp - countdown 
########end game singal:
    if countdown <=0:
        running=False
    if player.hp <= 0:
        running=False

#####screen rendering
    screen.fill("gray")
    score_text = font.render(f"score:{score}",True,(0,0,0))
    hp = font.render(f"hp:{player.hp}",True,(0,0,0))
    
    screen.blit(score_text,(10,10))
    screen.blit(timer_text,((screen_width-timer_text.get_width())/2,10))
    screen.blit(hp,(900,10))
        
    all_sprites.draw(screen)
    #add player on the screen
 
    pygame.display.flip()#display the work on screen

    clock.tick(60) ##FPS 60

###end UI
end_game(score)

pygame,quit()

#####todo:
#
 