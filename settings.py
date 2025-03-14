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

# Initialize Sounds
pygame.mixer.init()
pygame.mixer.music.load("assets/background_music.mp3")  # Background Music
pygame.mixer.music.play(-1)  # Loop indefinitely

