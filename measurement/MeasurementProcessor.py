#!/usr/bin/python3
from measurement.MeasurementReader import MeasurementReader
from measurement.MeasurementSender import MeasurementSender


class MeasurementProcessor(object):

    def __init__(self):
        self.measurement_reader = MeasurementReader(interval=300)
        self.measurement_sender = MeasurementSender(destination_url=r'https://rainly-api.herokuapp.com/add_measurement')

    def run(self):

        while True:
            year, month, day, clock_time, rainfall = self.measurement_reader.read()
            self.measurement_sender.send(year=year,
                                         month=month,
                                         day=day,
                                         clock_time=clock_time,
                                         rainfall=rainfall)

if __name__ == "__main__":
    measurement_processor = MeasurementProcessor()
    measurement_processor.run()
    print("Measurement processor executed successfully!")
