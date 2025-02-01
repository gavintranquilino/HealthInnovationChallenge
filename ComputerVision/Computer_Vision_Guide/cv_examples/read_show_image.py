import cv2

# Load an image from file
image = cv2.imread('images/pose.jpg')

# Display the image in a window
cv2.imshow('Loaded Image', image)

# Wait until any key is pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
