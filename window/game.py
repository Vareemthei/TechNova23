import time
import random

import pygame
import cv2

import window.ui as ui
from window.settings import *
from window.background import Background
from movement_tracking.pose_tracking import PoseTracking


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        # Load camera
        self.cap = cv2.VideoCapture(0)
        self.camera_loaded = False

        # Start Pose Tracking

    # LOADING
    def reset(self):  # reset all the needed variables
        # MOVEMENT TRACKING

        # GAME DATA
        self.score = 0
        self.game_start_time = time.time()

    def load_camera(self):
        _, self.frame = self.cap.read()
        self.camera_loaded = True
        

    # UPDATE GAME DATA
    def update_score(self):
        if self.pose.is_bicep_curled():
            self.score += 1
        pass

    def game_time_update(self):
        self.time_left = max(
            round(LEVEL_DURATION - (time.time() - self.game_start_time), 1), 0)

    # UPDATE DISPLAY
    def draw(self):
        # draw the background
        self.background.draw(self.surface)

        # draw the character

        # draw the webcam display

        # draw the score
        ui.draw_text(
            self.surface,
            f"Score : {self.score}",
            (5, 5), COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255, 255, 255)
        )

        # draw the time left
        # change the text color if less than 5 s left
        timer_text_color = (
            160, 40, 0) if self.time_left < 5 else COLORS["timer"]
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONTS["medium"],
                     shadow=True, shadow_color=(255, 255, 255))

    def update(self):
        self.game_time_update()
        self.draw()
        if self.camera_loaded == False:
            self.load_camera();
            self.pose = PoseTracking()
            self.pose.scan_pose()



        if self.time_left > 0:
            # TODO: write the main game loop
            pass

        else:  # when the game is over
            if ui.button(self.surface, 540, "Continue"):
                return "menu"

        # cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
