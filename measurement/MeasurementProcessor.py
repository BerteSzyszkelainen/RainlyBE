#!/usr/bin/python3
from measurement.MeasurementReader import MeasurementReader
from measurement.MeasurementSender import MeasurementSender


class MeasurementProcessor(object):

    def __init__(self):
        self.measurement_reader = MeasurementReader(interval=300)
        self.measurement_sender = MeasurementSender(destination_url=r'https://rainly-api.herokuapp.com/add_measurement')

    def run(self):

        while True:
            rainfall, temperature, humidity, pressure, wind_speed_avg, wind_speed_max, wind_direction, date = self.measurementReader.read_fake()
            self.measurement_sender.send(
                rainfall=rainfall,
                temperature=temperature,
                humidity=humidity,
                pressure=pressure,
                wind_speed_avg=wind_speed_avg,
                wind_speed_max=wind_speed_max,
                wind_direction=wind_direction,
                date=date
            )

if __name__ == '__main__':
    measurement_processor = MeasurementProcessor()
    measurement_processor.run()