# settings.py
import pygame

# Game Settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
SPEEDS = {"Easy": 10, "Medium": 15, "Hard": 20}

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)

# Initialize Font
pygame.font.init()
font = pygame.font.SysFont("bahnschrift", 25)
