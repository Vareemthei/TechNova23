import cv2
import mediapipe as mp
# from settings import *
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a) #first point
    b = np.array(b) #mid point
    c = np.array(c) #end point

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0]) #calculates angle between points
    angle = np.abs(radians*180.0/np.pi) #converts to degrees

    if angle >180.0:
        angle = 360-angle #if angle is greater than 180, subtract from 360

    return angle

class PoseTracking:
    def __init__(self):
        self.pose_tracking = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.shoulder = 0
        self.elbow = 0
        self.wrist = 0
        self.angle = 0
        self.counter = 0
        self.stage = None


    def scan_pose(self, image):
        rows, cols, _ = image.shape

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #converts to RGB
        image.flags.writeable = False

        self.results = self.pose_tracking.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks try and catch incase cant exteact landmarks
        try:
            landmarks = self.results.pose_landmarks.landmark #extracts landmarks  
            
            # Get coordinates
            self.shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y] #gets shoulder coordinates
            self.elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y] #gets elbow coordinates
            self.wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y] #gets wrist coordinates

            # Calculate angle
            self.angle = calculate_angle(self.shoulder, self.elbow, self.wrist) #calculates angle

            # Visualize angle
            cv2.putText(image, str(self.angle),
                        tuple(np.multiply(self.elbow, [640, 480]).astype(int)), #puts angle on screen
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA #text color and size
                        )

            # Curl counter logic  
            if self.angle > 160:
                self.stage = "down"
            if self.angle < 30 and self.stage =='down':
                self.stage="up"
                self.counter +=1
                print(self.counter)
        except:
            pass

        return image

    def get_counter(self):
        return (self.counter)


    def display_pose(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def is_bicep_curled(self):
        pass



#VIDEO FEED
# cap = cv2.VideoCapture(0)  #video caputre device/ webcam (0 represents webcam)

# counter = 0 
# stage = None

# with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#     while cap.isOpened():
#         ret, frame = cap.read() #reading the frame from webcam

#         # Recolor image to RGB
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converts to RGB
#         image.flags.writeable = False #image is no longer writeable

#         #Make detection
#         results = pose.process(image) #processes image

#         # Recolor back to BGR
#         image.flags.writeable = True #image is now writeable
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) #converts back to BGR

#         # Extract landmarks try and catch incase cant exteact landmarks
#         try:
#             landmarks = results.pose_landmarks.landmark #extracts landmarks

#             # Get coordinates
#             shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y] #gets shoulder coordinates
#             elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y] #gets elbow coordinates
#             wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y] #gets wrist coordinates

#             # Calculate angle
#             angle = calculate_angle(shoulder, elbow, wrist) #calculates angle

#             # Visualize angle
#             cv2.putText(image, str(angle),
#                         tuple(np.multiply(elbow, [640, 480]).astype(int)), #puts angle on screen
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA #text color and size
#                         )
            
#             # Curl counter logic
#             if angle > 160:
#                 stage = "down"
#             if angle < 30 and stage =='down':
#                 stage="up"
#                 counter +=1
#                 print(counter)

#         except:
#             pass

#         # Render curl counter
#         cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1) #creates rectangle for counter

#         # Render detections 
#         mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                   mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
#                                   mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
#                                   )

        
#         cv2.imshow('MediaPipe Feed', image) #creates popup to visualize image

#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             #if hit q breaks feed
#             break

# cap.release()
# cv2.destroyAllWindows()

# shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
# elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
# wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

# angle = calculate_angle(shoulder, elbow, wrist)