import pygame, sys

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

color=BLACK
colors=(RED, ORANGE, YELLOW, GREEN, BLUE, DARKBLUE, PURPLE, BLACK)

screen=pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
pygame.display.set_caption('PAINT')

e=pygame.image.load('eraser.png')
t=pygame.image.load('trash.png')
c=pygame.image.load('circle.png')
r=pygame.image.load('rect.png')

def draw_rect(surface, color, x, y, h, w):
    pygame.draw.rect(surface, color, (x, y, h, w))

red_rect=pygame.Rect(20, 10, 60, 30)
orange_rect=pygame.Rect(20, 60, 60, 30)
yellow_rect=pygame.Rect(20, 110, 60, 30)
green_rect=pygame.Rect(20, 160, 60, 30)
blue_rect=pygame.Rect(20, 210, 60, 30)
darkblue_rect=pygame.Rect(20, 260, 60, 30)
purple_rect=pygame.Rect(20, 310, 60, 30)
black_rect=pygame.Rect(20, 360, 60, 30)
rect_rect=pygame.Rect(20, 410, 60, 30)
circle_rect=pygame.Rect(20, 460, 60, 30)
eraser_rect=pygame.Rect(20, 510, 60, 30)
trash_rect=pygame.Rect(20, 560, 60, 30)

stamp_0=pygame.transform.scale(r, (60, 30))
stamp_1=pygame.transform.scale(c, (60, 30))

draw=False
draw1=False
stamp=0

while True:
    
    draw_rect(screen, (211, 211, 211), 0, 0, 100, 600)
    
    for i in range(len(colors)):
        draw_rect(screen, colors[i], 20, (i*50+10), 60, 30)
        
    screen.blit(r, rect_rect) 
    screen.blit(c, circle_rect)
    screen.blit(e, eraser_rect)
    screen.blit(t, trash_rect)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.image.save(screen, 'screen.jpg')
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                draw=True

        if event.type==pygame.MOUSEBUTTONUP:
            draw=False

    mouse_pos=pygame.mouse.get_pos()
    if draw and mouse_pos[0]>100:
        if draw1==False: pygame.draw.circle(screen, color, mouse_pos, 5)
        elif stamp==0 and draw1: 
            screen.blit(stamp_0, (mouse_pos[0], mouse_pos[1]))
            draw=False
        elif stamp==1 and draw1:
            screen.blit(stamp_1, (mouse_pos[0], mouse_pos[1]))
            draw=False
    
    if draw:

        if red_rect.collidepoint(mouse_pos): 
            color=RED
            draw1=False
        if orange_rect.collidepoint(mouse_pos): 
            color=ORANGE
            draw1=False
        if yellow_rect.collidepoint(mouse_pos): 
            color=YELLOW
            draw1=False
        if green_rect.collidepoint(mouse_pos): 
            color=GREEN
            draw1=False
        if blue_rect.collidepoint(mouse_pos): 
            color=BLUE
            draw1=False
        if darkblue_rect.collidepoint(mouse_pos): 
            color=DARKBLUE
            draw1=False
        if purple_rect.collidepoint(mouse_pos): 
            color=PURPLE
            draw1=False
        if black_rect.collidepoint(mouse_pos): 
            color=BLACK
            draw1=False
        if eraser_rect.collidepoint(mouse_pos): 
            color=WHITE
            draw1=False
        if trash_rect.collidepoint(mouse_pos): draw_rect(screen, WHITE, 100, 0, 700, 600)

        if rect_rect.collidepoint(mouse_pos): 
            stamp=0 
            draw1=True
        if circle_rect.collidepoint(mouse_pos):
            stamp=1
            draw1=True

    pygame.display.update()