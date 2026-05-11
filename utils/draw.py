import cv2
from utils.config import *

class Drawer:
    def draw_tracks(self, frame, tracks):
        for x1, y1, x2, y2, track_id in tracks:
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

            # cv2.rectangle(frame, (x1, y1), (x2, y2), BOX_COLOR, THICKNESS)

            cv2.putText(
                frame,
                f"ID: {track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                TEXT_COLOR,
                THICKNESS
            )
        return frame

    def draw_count(self, frame, left, right):
        cv2.putText(frame, f"Left: {left}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.putText(frame, f"Right: {right}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        return frame