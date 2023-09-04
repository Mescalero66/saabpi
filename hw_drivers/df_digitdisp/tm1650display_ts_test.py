# The MIT License (MIT)
# 
# Test Code for Python Driver for:
# DFRobot DFR0645-R DFR0645-G <https://wiki.dfrobot.com/4-Digital%20LED%20Segment%20Display%20Module%20%20SKU:%20DFR0645-G_DFR0645-R>
# THIS IS NOT AN I2C DEVICE - IT WAS FUCKING ANNOYING TO GET IT TO WORK
#
# Shout out to CarlWilliamsBristol <https://github.com/CarlWilliamsBristol/pxt-tm1650display>

import time
from tm1650display_ts import Tm1650DisplayClass
import RPi.GPIO as GPIO

# connect to clockPin & dataPin
clockPin = 6
dataPin = 5

# create object
disp1 = Tm1650DisplayClass(clockPin, dataPin)
# disp1.sendStart()

# turn on with brightness (high 0 to low 7)
disp1.display_on(0)

# set communications speed (baud rate)
# disp1.setSpeed(100000)

# change brightness
br = 0
while br < 8:
    disp1.display_on(br)
    brString = 'Br ' + str(br)
    disp1.show_string(brString)
    br += 1
    time.sleep(2)

# display number
int = 125

while int < 250:
    print(int)
    disp1.show_integer(int)
    int += 1
    # time.sleep(0.5)

#####################################
##
## DECIMALS ALWAYS SHOW LAST DIGIT AS A 9
## DON'T KNOW WHY
##
#####################################

# display decimal number
disp1.show_decimal(12.34)
time.sleep(1)
disp1.show_decimal(56.78)
time.sleep(1)
disp1.show_decimal(9.10)
time.sleep(1)
disp1.show_decimal(112.1)
time.sleep(1)
disp1.show_decimal(3.1)
time.sleep(1)

# display hex code
disp1.show_hex(5)
time.sleep(1)

#######
#
# LETTERS STILL NOT WORKING
#
#######

# display character at a given position (0 - 3)
#disp1.show_char(0, "a")
#time.sleep(2)
#disp1.show_char(1, "b")
#time.sleep(2)
#disp1.show_char(2, "c")
#time.sleep(2)
#disp1.show_char(3, "d")
#time.sleep(2)

#display a string
disp1.show_string("5aab")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string("J0n0")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string("2023")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string("grnd")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string("head")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string(" alt")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string("engn")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)
disp1.show_string("360*")
time.sleep(2)
disp1.show_string("----")
time.sleep(1)

disp1.show_string("abcdefg")
time.sleep(3)

# clear display
disp1.display_clear()
time.sleep(3)

# display off
disp1.display_off()