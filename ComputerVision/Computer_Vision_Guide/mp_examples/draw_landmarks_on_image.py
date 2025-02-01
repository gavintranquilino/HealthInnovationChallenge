import cv2
import mediapipe as mp

# Initialize MediaPipe Pose class and drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Load the image from file
image_path = 'images/pose.jpg'  # Replace with your image file path
image = cv2.imread(image_path)

# Convert the image color from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize Pose Estimation with default parameters
with mp_pose.Pose(static_image_mode=True) as pose:
    # Process the image to detect the pose
    result = pose.process(image_rgb)


    if result.pose_landmarks:

        landmark = result.pose_landmarks.landmark
        print(landmark)

        # landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility

        # landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x

        # Draw pose landmarks on the image
        mp_drawing.draw_landmarks(
            image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0,180,240), thickness=3, circle_radius=3), 
            mp_drawing.DrawingSpec(color=(180,140,0), thickness=3, circle_radius=3), 
        )



# Display the result
cv2.imshow('Pose Detection', image)

# Wait until a key is pressed and then close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
