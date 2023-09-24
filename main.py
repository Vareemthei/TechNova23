# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from window.settings import *
from window.game import Game
from window.menu import Menu


# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 32)  # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

mainClock = pygame.time.Clock()  # used to limit the fps


# Music ----------------------------------------------------------- #
# OPTIONAL: play music
# pygame.mixer.music.load("Assets/Sounds/Komiku_-_12_-_Bicycle.mp3")
# pygame.mixer.music.set_volume(MUSIC_VOLUME)
# pygame.mixer.music.play(-1)

# Variables ------------------------------------------------------- #
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)


# Functions ------------------------------------------------------ #
def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    if state == "menu":
        if menu.update() == "game":
            game.reset()  # reset the game to start a new game
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS)


# Loop ------------------------------------------------------------ #
while True:

    # Buttons ----------------------------------------------------- #
    user_events()

    # Update ------------------------------------------------------ #
    update()
