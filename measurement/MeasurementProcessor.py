#!/usr/bin/python3
from measurement.MeasurementReader import MeasurementReader
from measurement.MeasurementSaver import MeasurementSaver


class MeasurementProcessor(object):

    def __init__(self):
        self.measurement_reader = MeasurementReader(interval=300)
        self.measurement_saver = MeasurementSaver(destination_file=r'/home/rainly/Projects/RainlyBE/data/rainfall')

    def run(self):

        while True:
            timestamp, rainfall = self.measurement_reader.read()
            self.measurement_saver.save(
                timestamp=timestamp,
                rainfall=rainfall
            )

if __name__ == '__main__':
    obj = MeasurementProcessor()
    obj.run()
