import pygame
from window.settings import *

from utils import image as img
# OPTIONAL: add a +1 display when a point is scored


def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
              shadow=False, shadow_color=(0, 0, 0), shadow_offset=2):
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow:  # make the shadow
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset,
                     label_rect.y + shadow_offset))

    surface.blit(label, label_rect)  # draw the text


# def button2(surface, pos_y, image, click_sound=None):
#     image = img.load(image)
#     rect = image.get_rect()

#     # Position the button in the center (horizontally)
#     rect.x = SCREEN_WIDTH//2 - rect.w//2
#     rect.y = pos_y

#     on_button = False

#     if rect.collidepoint(pygame.mouse.get_pos()):
#         on_button = True

#     if on_button and pygame.mouse.get_pressed()[0]:
#         if click_sound is not None:
#             click_sound.play()
#         return True


# TODO: test and add the quit button

def button(surface, pos_y, text=None, click_sound=None):
    rect = pygame.Rect(
        (SCREEN_WIDTH//2 - BUTTONS_SIZES[0]//2, pos_y), BUTTONS_SIZES)

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["buttons"]["second"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    # draw the shadow rectangle
    pygame.draw.rect(
        surface,
        COLORS["buttons"]["shadow"],
        (rect.x - 6, rect.y - 6, rect.w, rect.h),
        border_radius=10
    )
    pygame.draw.rect(
        surface,
        color,
        rect,
        border_radius=10
    )  # draw the rectangle
    # draw the text
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["buttons"]["text"], pos_mode="center",
                  shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    # if the user press on the button
    if on_button and pygame.mouse.get_pressed()[0]:
        if click_sound is not None:  # play the sound if needed
            click_sound.play()
        return True
