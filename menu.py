# menu.py
import pygame
from settings import *

def main_menu(win):
    win.fill(BLACK)
    font = pygame.font.SysFont("bahnschrift", 30)
    message1 = font.render("Snake Game", True, YELLOW)
    message2 = font.render("Press S to Start", True, WHITE)
    message3 = font.render("Press Q to Quit", True, WHITE)

    win.blit(message1, (WIDTH // 3, HEIGHT // 5))
    win.blit(message2, (WIDTH // 3, HEIGHT // 3))
    win.blit(message3, (WIDTH // 3, HEIGHT // 2.5))
    
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
