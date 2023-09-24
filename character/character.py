import time

from window.settings import *
from utils import image


class Character:
    def __init__(self):
        self.images = [image.load(
            f"assets/character/byte{nb}.png", size=CHARACTER_SIZE) for nb in range(1, 5)]
        self.current_frame = 0
        self.animation_timer = 0

    # change the frame of the character when needed
    def animate(self):
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images) - 1:
                self.current_frame = 0

    def draw(self, surface, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)):
        self.animate()

        self.animate()
        image.draw(
            surface,
            self.images[self.current_frame],
            pos,
            pos_mode="center"
        )
