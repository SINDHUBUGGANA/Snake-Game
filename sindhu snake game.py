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
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)

# Snake and game settings
BLOCK_SIZE = 10
SPEEDS = {"Easy": 10, "Medium": 15, "Hard": 20}

# Font
font = pygame.font.SysFont("bahnschrift", 25)

def main_menu():
    win.fill(BLACK)
    show_message("Snake Game", YELLOW, WIDTH // 3, HEIGHT // 5)
    show_message("Press S to Start", WHITE, WIDTH // 3, HEIGHT // 3)
    show_message("Press Q to Quit", WHITE, WIDTH // 3, HEIGHT // 2.5)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return  # Start the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def choose_difficulty():
    win.fill(BLACK)
    show_message("Choose Difficulty: 1-Easy  2-Medium  3-Hard", YELLOW, WIDTH // 6, HEIGHT // 3)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "Easy"
                elif event.key == pygame.K_2:
                    return "Medium"
                elif event.key == pygame.K_3:
                    return "Hard"

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], block_size, block_size], border_radius=3)

def show_message(msg, color, x, y):
    message = font.render(msg, True, color)
    win.blit(message, [x, y])

def display_score(score, high_score):
    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, YELLOW)
    win.blit(score_text, [10, 10])

def game_loop():
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0
    
    main_menu()
    difficulty = choose_difficulty()
    speed = SPEEDS[difficulty]
    
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
            win.fill(BLUE)
            show_message("You Lost! Press C to Play Again or Q to Quit", RED, WIDTH // 6, HEIGHT // 3)
            display_score(score, high_score)
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
        
        win.fill(BLUE)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE], border_radius=3)
        display_score(score, high_score)
        
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
            
            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))
        
        clock.tick(speed)
    
    pygame.quit()
    quit()

# Run the game
game_loop()