from ultralytics import YOLO

model = YOLO("yolo26s.pt")

results = model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=4,
)

