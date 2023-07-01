import pygame
import random
from pygame.locals import *
from pygame.sprite import *
import time

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

clock = pygame.time.Clock()
######
screen_width = 1000
screen_height = 700
####component create
font = pygame.font.Font(None, 36) 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BROMATO")

###sprite gruppe 
all_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()

###add monster
for i in range(10):
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

    if countdown <=0:
        running=False

    timer_text = font.render(f"Countdown:{countdown}",True,(255,255,255))

    #####update the sprite
    all_sprites.update()

    ####collision detection
    hits = pygame.sprite.spritecollide(player,monsters,True)
    
    for hit in hits:
        counter = counter+1
        monster = Monster()
        monster.image.fill((50+counter*1.2,0+counter*0.5,0+counter))
        player.image.fill((40+counter*1.1,counter*1+100,2+counter))
        all_sprites.add(monster)
        monsters.add(monster)

    screen.fill("gray")
    score = font.render(str(counter),True,(0,0,0))

    screen.blit(score,(10,10))
    screen.blit(timer_text,((screen_width-timer_text.get_width())/2,10))
        
    all_sprites.draw(screen)
    #add player on the screen
 
    pygame.display.flip()#display the work on screen

    clock.tick(60) ##FPS 60

###end UI
end_game(counter)

pygame,quit()

#####todo:
#
 