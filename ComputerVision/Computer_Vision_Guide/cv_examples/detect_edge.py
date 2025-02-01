import cv2

# Load an image from file
image = cv2.imread('images/pose.jpg')

# Apply Canny edge detection
threshold_1 = 100   # try tunning these thresholds and see the changes!
threshold_2 = 200
edges = cv2.Canny(image, threshold_1, threshold_2)

# Display the edges
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
