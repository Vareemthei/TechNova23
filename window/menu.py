import pygame

import sys
from window.settings import *
from window.background import Background
import window.ui as ui


class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background(1)
        self.click_sound = CLICK_SOUND

    def draw(self):
        self.background.draw(self.surface)
        # Draw the title
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                     shadow=True, shadow_color=COLORS["shadow"], pos_mode="center")

    def update(self):
        self.draw()
        if ui.button(self.surface, 320, "START", click_sound=self.click_sound):
            return "game"

        if ui.button(self.surface, 320+BUTTONS_SIZE[1]*1.5, "EXIT", click_sound=self.click_sound):
            pass
