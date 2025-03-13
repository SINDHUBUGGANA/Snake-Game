# main.py
import pygame
from menu import main_menu
from game import game_loop
from settings import *

# Initialize pygame
pygame.init()

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Start background music
pygame.mixer.init()
pygame.mixer.music.load("assets/background_music.mp3")  # Make sure the file exists in the assets folder
pygame.mixer.music.play(-1)  # Loop indefinitely

# Show main menu
main_menu(win)

# Start the game
game_loop(win)
