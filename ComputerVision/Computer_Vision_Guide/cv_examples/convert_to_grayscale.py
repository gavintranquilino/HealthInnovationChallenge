import cv2

# Load an image from file
image = cv2.imread('images/pose.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait until any key is pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
