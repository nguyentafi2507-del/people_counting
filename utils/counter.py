class Counter:
    def __init__(self, line_x):
        self.line_x = line_x

        self.left_count = 0
        self.right_count = 0

        self.counted_ids = set()
        self.prev_positions = {}

    def update(self, tracks):
        for x1, y1, x2, y2, track_id in tracks:
            cx = int((x1 + x2) / 2)

            prev_cx = self.prev_positions.get(track_id, None)

            if prev_cx is not None:
                # trái → phải
                if prev_cx < self.line_x and cx >= self.line_x:
                    if track_id not in self.counted_ids:
                        self.right_count += 1
                        self.counted_ids.add(track_id)

                # phải → trái
                elif prev_cx > self.line_x and cx <= self.line_x:
                    if track_id not in self.counted_ids:
                        self.left_count += 1
                        self.counted_ids.add(track_id)

            self.prev_positions[track_id] = cx

        return self.left_count, self.right_count