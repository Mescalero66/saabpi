## log in via terminal
ssh pi@raspberrypi.local

## update pi and reboot
sudo apt update && sudo apt full-upgrade --yes && sudo reboot

## install  Git, Pip
sudo apt install git python3-dev python3-pip --yes

## clone grove.py repo 
git clone https://github.com/Seeed-Studio/grove.py
cd grove.py
sudo pip3 install . --break-system-packages

## enable I2C interface
sudo raspi-config nonint do_i2c 0

## install i2Ctools
sudo apt-get install i2c-tools

## install SoftI2C on I2C bus8, GPIO 23(SDA) and GPIO24(SCL) (not yet req'd)
dtoverlay=i2c-gpio,bus=8

this should be added to /boot/config.txt (then reboot)

<https://learn.adafruit.com/raspberry-pi-i2c-clock-stretching-fixes/software-i2c>

<https://github.com/fivdi/i2c-bus/blob/master/doc/raspberry-pi-software-i2c.md>

## identify I2C buses
ls /dev/i2c*

## START PIGPIO (must be done on every system start up somehow)
sudo pigpiod

## scan I2C devices
i2cdetect -y [bus]

i.e.
i2cdetect -y 1
would scan I2C bus #1 for devices

## install pynmeagps - to read NMEA GPS data
python3 -m pip install --upgrade pynmeagps --break-system-packages

## intall Pillow
sudo python3 -m pip install --upgrade pip --break-system-packages
sudo python3 -m pip install --upgrade Pillow --break-system-packages

## adafruit SSD1306 Drivers
sudo pip install Adafruit-SSD1306 --break-system-packages

## install pyserial
sudo pip3 install pyserial --break-system-packages

## reboot
sudo reboot