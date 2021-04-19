import pygame, sys, random, time
from pygame.math import Vector2

class MAIN:
    def __init__(self):

        self.snake=SNAKE()
        self.fruit=FRUIT()
        self.WALLS=WALLS()
    
    def update(self):

        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):

        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.WALLS.draw()

    def check_collision(self):

        if self.fruit.pos==self.snake.body[0]:
            global score 
            score+=1
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):

        if not 0<=self.snake.body[0].x<(number-1.5) or not 0<=self.snake.body[0].y<(number-1.5):
            self.game_over()

        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()

    def game_over(self):

        screen.fill((0, 0, 0))
        gameover=font.render('GAME OVER', True, (138, 43, 226)) 
        score1=font1.render('Your Score:'+str(score), True, (255, 255, 255)) 
        screen.blit(score1, (420, 530))
        text_rect=gameover.get_rect(center=(300, 300))
        screen.blit(gameover, text_rect)
        cont=font1.render('Tap SPACE to restart or ESC to exit', True, (138, 43, 226))
        screen.blit(cont, (120, 350))

        for event in pygame.event.get():

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        time.sleep(1)

    def draw_score(self):

        score_surface=font1.render('Score:'+str(score), True, (0, 0, 0)) 
        screen.blit(score_surface, (450, 530))

class SNAKE:

    def __init__(self):

        self.body=[Vector2(5, 10), Vector2(4, 10)]
        self.direction=Vector2(1, 0)
        self.new_block=False

    def draw_snake(self):

        for block in self.body:
            block_rect=pygame.Rect(block.x*size, block.y*size, size, size)
            pygame.draw.rect(screen, (138, 43, 226), block_rect)
    
    def move_snake(self):

        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.new_block=False

        else:
            body_copy=self.body[:-1]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body=body_copy[:]

    def add_block(self):

        self.new_block=True

class FRUIT:

    def __init__(self):

        self.randomize()
    
    def draw_fruit(self):

        fruit_rect=pygame.Rect(self.pos.x*size, self.pos.y*size, size, size)
        screen.blit(apple, fruit_rect)

    def randomize(self):

        self.x, self.y=random.randint(4, (number-4)), random.randint(4, (number-4))
        self.pos=Vector2(self.x, self.y)

class WALLS:

    def __init__(self):

        self.image=pygame.image.load('wall.png')
        self.x=self.image.get_height()
        self.y=self.image.get_width()

    def draw(self):

        for i in range(screen.get_width()//self.y+1):
            screen.blit(self.image, (i*self.y, 0))
            screen.blit(self.image, (i*self.y, screen.get_height()-self.x))

        for i in range(screen.get_height()//self.x + 1):
            screen.blit(self.image, (0, i*self.x))
            screen.blit(self.image, (screen.get_width()-self.y, i*self.x))

pygame.init()

font=pygame.font.SysFont('timesnewroman', 50)
font1=pygame.font.SysFont('timesnewroman', 25)
size=30
number=20
score=0

screen=pygame.display.set_mode((size*number, size*number))
pygame.display.set_caption('SNAKE GAME')

clock=pygame.time.Clock()

apple=pygame.image.load('apple.png') 
backround=pygame.image.load('grass.png')

def game():

    global score 
    score=0

    SCREEN_UPDATE=pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    main_game=MAIN()
  
    while True:
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==SCREEN_UPDATE:
                main_game.update()

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_UP:
                   main_game.snake.direction=Vector2(0, -1)
                elif event.key==pygame.K_DOWN:
                   main_game.snake.direction=Vector2(0, 1)
                elif event.key==pygame.K_LEFT:
                   main_game.snake.direction=Vector2(-1, 0)
                elif event.key==pygame.K_RIGHT:
                   main_game.snake.direction=Vector2(1, 0)
    
        screen.blit(backround, (0, 0))

        main_game.draw_elements()

        pygame.display.update()

        clock.tick(60)

start_page=pygame.image.load('start1.png')
screen.blit(start_page, (0, 0))
pygame.display.flip()
time.sleep(3)

for event in pygame.event.get():
    
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            game()