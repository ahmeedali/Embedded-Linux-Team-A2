#!/usr/bin/python3

from pynotifier import Notification
import psutil

battery = psutil.sensors_battery()
percent = f"{battery.percent:.2f}"

def Notify():
    Notification(
    title="Battery percentage:",
    description=percent + "% Remaining",
    duration=5,  # Duration in seconds       
    ).send()

# Todo: add class with methods to get battery info

if __name__ == '__main__':
    Notify()