# People Counting using YOLOv8 + DeepSORT

A real-time people counting system using YOLOv8 for person detection and DeepSORT for multi-object tracking.

The system counts people moving from left to right and right to left inside a selected ROI (Region of Interest).

---

## Features

- Real-time people detection
- DeepSORT tracking
- Left / Right people counting
- ROI-based detection
- Vertical counting line
- Video output saving
- Custom YOLO model support

---

## Pipeline

```text
Video Input
    ↓
ROI Selection
    ↓
YOLOv8 Detection
    ↓
DeepSORT Tracking
    ↓
Direction Counting
    ↓
Output Video
