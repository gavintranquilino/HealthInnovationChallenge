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
            # print(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST])
            # if frames == 30:
            #     fhand.write("x: " + str(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x) + "\n")
            #     # fhand.write("x")
            #     frames = 0

            # Print WORLD landmark coordinates in (x, y, z) format of landmark RIGHT_WRIST
            print(str(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].z) + " " + str(result.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].z))
            
        # Display the output
        cv2.imshow('Pose Estimation', frame)

        #

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
