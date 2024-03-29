# MIT License
# Copyright (c) 2024 Mescalero
# <https://github.com/Mescalero66/saabpi>
# Project v1.1 - Released 20240224

import grove_4digitdisp
import time

display = grove_4digitdisp.Grove4DigitDisplay(12, 13)
count = 0

display.show("SAAB")
time.sleep(2)

while True:
    t = time.strftime("%H%M", time.localtime(time.time()))
    display.show(t)
    display.set_colon(count & 1)
    count += 1
    time.sleep(1)