import time

class frame_counter():
    def __init__(self):
        self.fps = 0
        self.count = 0
        self.start_time = time.time()
    def frame(self):
        self.count += 1
        t = time.time()
        if t - self.start_time > 1:
            self.fps = self.count / (t - self.start_time)
            self.start_time = t
            self.count = 0