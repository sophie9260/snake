import pygame
import time
import random


pygame.init()

box_len = 900
box_height = 600

white = (255,255,255)
yellow = (254, 219, 30)
black = (0,0,0)
blue = (117,101,148)
green = (124, 204, 124)
red = (245, 35, 54)

add_caption = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("SNAKE GAME")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont("impact", 30)
score_font = pygame.font.SysFont("impact", 30)

def final_score(score):
    value = score_font.render("Welcome to the Snake Game ----- Your Score is : "+ str(score), True, black )
    add_caption.blit(value, [0,0])

def make_snake(snake_block, list_snake):
    for x in list_snake:
        #print(x)
        pygame.draw.rect(add_caption, green, [x[0], x[1], snake_block, snake_block])
        #pygame.draw.rect()
        
def display_msg(msg,colour):
    mssg = display_style.render(msg, True, colour)
    add_caption.blit(mssg, [box_len/6, box_height/3])

def game_start():
    game_over = False
    game_close = False

    value_x1 = box_len/2
    value_y1 = box_height/2

    new_x1 = 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, box_len-snake_block)//10.0)*10.0
    foody_pos = round(random.randrange(0, box_height-snake_block)//10.0)*10.0

    while not game_over:

        while game_close == True:
            add_caption.fill(blue)
            display_msg("You lost! Wanna play again? Press C, if not Press Q to quit ", black)
            final_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0
        if value_x1>=box_len or value_x1<0 or value_y1>=box_height or value_y1<0:
            game_close = True

        value_x1 = value_x1+new_x1
        value_y1 = value_y1+new_y1
        add_caption.fill(blue)
        pygame.draw.rect(add_caption, red, [foodx_pos, foody_pos, snake_block,snake_block])
        snake_head = []
        snake_head.append(value_x1)
        snake_head.append(value_y1)
        list_snake.append(snake_head)
        if len(list_snake)>snake_len:
            del list_snake[0]
        
        for x in list_snake[:-1]:
            if x == snake_head:
                game_close = True

        make_snake(snake_block, list_snake)
        final_score(snake_len-1)

        pygame.display.update()
        print(value_x1, foodx_pos, value_y1, foody_pos)
        
        if value_x1 == foodx_pos and value_y1 == foody_pos:
            print('collision')
            foodx_pos= round(random.randrange(0,box_len-snake_block)//10.0)*10.0
            foody_pos = round(random.randrange(0, box_height-snake_block)//10.0)*10.0
            snake_len = snake_len+1

        timer.tick(snake_speed)

    pygame.quit()
    quit()

game_start()