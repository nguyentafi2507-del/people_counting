from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort(
            max_age=60,
            max_cosine_distance=0.2,
        )

    def update(self, detections, frame):
        bbs = []

        for detection in detections:
            # detection = [x, y, w, h, conf]
            bbs.append((detection[:4], detection[4], "person"))

        tracks = self.tracker.update_tracks(bbs, frame=frame)

        res = []
        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            ltrb = track.to_ltrb()

            res.append(list(ltrb) + [track_id])

        return res