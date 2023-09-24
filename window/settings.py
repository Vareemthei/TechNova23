import pygame

WINDOW_NAME = "Placeholder"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

# FPS
FPS = 90
DRAW_FPS = True

# FRAME DISPLAY
FRAME_DISPLAY = False

# sizes
BUTTONS_SIZE = (400, 90)

CHARACTER_SIZE = (300, 480)

# animation
ANIMATION_SPEED = 0.8  # seconds per frame

# difficulty
LEVEL_DURATION = 60  # in seconds

# colors
COLORS = {
    "title": (255, 240, 240),
    "score": (255, 240, 240),
    "timer": (255, 240, 240),
    "timer_warning": (160, 40, 0),
    "buttons": {
        "default": (185, 118, 245),
        "second":  (210, 162, 244),
        "text": (255, 240, 240),
        "shadow": (127, 81, 168)
    }
}  # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16  # value between 0 and 1
SOUNDS_VOLUME = 1

CLICK_SOUND = None

# fonts
pygame.font.init()
DEFAULT_FONT_PATH = "assets/fonts/ARCADECLASSIC.ttf"

FONTS = {}
FONTS["small"] = pygame.font.Font(DEFAULT_FONT_PATH, 40)
FONTS["medium"] = pygame.font.Font(DEFAULT_FONT_PATH, 72)
FONTS["big"] = pygame.font.Font(DEFAULT_FONT_PATH, 120)

# images
GEM_IMAGE = "assets/images/gem.png"

BACKGROUND_IMAGE = "assets/images/background.png"

# buttons images
# START_BUTTON_IMAGE = "assets/images/buttons/start.png"
# QUIT_BUTTON_IMAGE = "assets/images/buttons/quit.png"
