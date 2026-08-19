from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train-4/weights/best.pt")

image = cv2.imread("images/test1.png")

results = model(image)

result = results[0]

for box in result.boxes:

    class_id = int(box.cls[0])

    confidence = float(box.conf[0])

    x1,x2,x3,x4 = map(int, box.xyxy[0])

    class_name = model.names[class_id]

    cv2.rectangle(
        image,
        (x1,x2),
        (x3,x4),
        (0,255,0),
        2
    )

    label = f"{class_name}"

    cv2.putText(
        image,
        label,
        (x1,x2 - 10),
        cv2.FONT_HERSHEY_COMPLEX,
        0.6,
        (0,255,0),
        2
    )

cv2.imshow("Yolo Output", image)

cv2.waitKey(0)
cv2.destroyAllWindows()