import cv2
import numpy as np

# Load image
img = cv2.imread('sample.jpg')
blurred = cv2.GaussianBlur(img, (9, 9), 0)

# Sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Blurred", blurred)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()