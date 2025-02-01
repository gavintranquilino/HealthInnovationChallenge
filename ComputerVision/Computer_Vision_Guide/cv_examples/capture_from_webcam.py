import cv2

# Capture video from webcam
cap = cv2.VideoCapture(0) # usually takes 0 for a built-in webcam
                          # try experimenting with 1 and 2 if nothing shows up

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break


    # Display the frame
    cv2.imshow('Webcam', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()