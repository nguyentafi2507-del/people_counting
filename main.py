import cv2
import os
import time
from ultralytics import YOLO

from tracker.deepsort import Tracker
from utils.counter import Counter
from utils.zone import Zone
from utils.draw import Drawer
from utils.config import *

#Load model
model = YOLO("runs/detect/train/weights/best.pt")

#Init modules
tracker = Tracker()
counter = Counter(LINE_X)
zone = Zone(LINE_X)
drawer = Drawer()

#Video source
cap = cv2.VideoCapture("demo/demo.mp4")

#Tạo folder demo
os.makedirs("demo", exist_ok=True)

#Video writer
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 25

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_path = f"TEST/output_{int(time.time())}.mp4"

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

print(f"Saving video to: {output_path}")

#FPS calculation
prev_time = time.time()

#Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Cắt ROI
    roi_frame = frame[ROI_Y1:ROI_Y2, ROI_X1:ROI_X2]

    #Detect trên ROI
    results = model(roi_frame)[0]

    detections = []

    for box, cls, conf in zip(results.boxes.xyxy, results.boxes.cls, results.boxes.conf):
        if conf < CONF_THRESHOLD:
            continue

        class_id = int(cls.item())
        label = results.names[class_id]

        if label != "person":
            continue

        x1, y1, x2, y2 = box.tolist()

        #Map về frame gốc
        x1 += ROI_X1
        y1 += ROI_Y1
        x2 += ROI_X1
        y2 += ROI_Y1

        # convert xywh
        w = x2 - x1
        h = y2 - y1

        detections.append([x1, y1, w, h, float(conf)])

    #Tracking
    tracks = tracker.update(detections, frame)

    #Counting
    left, right = counter.update(tracks)

    # Drawing
    frame = drawer.draw_tracks(frame, tracks)
    frame = drawer.draw_count(frame, left, right)
    frame = zone.draw(frame)

    #FPS
    curr_time = time.time()
    fps_display = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(frame, f"FPS: {int(fps_display)}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #Show
    cv2.imshow("People Counting", frame)

    # ===== 9. Save =====
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# ===== Cleanup =====
cap.release()
out.release()
cv2.destroyAllWindows()