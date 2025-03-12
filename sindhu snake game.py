import pygame
import random

# Initialize pygame
pygame.init()

# Display window
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sindhu Snake Game")

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (213, 50, 80)

# Snake properties
BLOCK_SIZE = 10  # Size of snake block
SPEED = 10  # Speed of the snake

# Font
font = pygame.font.SysFont("bahnschrift", 25)

# Game loop function
def game_loop():
    # Initial positions
    snake_x, snake_y = WIDTH // 2, HEIGHT // 2  # Start at center
    dx, dy = 0, 0  # Movement variables

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x = random.randint(0, WIDTH - BLOCK_SIZE) // 10 * 10
    food_y = random.randint(0, HEIGHT - BLOCK_SIZE) // 10 * 10

    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        while game_over:
            win.fill(BLACK)
            message = font.render("Game Over! Press S to Play Again or Q to Quit", True, RED)
            win.blit(message, (WIDTH // 6, HEIGHT // 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_s:
                        game_loop()  # Restart the game

        win.fill(BLACK)  # Clear the screen

        # Draw food
        pygame.draw.rect(win, (255, 0, 0), (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        # Draw snake
        for part in snake_list:
            pygame.draw.rect(win, GREEN, (part[0], part[1], BLOCK_SIZE, BLOCK_SIZE))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK_SIZE

        # Move the snake
        snake_x += dx
        snake_y += dy

        # Add new head to the snake
        snake_head = (snake_x, snake_y)
        snake_list.append(snake_head)

        # Keep the length of the snake
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check collision with walls
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_over = True  # End the game if snake hits the wall

        # Check collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True  # End the game if snake collides with itself

        # Check if snake eats food
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randint(0, WIDTH - BLOCK_SIZE) // 10 * 10
            food_y = random.randint(0, HEIGHT - BLOCK_SIZE) // 10 * 10
            snake_length += 1  # Increase the length of the snake

        pygame.display.update()
        clock.tick(SPEED)  # Control game speed

    pygame.quit()

# Run the game
game_loop()
