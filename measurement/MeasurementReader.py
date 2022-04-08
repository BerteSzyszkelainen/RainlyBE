#!/usr/bin/python3
import datetime

from gpiozero import Button
import time

def wait_for(interval):
    start_time = time.time()
    while time.time() - start_time <= interval:
        print("Measurement in process...")
        time.sleep(10)

class MeasurementReader(object):
    BUCKET_SIZE = 0.2794

    def __init__(self, interval):
        self.interval = interval
        self.sensor = Button(6)
        self.tip_count = 0
        self.sensor.when_pressed = self.bucket_tipped

    def bucket_tipped(self):
        self.tip_count = self.tip_count + 1

    def reset_rainfall(self):
        self.tip_count = 0

    def read(self):
        wait_for(interval=self.interval)
        rainfall = round(self.tip_count * self.BUCKET_SIZE, 2)
        timestamp = datetime.datetime.now()
        self.reset_rainfall()
        print(f"Read rainfall: {rainfall} mm at timestamp {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        return timestamp, rainfall

if __name__ == "__main__":
    obj = MeasurementReader(interval=20)
    obj.read()


