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
        # Draw exercises
        pygame.draw.rect(
            self.surface,
            COLORS["title_bg"],
            (150, 45, SCREEN_WIDTH - 300, 175),
            border_radius=20
        )
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                     shadow=True, shadow_color=(255, 255, 255), pos_mode="center")

    def update(self):
        self.draw()
        if ui.button(self.surface, 320, "CURRENT MOVE", click_sound=self.click_sound):
            return "game"

        if ui.button(self.surface, 320+BUTTONS_SIZE[1]*1.5, "NEXT MOVE", click_sound=self.click_sound):
            pass
