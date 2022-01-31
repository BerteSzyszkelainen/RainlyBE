#!/usr/bin/python3
from measurement.MeasurementReader import MeasurementReader
from measurement.MeasurementSender import MeasurementSender


class MeasurementProcessor(object):

    def __init__(self):
        pass

    def run(self):
        measurementReader = MeasurementReader(interval=300)
        measurementSender = MeasurementSender(destination_url=r'http://localhost:5000/add_measurement')

        while True:
            rainfall, temperature, humidity, pressure, wind_speed_avg, wind_speed_max, wind_direction, date = measurementReader.read_fake()
            measurementSender.send(
                rainfall=rainfall,
                temperature=temperature,
                humidity=humidity,
                pressure=pressure,
                wind_speed_avg=wind_speed_avg,
                wind_speed_max=wind_speed_max,
                wind_direction=wind_direction,
                date=date
            )
