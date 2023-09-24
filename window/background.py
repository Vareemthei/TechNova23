import pygame

import utils.image as image
from window.settings import *


class Background:
    def __init__(self, ID=0):
        self.image = image.load(
            BACKGROUND_IMAGE[ID],
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            convert="default"
        )

    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2,
                   SCREEN_HEIGHT//2), pos_mode="center")
