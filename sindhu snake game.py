import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Snake and game settings
BLOCK_SIZE = 10
SPEED = 15

# Font
font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], block_size, block_size])

def show_message(msg, color, x, y):
    message = font.render(msg, True, color)
    win.blit(message, [x, y])

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    win.blit(score_text, [10, 10])

def game_loop():
    game_over = False
    game_close = False
    
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    
    snake_list = []
    snake_length = 1
    
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    
    score = 0
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            win.fill(BLACK)
            show_message("You Lost! Press C to Play Again or Q to Quit", RED, WIDTH // 6, HEIGHT // 3)
            display_score(score)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK_SIZE
        
        x += dx
        y += dy
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        display_score(score)
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(BLOCK_SIZE, snake_list)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1
            score += 10
        
        clock.tick(SPEED)
    
    pygame.quit()
    quit()

# Run the game
game_loop()
