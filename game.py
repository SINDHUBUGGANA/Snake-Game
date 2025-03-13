# game.py
import pygame
import random
import time
from settings import *

def draw_snake(win, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE], border_radius=3)

def display_score(win, score, high_score):
    font = pygame.font.SysFont("bahnschrift", 25)
    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, YELLOW)
    win.blit(score_text, [10, 10])

def game_loop(win):
    # Load high score
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0

    # Game variables
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake_list = []
    snake_length = 1
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    score = 0

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        win.fill(BLUE)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE], border_radius=3)
        display_score(win, score, high_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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

        # Collision checks
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            running = False

        # Snake mechanics
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                running = False

        draw_snake(win, snake_list)
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

        clock.tick(SPEEDS["Medium"])  # Default speed

    pygame.quit()
    quit()
