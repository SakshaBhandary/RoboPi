import cv2

# Load pre-trained model (MobileNet SSD)
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet.caffemodel")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            if idx == 15:  # Class 15 is 'person'
                box = detections[0, 0, i, 3:7] * [frame.shape[1], frame.shape[0]] * 2
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    cv2.imshow("Person Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()