#!/usr/bin/python3
import requests


class MeasurementSender:

    def __init__(self, destination_url):
        self.destination_url = destination_url

    def send(self, rainfall, temperature, humidity, pressure, wind_speed_avg, wind_speed_max, wind_direction, date):
        requests.post(
            url=self.destination_url,
            data={
                'rainfall': rainfall,
                'temperature': temperature,
                'humidity': humidity,
                'pressure': pressure,
                'wind_speed_avg': wind_speed_avg,
                'wind_speed_max': wind_speed_max,
                'wind_direction': wind_direction,
                'date': date
            }
        )
        print("Successfully sent data!")
