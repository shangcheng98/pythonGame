import pygame
import random
from pygame.locals import *
from pygame.sprite import *
import time
import os

from gameClass.player import Player
from gameClass.monster import Monster
from gameClass.food import Food
from gameClass.bullet import Bullet



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
foods=pygame.sprite.Group()
bullets = pygame.sprite.Group()



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
###add monster at beginning
for i in range(3):
    monster = Monster()
    food = Food()
    all_sprites.add(monster)
    all_sprites.add(food)
    monsters.add(monster)
    foods.add(food)

#####add game parameter
counter=0 #score
game_duration=60
start_time=time.time()
fps_counter=0
hit_time = 100

while running:
    fps_counter +=1
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

    ### rate = 60 * 0.002
    if countdown%5 ==0:
        if random.randint(1,1000)%100 ==0: 
                food = Food()
                all_sprites.add(food)
                foods.add(food)
    
    if countdown%10 ==0:
        for i in range(1):
            if random.randint(1,36)%6 ==0: 
                monster = Monster()
                all_sprites.add(monster)
                monsters.add(monster)
    


    timer_text = font.render(f"Countdown:{countdown}",True,(255,255,255))

    #####update the sprite
    all_sprites.update()

    ####collision detection
    hits_byMonster = pygame.sprite.spritecollide(player,monsters,True)
    hits_byFood = pygame.sprite.spritecollide(player,foods,True)
    hits_byBullet = pygame.sprite.groupcollide(bullets,monsters,True,True)

    for hit in hits_byMonster:
        counter = counter+1
        player.hp -=10
        
    
    for eat in hits_byFood:
        hit_time = countdown
        player.hp+= random.randint(1,5)
        countdown -=10     
    if hit_time - countdown <=5:
        if fps_counter%10 ==0:
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets.add(bullet)
       

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
 