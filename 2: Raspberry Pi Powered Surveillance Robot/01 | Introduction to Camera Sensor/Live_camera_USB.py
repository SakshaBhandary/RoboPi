import cv2

# Start video capture (0 is usually the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Show the video frame
    cv2.imshow("Live Camera Feed", frame)

    # Press 'q' to quit the feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destroy windows
cap.release()
cv2.destroyAllWindows()
