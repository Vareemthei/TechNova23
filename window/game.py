import time
import threading

import pygame
import cv2

import window.ui as ui
from window.settings import *
from window.background import Background
from movement_tracking.pose_tracking import PoseTracking
from character.character import Character
from utils import image


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background(0)
        self.character = Character()

        # Load camera
        self.cap = cv2.VideoCapture(0)

        # Set up the pose tracking

    # LOADING
    def reset(self):  # reset all the needed variables
        # MOVEMENT TRACKING
        self.pose = PoseTracking()
        self.tracking_thread = None
        self.scanning_pose = False

        # GAME DATA
        self.score = 0
        self.game_start_time = time.time() + 3

    def load_camera(self):
        _, self.frame = self.cap.read()

    # UPDATE GAME DATA
    def update_score(self):
        self.score = self.pose.get_counter()

    def game_time_update(self):
        self.time_left = max(
            round(LEVEL_DURATION - (time.time() - self.game_start_time), 1), 0)

    # UPDATE DISPLAY
    def draw_starting_screen(self):
        # draw the background
        self.background.draw(self.surface)

        ui.draw_text(
            self.surface,
            "GET READY TO MOVE!",
            (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 150),
            COLORS["dark_text"],
            font=FONTS["big"],
            shadow=True,
            shadow_color=(255, 255, 255),
            pos_mode="center"
        )

        ui.draw_text(
            self.surface,
            "Health tip",
            (SCREEN_WIDTH//2, SCREEN_HEIGHT//2),
            COLORS["dark_text"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255),
            pos_mode="center"
        )

        ui.draw_text(
            self.surface,
            "Don't forget to drink water!",
            (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80),
            COLORS["dark_text"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255),
            pos_mode="center"
        )

    def draw(self):
        # draw the background
        self.background.draw(self.surface)

        # draw the character
        self.character.draw(self.surface)

        # draw the score
        # image.draw(self.surface, image.load(GEM_IMAGE),
        #    (20, 50), pos_mode="top_left")

        ui.draw_text(
            self.surface,
            f"Score  {self.score}",
            (20, 5),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255)
        )

        # draw the curret and next move
        ui.fake_button(self.surface, (210, 300),
                       text="Current Move", width=350, height=70)

        ui.fake_button(self.surface, (SCREEN_WIDTH - 175, 300),
                       text="Next Move", width=300, height=70)

        # draw the names for the current and next move
        ui.draw_text(
            self.surface,
            "LEFT ARM",
            (60, 400),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255)
        )

        ui.draw_text(
            self.surface,
            "BICEP CURLS",
            (30, 480),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255)
        )

        ui.draw_text(
            self.surface,
            "RIGHT ARM",
            (830, 400),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255)
        )

        ui.draw_text(
            self.surface,
            "BICEP CURLS",
            (790, 480),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255)
        )

        # draw the time left
        # change the text color if less than 5 s left
        timer_text_color = COLORS["timer_warning"] if self.time_left < 5 else COLORS["timer"]

        ui.draw_text(
            self.surface,
            f"Time Left    {self.time_left}", (SCREEN_WIDTH//2 + 20, 5),
            timer_text_color, font=FONTS["medium"],
            shadow=True, shadow_color=(255, 255, 255)
        )

    # MAIN LOOP
    def update(self):
        # TODO: when the pose tracking starts, there is a delay of like 3 sec before it starts tracking... fix that in some way

        self.load_camera()
        self.game_time_update()
        self.update_score()

        if not self.scanning_pose:
            self.scanning_pose = True

            self.tracking_thread = threading.Thread(
                target=self.pose.scan_pose, daemon=True)

            self.tracking_thread.start()

            self.draw_starting_screen()
            pygame.display.update()

            time.sleep(3)

        else:
            self.draw()

        if self.time_left < 0:  # when the game is over
            self.pose.set_disable_pose(True)
            self.tracking_thread.join()

            # return to the menu
            if ui.button(self.surface, 540, "Continue"):
                return "menu"

        if FRAME_DISPLAY:
            cv2.imshow("Frame", self.frame)

        cv2.waitKey(1)
