# Resize the image to half its original size
import cv2

# Load an image from file
image = cv2.imread('images/pose.jpg')

resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
