# displayText.py
#
# Description:
# Prints text to an SSD1306 display module using the Adafruit_Python_SSD1306
# and Python Imaging Library (PIL) libraries.
#
# Created by John Woolsey on 07/05/2018.
# Copyright (c) 2018 Woolsey Workshop.  All rights reserved.

import SSD1306 as oled1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

# Adafruit_Python_SSD1306 graphics library configuration for
# SunFounder OLED SSD1306 Display Module.
# Use the configuration compatible with your display module.
# See library "examples" directory for configuration selection.
# 128x64 display with hardware I2C and no reset pin
display = oled1306.SSD1306_128_64(rst=None)
# Setup
display.begin()  # initialize graphics library for selected display module
display.clear()  # clear display buffer
display.display()  # write display buffer to physical display
displayWidth = display.width  # get width of display
displayHeight = display.height  # get height of display
image = Image.new('1', (displayWidth, displayHeight))  # create graphics library image buffer
draw = ImageDraw.Draw(image)  # create drawing object
font = ImageFont.load_default()  # load and set default font

# Draw text
draw.text((0,0), "Hello,\nRaspberry Pi!", font=font, fill=255)  # print text to image buffer
# Display to screen
display.image(image)  # set display buffer with image buffer
display.display()  # write display buffer to physical display
# Cleanup
GPIO.cleanup()  # release all GPIO resources