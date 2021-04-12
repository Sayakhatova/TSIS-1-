import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

#const
black=(0, 0, 0)
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
SCREEN_HEIGHT=600
SCREEN_WIDTH=400
speed=5
score=0

fps=60
FPS=pygame.time.Clock()

#screen
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(white)
pygame.display.set_caption('GAME')

#font
font=pygame.font.SysFont('timesnewroman', 60)
font1=pygame.font.SysFont('timesnewroman', 20)
game_over=font.render('GAME OVER', True, black)

#backround
backround=pygame.image.load("AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Enemy.png")
        self.surf=pygame.Surface((42, 70))
        self.rect=self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), 0))

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom>600):
            score+=1
            self.rect.top=0
            self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image=pygame.image.load("Player.png")
        self.surf=pygame.Surface((40, 75))
        self.rect=self.surf.get_rect(center=(160, 520))
       
    def move(self):
        pressed_keys=pygame.key.get_pressed()

        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right<SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


INC_SPEED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED, 1000)

E=Enemy()
P=Player()

enemies=pygame.sprite.Group()
enemies.add(E)
all=pygame.sprite.Group()
all.add(E)
all.add(P)

while True:
    #exit game
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE | pygame.K_F4:
                pygame.quit()
    screen.blit(backround, (0, 0))
    scores=font1.render(str(score), True, black)
    screen.blit(scores, (10, 10))

    for entity in all:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        screen.fill(red)
        screen.blit(game_over, (30, 250))

        pygame.display.update()

        for entity in all:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    pygame.display.flip()
    FPS.tick(fps)