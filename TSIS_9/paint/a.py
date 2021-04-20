import pygame, sys, time

pygame.init()

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
PURPLE=(148, 0, 211)
YELLOW=(255, 255, 0)
ORANGE=(255, 140, 0)
DARKBLUE=(0, 0, 139)

prevPoint=(0, 0)
curPoint=(0, 0)

currentTool=0
toolCount=4

current_color=0
colors=(RED, ORANGE, YELLOW, GREEN, BLUE, DARKBLUE, PURPLE, BLACK)

screen=pygame.display.set_mode((800, 600))
screen.fill(WHITE)
pygame.display.set_caption('PAINT')

e=pygame.image.load('eraser.png')
t=pygame.image.load('trash.png')
c=pygame.image.load('circle.png')
r=pygame.image.load('rect.png')

def draw_rectangle(surface, color, x, y, h, w):
    pygame.draw.rect(surface, color, (x, y, h, w), 5)
def draw_rect(surface, color, x, y, h, w):
    pygame.draw.rect(surface, color, (x, y, h, w))
def draw_circle(surface, color, x, y):
    pygame.draw.circle(surface, color, (x, y), 30, 3)
def draw_line(surface, color, startPos, endPos):
    pygame.draw.line(surface, color, startPos, endPos, 2)
def erase(surface, x, y):
    pygame.draw.circle(surface, WHITE, (x, y), 30)

isPressed=False

while True:
    
    draw_rect(screen, (211, 211, 211), 0, 0, 100, 600)
    
    for i in range(len(colors)):
        draw_rect(screen, colors[i], 20, (i*50+10), 60, 30)
        
    screen.blit(r, pygame.Rect(20, 410, 60, 30)) 
    screen.blit(c, pygame.Rect(20, 460, 60, 30))
    screen.blit(e, pygame.Rect(20, 510, 60, 30))
    screen.blit(t, pygame.Rect(20, 560, 60, 30))
    
    pygame.display.update()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.image.save(screen, 'screen.jpg')
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n: 
                currentTool=(currentTool+1)%toolCount
            elif event.key==pygame.K_c:
                current_color=(current_color+1)%len(colors)
            elif event.key==pygame.K_e:
                screen.fill(WHITE)

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                isPressed=True
                prevPoint=pygame.mouse.get_pos()
        elif event.type==pygame.MOUSEBUTTONUP:
            isPressed=False
        elif event.type==pygame.MOUSEMOTION:
            if isPressed:
                prevPoint=curPoint
                curPoint=pygame.mouse.get_pos()

    if currentTool==0:
        draw_line(screen, colors[current_color], prevPoint, curPoint)
    elif currentTool==1:
        draw_rectangle(screen, colors[current_color], curPoint[0], curPoint[1], 50, 50)
    elif currentTool==2:
        draw_circle(screen, colors[current_color], *curPoint)
    elif currentTool==3:
        erase(screen, *curPoint)

    pygame.display.update()