import cv2

# Use Pi Camera by accessing the proper device (0 or /dev/video0)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not cap.isOpened():
    print("Error: Could not access Pi Camera.")
    exit()

print("Press 'q' to exit the camera feed.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the frame
    cv2.imshow("Raspberry Pi Camera Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
