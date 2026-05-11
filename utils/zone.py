import cv2
from utils.config import *

class Zone:
    def __init__(self, line_x):
        self.line_x = line_x

    def draw(self, frame):
        # vẽ ROI box
        cv2.rectangle(
            frame,
            (ROI_X1, ROI_Y1),
            (ROI_X2, ROI_Y2),
            ROI_COLOR,
            2
        )

        # vẽ line dọc
        cv2.line(
            frame,
            (self.line_x, ROI_Y1),
            (self.line_x, ROI_Y2),
            LINE_COLOR,
            THICKNESS
        )

        return frame