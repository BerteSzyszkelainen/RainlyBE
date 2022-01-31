#!/usr/bin/python3
import datetime
import locale
from random import random

from gpiozero import Button
from utilities import utilities

locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")


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
        utilities.wait_for(interval=self.interval)
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

    def read_fake(self):
        utilities.wait_for(interval=self.interval)
        rainfall = round(random.uniform(0, 4), 1)
        temperature = round(random.uniform(-5, 8), 1)
        humidity = round(random.uniform(60, 90), 1)
        pressure = round(random.uniform(980, 1020), 1)
        wind_speed_avg = round(random.uniform(0, 35), 1)
        wind_speed_max = round(random.uniform(5, 60), 1)
        wind_direction = round(random.uniform(0, 360), 1)
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return rainfall, temperature, humidity, pressure, wind_speed_avg, wind_speed_max, wind_direction, date
