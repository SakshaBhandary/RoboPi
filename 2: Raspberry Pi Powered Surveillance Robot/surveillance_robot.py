import cv2
import time

# Load pre-trained MobileNet SSD model with Caffe config for object detection
net = cv2.dnn.readNetFromCaffe(
    'deploy.prototxt.txt', 
    'mobilenet_iter_73000.caffemodel'
)

# Define class labels MobileNet SSD was trained on (COCO subset)
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]
TARGETS = {"person", "cat", "dog", "horse", "cow", "sheep", "bird"}

# Start video capture from Pi camera or USB cam
cap = cv2.VideoCapture(0)
time.sleep(2)  # Warm-up time

while True:
    ret, frame = cap.read()
    if not ret:
        break

    (h, w) = frame.shape[:2]

    # Preprocess input for model
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        0.007843, (300, 300), 127.5
    )
    net.setInput(blob)
    detections = net.forward()

    # Loop over detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            if label in TARGETS:
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")

                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(frame, f"{label}: {confidence:.2f}",
                            (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255), 2)

    cv2.imshow("Surveillance Robot", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()