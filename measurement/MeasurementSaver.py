#!/usr/bin/python3
import csv
import datetime


class MeasurementSaver:

    def __init__(self, destination_file):
        self.destination_file = destination_file

    def save(self, timestamp, rainfall):
        with open(self.destination_file, 'a', newline='') as file:
            fieldnames = ["timestamp", "year", "month", "day", "hour", "minute", "second", "rainfall"]
            row = {
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "year": timestamp.strftime("%Y"),
                "month": timestamp.strftime("%m"),
                "day": timestamp.strftime("%d"),
                "hour": timestamp.strftime("%H"),
                "minute": timestamp.strftime("%M"),
                "second": timestamp.strftime("%S"),
                "rainfall": rainfall
            }
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(row)
            print("Successfully saved data!")


if __name__ == "__main__":
    obj = MeasurementSaver(destination_file=r"test_rainfall.csv")
    obj.save(timestamp=datetime.datetime.now(), rainfall=10)