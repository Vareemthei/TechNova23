import cv2
import mediapipe as mp
import numpy as np


# MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def calculate_angle(a, b, c):
    a = np.array(a)  # first point
    b = np.array(b)  # mid point
    c = np.array(c)  # end point

    # calculates angle between points
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
        np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)  # converts to degrees

    if angle > 180.0:
        angle = 360-angle  # if angle is greater than 180, subtract from 360

    return angle


class PoseTracking:
    def __init__(self):
        self.pose_tracking = mp_pose.Pose(
            min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.shoulder = 0
        self.elbow = 0
        self.wrist = 0
        self.angle = 0
        self.counter = 0
        self.stage = None
        self.disable_pose = False

    def scan_pose(self):
        cap = cv2.VideoCapture(0)
        image = None

        while True:
            if self.disable_pose:
                break

            ret, frame = cap.read()  # DON'T DELETE RET!
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # converts to RGB
            image.flags.writeable = False

            self.results = self.pose_tracking.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks try and catch incase cant exteact landmarks
            try:
                landmarks = self.results.pose_landmarks.landmark  # extracts landmarks

                # Get coordinates
                self.shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]  # gets shoulder coordinates
                self.elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]  # gets elbow coordinates
                self.wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]  # gets wrist coordinates

                # Calculate angle
                self.angle = calculate_angle(
                    self.shoulder, self.elbow, self.wrist)  # calculates angle

                # Visualize angle
                cv2.putText(image, str(self.angle),
                            # puts angle on screen
                            tuple(np.multiply(self.elbow, [
                                  640, 480]).astype(int)),
                            # text color and size
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,
                                                            255, 255), 2, cv2.LINE_AA
                            )

                # Curl counter logic
                if self.angle > 160:
                    self.stage = "down"
                if self.angle < 30 and self.stage == 'down':
                    self.stage = "up"
                    self.counter += 1
            except:
                pass

        return image

    def get_counter(self):
        return self.counter

    def set_disable_pose(self, disable_pose):
        self.disable_pose = disable_pose

    def display_pose(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)
