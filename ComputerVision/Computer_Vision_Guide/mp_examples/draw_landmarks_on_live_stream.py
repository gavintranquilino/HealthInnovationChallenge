import cv2
import mediapipe as mp

# Initialize MediaPipe Pose class and drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

# Initialize Pose Estimation with default parameters
with mp_pose.Pose() as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Convert the frame color from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect the pose
        result = pose.process(frame_rgb)

        # Draw pose landmarks on the frame
        if result.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

        # Display the output
        cv2.imshow('Pose Estimation', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
