# game.py
import pygame
import random
from settings import *
from menu import choose_difficulty

def draw_snake(win, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE], border_radius=3)

def display_score(win, score, high_score):
    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, YELLOW)
    win.blit(score_text, [10, 10])

def game_loop(win):
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0

    difficulty = choose_difficulty(win)
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
            show_message(win, "You Lost! Press C to Play Again or Q to Quit", RED, WIDTH // 6, HEIGHT // 3)
            display_score(win, score, high_score)
            pygame.display.update()
            #game_over_sound.play()  # Play game over sound

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        game_loop(win)  # Restart game

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

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        win.fill(BLUE)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE], border_radius=3)
        display_score(win, score, high_score)

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(win, snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1
            score += 10
            #eat_sound.play()  # Play eating sound

            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))

        clock.tick(speed)

    pygame.quit()
    quit()
