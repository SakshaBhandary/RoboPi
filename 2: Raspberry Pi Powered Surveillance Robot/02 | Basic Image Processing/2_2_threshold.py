import cv2

# Load grayscale image
img = cv2.imread('sample.jpg', 0)

# Apply threshold
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Original", img)
cv2.imshow("Binary Threshold", binary)
cv2.imshow("Otsu Threshold", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()