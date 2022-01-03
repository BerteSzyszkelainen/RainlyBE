#!/usr/bin/python3
import requests


class MeasurementSender:

    def __init__(self, destination_url):
        self.destination_url = destination_url

    def send(self, year, month, day, clock_time, rainfall):
        requests.post(url=self.destination_url,
                                 data={'year': year,
                                       'month': month,
                                       'day': day,
                                       'clock_time': clock_time,
                                       'rainfall': rainfall})

        print("Successfully sent data!")


if __name__ == "__main__":
    MeasurementSender = MeasurementSender(destination_url=r'https://rainly-api.herokuapp.com/add_measurement')
    MeasurementSender.send(year="2022",
                           month="January",
                           day="5",
                           clock_time="18:00",
                           rainfall="1.00")
