import cv2
import mediapipe as mp
from time import sleep

fhand = open("location_time.txt", "w")

# Initialize MediaPipe Pose class and drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

frames = 0

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

# User's information
total_dist = 0 # m
avg_speed = 0 # m/s
total_time = 0 # s

x_right = 0
y_right = 0
z_right = 0
x_right_new = 0
y_right_new = 0
z_right_new = 0

x_left = 0
y_left = 0
z_left = 0
x_left_new = 0
y_left_new = 0
z_left_new = 0

threshold_dist = 0.05

# Initialize Pose Estimation with default parameters
with mp_pose.Pose() as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        frames += 1

        if not ret:
            print("Failed to capture image")
            break

        frame = cv2.flip(frame, 1)

        # Convert the frame color from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect the pose
        result = pose.process(frame_rgb)

        # Draw pose landmarks on the frame
        if result.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

            if frames == 3: 
                # ----- TOTAL DISTANCE -----
                # RIGHT HAND
                x_right = x_right_new
                y_right = y_right_new
                z_right = z_right_new

                x_right_new = abs(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].x)
                y_right_new = abs(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].y)
                z_right_new = abs(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].z)
                
                # LEFT HAND
                x_left = x_left_new
                y_left = y_left_new
                z_left = z_left_new

                x_left_new = abs(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].x)
                y_left_new = abs(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].y)
                z_left_new = abs(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].z)

                d_right = ((x_right_new - x_right) ** 2 + (y_right_new - y_right) ** 2 + (z_right_new - z_right) ** 2) ** 0.5
                d_left = ((x_left_new - x_left) ** 2 + (y_left_new - y_left) ** 2 + (z_left_new - z_left) ** 2) ** 0.5

                if d_right < threshold_dist: 
                    d_right = 0
                if d_left < threshold_dist:
                    d_left = 0

                total_dist += d_left + d_right

                # ----- AVERAGE SPEED -----
                

                print("Total distance: " + str(total_dist) + " m")
                frames = 0

        # Display the output
        cv2.imshow('Pose Estimation', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
