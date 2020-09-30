import pygame
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
 
display_width = 800
display_height  = 600
x1 = display_width/2
y1 = display_height/2
dis = pygame.display.set_mode((display_width, display_width))
pygame.display.set_caption('Snake Game')

#Initializing parameters and display settings
 
game_over = False
 
snake_block=10
 
x1_change = 0 #analog to speed
y1_change = 0
 
clock = pygame.time.Clock()
snake_speed=30
 
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width/2, display_height/2])
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
 
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("You lost!",blue)
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit()