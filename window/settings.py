import pygame

WINDOW_NAME = "Placeholder"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
CHARACTER_SIZE = (150, 150)

# drawing
DRAW_HITBOX = False  # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08  # the frame of the insects will change every X sec

# difficulty
# TODO: add difficulty?
LEVEL_DURATION = 30  # in seconds

# colors
COLORS = {
    "title": (38, 61, 39),
    "score": (38, 61, 39),
    "timer": (38, 61, 39),
    "buttons": {
        "default": (56, 67, 209),
        "second":  (87, 99, 255),
        "text": (255, 255, 255),
        "shadow": (46, 54, 163)
    }
}  # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16  # value between 0 and 1
SOUNDS_VOLUME = 1

CLICK_SOUND = None

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)

# images
BACKGROUND_IMAGE = "assets/images/background.png"
