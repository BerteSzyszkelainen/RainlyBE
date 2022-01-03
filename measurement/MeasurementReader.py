#!/usr/bin/python3
import datetime
from gpiozero import Button
import time

def wait_for(interval):
    start_time = time.time()
    while time.time() - start_time <= interval:
        print("Measurement in process...")
        time.sleep(2)

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
        self.reset_rainfall()
        current_timestamp = datetime.datetime.now()
        year = current_timestamp.strftime("%Y")
        month = current_timestamp.strftime("%B")
        day = current_timestamp.strftime("%d")
        clock_time = current_timestamp.strftime("%H:%M:%S")
        print("Successfully read data, year: {}, month: {}, day: {}, clock_time: {},  rainfall: {}".format(year,
                                                                                                           month,
                                                                                                           day,
                                                                                                           clock_time,
                                                                                                           rainfall))
        return year, month, day, clock_time, rainfall
        
       
if __name__ == "__main__":
    measurementReader = MeasurementReader(interval=10)
    measurementReader.read()
