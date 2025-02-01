import cv2

# Capture video from a file
cap = cv2.VideoCapture('images/macarena_dance.mp4')

while True:
    # Read a frame from the video file
    ret, frame = cap.read()
    
    if not ret:
        break  # Break the loop if the video is finished

    # Display the frame
    cv2.imshow('Video Frame', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()
