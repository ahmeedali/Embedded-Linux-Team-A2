#! /usr/bin/python3

from pynotifier import Notification
import psutil

battery = psutil.sensors_battery()
percent = battery.percent
#print(percent)
Notification('Battery' ,str(percent), duration = 10).send()