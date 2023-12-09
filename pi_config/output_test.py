# MIT License
# Copyright (c) 2023 Mescalero
# <https://github.com/Mescalero66/saabpi>
# Project v1.0 - Released 20231209

import RPi.GPIO as GPIO
import time

i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

while i < 100:
    GPIO.output(5, 1)
    print("HIGH", i)
    time.sleep(0.5)
    GPIO.output(5, 0)
    print("LOW", i)
    time.sleep(0.5)
    i += 1